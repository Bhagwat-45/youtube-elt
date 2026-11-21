from youtube_api.get_video_ids import get_vids
from youtube_api.video_stats import get_video_stats
from youtube_api.extract_data import extract_data
from _helper.save_to_json import save_to_json
from config.settings import settings

def main():
    save_to_json(extract_data(get_vids(get_video_stats(settings.channel_playlist_id_url))))

if __name__ == "__main__":
    main()
