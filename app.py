import subprocess, os, time

KEY = os.getenv("YOUTUBE_KEY", "0jpp-vt8v-x56r-v595-3btj")
RTMP = f"rtmp://a.rtmp.youtube.com/live2/{KEY}"

FFMPEG_FILTER = "drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:text='MINECRAFT 24 HORAS':fontcolor=yellow:fontsize=80:x=(w-text_w)/2:y=150,drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:text='IP\\: santi.mcsh.gg':fontcolor=white:fontsize=70:x=(w-text_w)/2:y=350:box=1:boxcolor=black@0.8:boxborderw=15,drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:text='ENTRA YA 24/7':fontcolor=yellow:fontsize=70:x=(w-text_w)/2:y=550"

while True:
    cmd = ["ffmpeg","-re","-f","lavfi","-i","color=c=0x2e8b57:s=1280x720:r=30","-f","lavfi","-i","anullsrc","-vf",FFMPEG_FILTER,"-c:v","libx264","-preset","veryfast","-b:v","2500k","-c:a","aac","-f","flv",RTMP]
    subprocess.run(cmd)
    time.sleep(5)
