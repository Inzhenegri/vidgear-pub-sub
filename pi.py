from vidgear.gears import PiGear
from vidgear.gears import NetGear
from vidgear.gears import VideoGear
import cv2


options_pigear = {
    "exposure_mode": "off",
    "iso": 100,
    # "exposure_compensation": -25,
    # "awb_mode": "horizon",
    # "sensor_mode": 0,
}

options_netgear = {
    'flag': 0,
    'copy': False,
    'track': False,
    # frame compression
    "jpeg_compression_quality": 50,
    'jpeg_compression_fastupsample': True
}

# stream = PiGear(
#     resolution=(320, 240),
#     framerate=60,
#     logging=True,
#     **options_pigear
# ).start()
stream = cv2.VideoCapture(0)

server = NetGear(
    # address='192.168.11.145', # school network
    address='192.168.11.137', # home network
    port='5454',
    protocol='tcp',
    pattern=2,
    logging=True,
    receive_mode=False,
    **options_netgear
)

while True:
    try:
        _, frame = stream.read()

        if frame is None:
            break

        server.send(frame=frame)
        print('sending...')
    except KeyboardInterrupt:
        break

# stream.stop()
server.close()
