import ffmpeg

# 🔑 अपनी YouTube stream key यहाँ डालो:
stream_key = "cffy-8rw9-abtc-wzb2-7u8w"
stream_url = f"rtmp://a.rtmp.youtube.com/live2/{stream_key}"

# 🔁 Loop में वीडियो चलाकर Live करो
ffmpeg.input("video.mp4", stream_loop=-1).output(
    stream_url,
    format='flv',
    vcodec='libx264',
    video_bitrate='500k',
    s='640x360',
    r=25,
    acodec='aac',
    audio_bitrate='128k'
).run()
