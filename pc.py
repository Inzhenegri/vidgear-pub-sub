from vidgear.gears import VideoGear
from vidgear.gears import NetGear
from vidgear.gears import ScreenGear
from vidgear.gears.asyncio import WebGear
from vidgear.gears.asyncio.helper import reducer
import cv2
import uvicorn
import asyncio


options = {
    'copy': False,
    'track': False
}

options_webgear = {
    'frame_size_reduction': 40,
    'frame_jpeg_quality': 100,
    'frame_jpeg_optimize': True,
    'frame_jpeg_progressive': False
}

client = NetGear(
    # address='192.168.11.145', # school network
    address='192.168.11.137', # home network
    port='5454',
    pattern=2,
    receive_mode=True,
    logging=True,
    protocol='tcp',
    **options
)

web = WebGear(logging=True, **options_webgear)

async def frame_producer():
    stream = ScreenGear().start()
    while True:
        frame = client.recv()

        if frame is None:
            break

        frame = await reducer(frame=frame, percentage=30)
        encoded_image = cv2.imencode(ext='.jpg', img=frame)[1].tobytes()

        yield (b"--frame\r\nContent-Type:video/jpeg2000\r\n\r\n" + encoded_image + b"\r\n")
        await asyncio.sleep(0.00001)

    stream.release()
    

web.config['generator'] = frame_producer
uvicorn.run(app=web(), host='localhost', port=8000)

web.shutdown()

cv2.destroyAllWindows()

