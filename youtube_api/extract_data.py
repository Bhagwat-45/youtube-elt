from _helper.batch_size import _batch_list
import requests
import json
from config.settings import settings

def extract_data(video_ids):
    extracted_data = []

    try:
        for batch in _batch_list(video_ids, settings.max_results):
            video_id_str = (",").join(batch)
            url = f"https://youtube.googleapis.com/youtube/v3/videos?part=contentDetails&part=snippet&part=statistics&id={video_id_str}&key={settings.api_key}"
            response = requests.get(url)
            response.raise_for_status()

            data = response.json()

            for item in data.get("items", []):
                video_id = item['id']
                snippet = item['snippet']
                contentDetails = item['contentDetails']
                statistics = item['statistics']

                video_data = {
                    "videoId": video_id,
                    "title": snippet['title'],
                    "publishedAt": snippet['publishedAt'] ,
                    "duration" : contentDetails['duration'],
                    "viewCount" : statistics.get("viewCount", None),
                    "likeCount" : statistics.get('likeCount', None),
                    "commentCount": statistics.get('commentCount', None)
                }

                extracted_data.append(video_data)

        return extracted_data
    
    except requests.exceptions.RequestException as e:
        raise e