import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('youtubeAPIkey')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id, title=None, desc=None, url=None, subscribers=None, videos=None, video_count=None) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.id = channel_id
        self.title = title
        self.desc = desc
        self.url = url
        self.subscribers = subscribers
        self.videos = videos
        self.video_count = video_count

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        dict_to_print = self.youtube.channels().list(id=self.id, part='snippet,statistics').execute()
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('youtubeAPIkey')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def to_json(self, argument):
        """Сохраняет значения атрибутов экземпляра Channel в файл в формате JSON"""
        with open('filename', 'w') as f:
            json.dump({
                'channel_id': self.id,
                'channel_name': self.title,
                'channel_desk': self.desc,
                'link': self.url,
                'subscribers': self.subscribers,
                'videos': self.videos,
                'total': self.video_count
            }, f)
