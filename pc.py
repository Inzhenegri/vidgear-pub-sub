from vidgear.gears import NetGear
import cv2
import asyncio


options = {
    'flag': 0,
    'copy': False,
    'track': False
}

client = NetGear(
    address='192.168.11.159', # school network
    # address='192.168.11.137', # home network
    port='5454',
    pattern=2,
    receive_mode=True,
    logging=True,
    protocol='tcp',
    **options
)

async def start():
    while True:
        frame = client.recv()

        if frame is None:
            break

        cv2.imshow('frame', frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

        await asyncio.sleep(0.00001)


asyncio.run(main=start())

cv2.destroyAllWindows()
client.close()
