import requests
from config.settings import settings

def get_vids(playlistId: str):
    video_ids = []
    pageToken = None

    base_url = f"https://youtube.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults={settings.max_results}&playlistId={playlistId}&key={settings.api_key}"

    try:
        while True:
            url = base_url

            if pageToken:
                url += f"&pageToken={pageToken}"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            for item in data.get('items', []):
                video_id = item['contentDetails']['videoId']
                video_ids.append(video_id)

            pageToken = data.get('nextPageToken')
            if not pageToken:
                break

        return video_ids
    except requests.exceptions.RequestException as e:
        raise e

