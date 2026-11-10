import time

import socketio

# Create a Socket.IO client
sio = socketio.Client()


@sio.event
def connect():
    print("Connected to server")

    # Emit the event 5 times
    for i in range(420):
        sio.emit("add", {"team": "homeTeamStatistics"})
        print(f"Emit {i + 1}/5 sent")
        time.sleep(.01)


@sio.event
def disconnect():
    print("Disconnected from server")


# Connect to the WebSocket server
sio.connect("wss://oilerssog.iktim.no")

# Keep the connection alive
sio.wait()
