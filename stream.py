import ffmpeg

# 🔑 अपनी YouTube Live Stream Key यहाँ डालो:
stream_key = "cffy-8rw9-abtc-wzb2-7u8w"  # ← आपकी key

# 🔗 YouTube RTMP URL तैयार करो:
stream_url = f"rtmp://a.rtmp.youtube.com/live2/{stream_key}"

# 🎬 वीडियो को इनपुट लेकर YouTube पर भेजो
ffmpeg.input("video.mp4", stream_loop=-1).output(
    stream_url,
    format='flv',
    vcodec='libx264',
    video_bitrate='500k',  # bitrate कम रखो ताकि stream टिके
    s='640x360',            # 360p resolution
    r=25,                   # frame rate
    acodec='aac',
    audio_bitrate='128k'
).run()
