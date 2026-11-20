import requests
import json
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")

api_key = os.getenv("AUTH_KEY")
channel_name = "MrBeast"

url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={channel_name}&key={api_key}"

def get_video_stats(url: str):

    try:
        response = requests.get(
            url
        )
        response.raise_for_status()
        data = response.json()
        channel_items = data["items"][0]
        channel_playlistId = channel_items["contentDetails"]["relatedPlaylists"]

        return channel_playlistId
    except requests.exceptions.RequestException as e:
        raise e

if __name__ == "__main__":
    print(get_video_stats(url=url))