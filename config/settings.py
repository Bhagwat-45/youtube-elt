import os
from dotenv import load_dotenv

load_dotenv()

class Settings():
    api_key: str = os.getenv("AUTH_KEY")
    channel_name: str = "MrBeast"
    channel_playlist_id_url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={channel_name}&key={api_key}"
    max_results: int = 50


settings = Settings()