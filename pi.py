from vidgear.gears import PiGear
from vidgear.gears import NetGear
from vidgear.gears import VideoGear


# stream = PiGear().start()
stream = VideoGear(source=0).start()
options = {
    'flag': 0,
    'copy': False,
    'track': False,
    'ssh_tunel_mode': 'pi@192.168.11.1',
    'ssh_tunel_pwd': 'raspberry',
    'ssh_tunnel_keyfile': '/home/pi/id_rsa'
}

server = NetGear(
    address='localhost',
    port='5454',
    protocol='tcp',
    pattern=2,
    logging=True,
    receive_mode=False,
    **options
)

while True:
    try:
        frame = stream.read()

        if frame is None:
            break

        server.send(frame=frame)
        print('sending...')
    except KeyboardInterrupt:
        break

stream.stop()
server.close()
