import os
import time

# Stream key directly डाल दी गई है (unsafe for public repos)
STREAM_KEY = "cffy-8rw9-abtc-wzb2-7u8w"
rtmp_url = f"rtmp://a.rtmp.youtube.com/live2/{STREAM_KEY}"

while True:
    print("🔴 Starting stream...")
    command = (
        "ffmpeg -re -stream_loop -1 -i video.mp4 "
        "-c:v libx264 -preset veryfast -b:v 800k -maxrate 800k -bufsize 1000k "
        "-vf scale=640:360 "
        "-c:a aac -ar 44100 -b:a 128k -f flv "
        + rtmp_url
    )
    os.system(command)
    print("⚠️ Stream stopped. Restarting in 5 seconds...")
    time.sleep(5)
