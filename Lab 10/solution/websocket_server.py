import asyncio
import websockets
from win10toast import ToastNotifier

logged_users = {}
toaster = ToastNotifier()
count = 0
user, to_user = "", ""


async def response(websocket, path):
    message = await websocket.recv()
    print(f'I got message from client: {message}')

    message_spl = message.split(',')
    logged_users[message_spl[0]] = message_spl[1]
    print(logged_users)
    await websocket.send(f"User: {message_spl[0]} has login status: {message_spl[1]}")
    if message_spl[1] == "True":
        status = "Available"
    else:
        status = "Not available"

    toaster.show_toast("You have new notification", f"User: {message_spl[0]} is: {status}", duration=10)


async def msg(websocket, path):
    got_message = await websocket.recv()
    print(f'I got message from client: {got_message}')

    await websocket.send(f"{got_message}")
    toaster.show_toast(f"You have new notification", f'{got_message}', duration=10)


async def msgOpened(websocket, path):
    got_message = await websocket.recv()
    print(f'I got message from client: {got_message}')

    await websocket.send(f"{got_message}")
    toaster.show_toast(f"You have new notification", f'{got_message}', duration=10)


async def msg_count(websocket, path):
    global count, user, to_user
    got_message = await websocket.recv()
    print(f'I got message from client: {got_message}')

    got_message_split = got_message.split(',')

    user, to_user = got_message_split[0], got_message_split[1]

    if got_message_split[0] == "" and got_message_split[1] == "" and got_message_split[2] == "":
        await websocket.send(f"{user},{to_user},{count}")

    if got_message_split[2] == '0':
        count = 0
    else:
        count += int(got_message_split[2])

    await websocket.send(f"{got_message_split[0]},{got_message_split[1]},{count}")

    toaster.show_toast(f"You have new notification", f"From User: {got_message_split[0]}", duration=10)


print("Websocket Server is started")
websocket_server = websockets.serve(response, 'localhost', 12345)
asyncio.get_event_loop().run_until_complete(websocket_server)

websocket_server_message = websockets.serve(msg, 'localhost', 1234)
asyncio.get_event_loop().run_until_complete(websocket_server_message)

websocket_server_message = websockets.serve(msgOpened, 'localhost', 1222)
asyncio.get_event_loop().run_until_complete(websocket_server_message)

websocket_server = websockets.serve(msg_count, 'localhost', 55555)
asyncio.get_event_loop().run_until_complete(websocket_server)

asyncio.get_event_loop().run_forever()


