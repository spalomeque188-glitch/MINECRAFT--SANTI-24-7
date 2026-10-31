import subprocess, os, time, threading
from http.server import BaseHTTPRequestHandler, HTTPServer

KEY = os.getenv("YOUTUBE_KEY", "0jpp-vt8v-x56r-v595-3btj")
RTMP = f"rtmp://a.rtmp.youtube.com/live2/{KEY}"
PORT = int(os.getenv("PORT", "10000"))

# Servidor web falso para que Render no lo apague (GRATIS)
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Minecraft Santi 24/7 Live - santi.mcsh.gg")

def run_web():
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    server.serve_forever()

threading.Thread(target=run_web, daemon=True).start()

FFMPEG_FILTER = "drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:text='MINECRAFT 24 HORAS':fontcolor=yellow:fontsize=80:x=(w-text_w)/2:y=150,drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:text='IP\\: santi.mcsh.gg':fontcolor=white:fontsize=70:x=(w-text_w)/2:y=350:box=1:boxcolor=black@0.8:boxborderw=15,drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:text='ENTRA YA 24/7':fontcolor=yellow:fontsize=70:x=(w-text_w)/2:y=550"

while True:
    try:
        cmd = ["ffmpeg","-re","-f","lavfi","-i","color=c=0x2e8b57:s=1280x720:r=30","-f","lavfi","-i","anullsrc","-vf",FFMPEG_FILTER,"-c:v","libx264","-preset","veryfast","-b:v","2500k","-c:a","aac","-f","flv",RTMP]
        subprocess.run(cmd)
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(5)
