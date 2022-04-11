import logging

import grpc

from grpc_api.schema import websockets_pb2, websockets_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:8002') as channel:
        stub = websockets_pb2_grpc.SenderStub(channel)
        response = stub.SendMessage(websockets_pb2.Message(name='me'))
    # print("Greeter client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
