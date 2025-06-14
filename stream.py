import os
import time

STREAM_KEY = os.getenv("STREAM_KEY")
if not STREAM_KEY:
    raise Exception("STREAM_KEY environment variable not set.")

# YouTube RTMP URL
rtmp_url = f"rtmp://a.rtmp.youtube.com/live2/{STREAM_KEY}"

# Loop forever
while True:
    print("Starting stream...")
    command = (
        "ffmpeg -re -stream_loop -1 -i video.mp4 "
        "-c:v libx264 -preset veryfast -b:v 800k -
