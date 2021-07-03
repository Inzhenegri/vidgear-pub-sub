from vidgear.gears import VideoGear
from vidgear.gears import NetGear
import cv2


options = {
    'copy': False,
    'track': False
}

client = NetGear(
    address='127.0.0.1',
    port='5454',
    pattern=2,
    receive_mode=True,
    logging=True,
    protocol='tcp',
    **options
)

while True:
    frame = client.recv()
    print(frame)

    if frame is None:
        break

    cv2.imshow('out', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
client.close()
