import subprocess, os, time, threading
from http.server import BaseHTTPRequestHandler, HTTPServer

KEY = os.getenv("YOUTUBE_KEY", "0jpp-vt8x-v56r-v595-3btj")
RTMP = f"rtmp://a.rtmp.youtube.com/live2/{KEY}"
PORT = int(os.getenv("PORT", "10000"))

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Minecraft Santi 24/7 Live - santi.mcsh.gg")

def run_web():
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    server.serve_forever()

threading.Thread(target=run_web, daemon=True).start()

FFMPEG_FILTER = "drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:text='MINECRAFT SANTI 24/7 - santi.mcsh.gg':fontcolor=white:fontsize=48:x=(w-text_w)/2:y=(h-text_h)/2"

while True:
    try:
        cmd = [
            "ffmpeg", "-re",
            "-f", "lavfi", "-i", "color=c=0x2e8b57:s=1280x720:r=30",
            "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
            "-vf", FFMPEG_FILTER,
            "-c:v", "libx264", "-preset", "veryfast",
            "-b:v", "2500k", "-maxrate", "2500k", "-bufsize", "5000k",
            "-pix_fmt", "yuv420p", "-g", "60",
            "-c:a", "aac", "-b:a", "128k", "-ar", "44100",
            "-f", "flv", RTMP
        ]
        subprocess.run(cmd)
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(5)
