import asyncio
import websockets


async def handler(websocket, path):
    data = await websocket.recv()
    reply = f"Data received as: {data}!"
    print(reply)

    await websocket.send(reply)


async def main():
    async with websockets.serve(handler, "localhost", 8000):
        await asyncio.Future()  # блокуємо код, щоб сервер працював постійно


if __name__ == '__main__':
    asyncio.run(main())
