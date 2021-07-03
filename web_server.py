import uvicorn
from vidgear.gears.asyncio import WebGear


options = {
    'frame_size_reduction': 40,
    'frame_jpeg_quality': 80,
    'frame_jpeg_optimize': True,
    'frame_jpeg_progressive': False
}

web = WebGear(source='test.mp4', logging=True, **options)

uvicorn.run(app=web(), host='localhost', port=8000)

web.shutdown()
