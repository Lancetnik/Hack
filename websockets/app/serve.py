import argparse
    
from fastapi import FastAPI

from api import api_router
from grpc_api.utils import create_server, start_server_process


app = FastAPI()

parser = argparse.ArgumentParser()
parser.add_argument('--port', nargs='?', type=int, default=8001, help='the listening port')
args, unknown = parser.parse_known_args()


@app.on_event("startup")
async def startup() -> None:
    server = create_server(args.port + 1)
    app.state.grpc_server = server
    app.state.grpc_server_process = start_server_process(server)


@app.on_event("shutdown")
async def shutdown() -> None:
    await app.state.grpc_server.stop(1)
    app.state.grpc_server_process.terminate()


app.include_router(api_router)
