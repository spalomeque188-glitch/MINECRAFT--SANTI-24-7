FROM python:3.10
RUN apt-get update && apt-get install -y ffmpeg
WORKDIR /app
COPY . .
CMD ["python", "app.py"]
