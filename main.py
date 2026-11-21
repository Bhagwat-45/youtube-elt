from youtube_api.get_video_ids import get_vids
from youtube_api.video_stats import get_video_stats
from config.settings import settings

def main():
    playlistId = get_video_stats(settings.channel_playlist_id_url)
    get_vids(playlistId)


if __name__ == "__main__":
    main()
