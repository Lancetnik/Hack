import asyncio
import multiprocessing
from typing import NoReturn

import grpc
from loguru import logger

from .endpoints import Sender
from .schema import websockets_pb2_grpc


def create_server(port=8002):
    server = grpc.aio.server()
    websockets_pb2_grpc.add_SenderServicer_to_server(Sender(), server)
    listen_addr = f'[::]:{port}'
    logger.info(f"Bind grpc server to {port} port")
    server.add_insecure_port(listen_addr)
    return server


async def start_server(server) -> NoReturn:
    logger.info("Starting grpc server")
    await server.start()
    await server.wait_for_termination()


def start_server_process(server):
    loop = asyncio.get_event_loop()
    future = loop.create_task(start_server(server))
    proc = multiprocessing.Process(target=loop.run_forever, args=[future], daemon=True)
    proc.start()
    return proc
