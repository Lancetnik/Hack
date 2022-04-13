import requests
import urllib3
import polyline

from loguru import logger
from bs4 import BeautifulSoup

from findStrava.additional.meta_strava.meta import META_INFO, META_STATUS

urllib3.disable_warnings()

def get_route():
    if META_STATUS:
        auth_url = "https://www.strava.com/oauth/token"

        payload = {
            'client_id': "80721",
            'client_secret': 'c0023d16ae9d11c137422a1808680da98ee2f72c',
            'refresh_token': '4163779b7169975d9588b0646dce2f24b8228a85',
            'grant_type': "refresh_token",
            'f': 'json'
        }

        session = requests.Session()
        res = session.post(auth_url, data=payload, verify=False)
        access_token = res.json()['access_token']

        headers = {'Authorization': 'Bearer ' + access_token, 'Accept-Language': 'pl,en-US;q=0.7,en;q=0.3'}
        params = {'per_page': 200, 'page': 1}

        logger.debug(res)

        login_response = session.get('https://strava.com/login')

        soup = BeautifulSoup(login_response.text)
        token = soup.find('input', {'name': 'authenticity_token'}).get('value')

        auth = session.post('https://www.strava.com/session', 
                            data={'email':'slovplan@mail.ru',
                                'password':'strava1488', 
                                'authenticity_token': token
                                }
                        )


        coords=['60.002403','30.02001','60.016741','30.986722']

        response = session.get(
            f'https://www.strava.com/api/v3/segments/explore?bounds={coords[0]},{coords[1]},{coords[2]},{coords[3]}&activity_type=running', 
                            headers=headers, params=params
                            )
        power_data = response.json()

        points = []
        for i in power_data['segments']:
            elem = session.get('https://www.strava.com/api/v3/segments/{}'.format(i["id"]), 
            headers=headers, params=params
            )
            name = elem.json()['local_legend']['title']
            id_user = elem.json()['local_legend']['athlete_id']
            points.append({
                'id':id_user,
                'name':str(name),
                'coordinates':polyline.decode(i['points'])
                })
    else:
        points = META_INFO
    return points
