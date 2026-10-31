import subprocess, os, time
KEY = os.getenv("YOUTUBE_KEY", "0jpp-vt8v-x56r-v595-3btj")
RTMP = f"rtmp://a.rtmp.youtube.com/live2/{KEY}"
print(f"Transmitiendo santi.mcsh.gg a YouTube...")
while True:
    cmd = ["ffmpeg","-re","-loop","1","-i","background.jpg","-f","lavfi","-i","anullsrc","-c:v","libx264","-tune","stillimage","-preset","veryfast","-b:v","2000k","-pix_fmt","yuv420p","-shortest","-c:a","aac","-f","flv",RTMP]
    subprocess.run(cmd)
    time.sleep(5)
