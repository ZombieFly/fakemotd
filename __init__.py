import asyncio
import socket

import BedrockFakeMotd


def handle_client(data):
    response = BedrockFakeMotd.summ_motd(data)
    return response


async def run_server():
    while True:
        data, addr = server.recvfrom(2048)
        server.sendto(handle_client(data), addr)

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 19132))

loop = asyncio.get_event_loop()
loop.run_until_complete(run_server())
