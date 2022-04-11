import grpc

from .schema import websockets_pb2, websockets_pb2_grpc


class Sender(websockets_pb2_grpc.SenderServicer):
    async def SendMessage(
            self,
            request: websockets_pb2.Message,
            context: grpc.aio.ServicerContext) -> websockets_pb2.Reply:
        print(request.name)
        return websockets_pb2.Reply(message='Hello, %s!' % request.name)
