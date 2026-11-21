import requests
from config.settings import settings

def get_video_stats(url: str):

    try:
        response = requests.get(
            url=settings.channel_playlist_id_url
        )
        response.raise_for_status()
        data = response.json()
        channel_items = data["items"][0]
        channel_playlistId = channel_items["contentDetails"]["relatedPlaylists"]['uploads']

        return channel_playlistId
    except requests.exceptions.RequestException as e:
        raise e


if __name__ == "__main__":
    print(get_video_stats(url=settings.channel_playlist_id_url))