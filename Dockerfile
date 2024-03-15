FROM python:3.11

WORKDIR /app

RUN apt-get -y update
RUN apt-get install --no-install-recommends -y ffmpeg

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "src/main.py"]
