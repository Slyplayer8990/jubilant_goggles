import mitmproxy
from mitmproxy import http
import sqlite3
import os
with open(output_file, 'w') as f:
        f.write("#EXTM3U\n")
        f.close()

# Tabloyu oluştur

def request(flow: http.HTTPFlow) -> None:
    conn = sqlite3.connect('stream_channels.db')
    cursor = conn.cursor()
    url = flow.request.url
    with open("log", "a") as file:
        file.write(url)

    # Eğer Content-Type HLS ise
    if 'master.m3u8' in url:
        with open(output_file, 'a') as f:
            f.write("#EXTINF:-1, {}\n".format(url))
            f.write("{}\n".format(url))
