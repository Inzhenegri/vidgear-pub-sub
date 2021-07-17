from vidgear.gears import PiGear
from vidgear.gears import NetGear
from vidgear.gears import VideoGear
import cv2
import threading


def camera_1():
    while True:
        _1, frame_1 = stream_1.read()
        if frame_1 is not None:
            server_1.send(frame=frame_1)


def camera_2():
    while True:
        _2, frame_2 = stream_2.read()
        if frame_2 is not None:
            server_2.send(frame=frame_2)

options_netgear = {
    'flag': 0,
    'copy': False,
    'track': False,
    "jpeg_compression_quality": 70,
    'jpeg_compression_fastupsample': True
}

stream_1 = cv2.VideoCapture(0)
stream_1.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
stream_1.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

stream_2 = cv2.VideoCapture(2)
stream_2.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
stream_2.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

server_1 = NetGear(
    address='192.168.11.159', # school network
    # address='192.168.11.137', # home network
    port='5462',
    protocol='tcp',
    pattern=2,
    logging=True,
    receive_mode=False,
    **options_netgear
)

server_2 = NetGear(
    address='192.168.11.159', # school network
    # address='192.168.11.137', # home network
    port='5463',
    protocol='tcp',
    pattern=2,
    logging=True,
    receive_mode=False,
    **options_netgear
)

camera_thread_1 = threading.Thread(target=camera_1, args=())
camera_thread_2 = threading.Thread(target=camera_2, args=())

camera_thread_1.start()
camera_thread_2.start()

while True:
    pass
    # try:
    #     _1, frame_1 = stream_1.read()
    #     _2, frame_2 = stream_2.read()

    #     if frame_1 is None:
    #         break
    #     if frame_2 is None:
    #         break

    #     server_1.send(frame=frame_1)
    #     server_2.send(frame=frame_2)

    #     print('sending...')
    # except KeyboardInterrupt:
    #     break

# stream_1.release()
# stream_2.release()

# server_1.close()
# server_2.close()
