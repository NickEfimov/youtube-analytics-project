import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('youtubeAPIkey')
    youtube = build('youtube', 'v3', developerKey=api_key)


    def __init__(self, channel_id :str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        channel = self.get_service().channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.id = channel['items'][0]['id']
        self.title = channel['items'][0]['snippet']['title']
        self.description = channel['items'][0]['snippet']['description']
        self.url = f'https://www.youtube.com/channel/{channel["items"][0]["id"]}'
        self.subscriber_count = channel['items'][0]['statistics']['subscriberCount']
        self.video_count = channel['items'][0]['statistics']['videoCount']
        self.view_count = channel['items'][0]['statistics']['viewCount']



    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        dict_to_print = self.youtube.channels().list(id=self.id, part='snippet,statistics').execute()
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('youtubeAPIkey')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def to_json(self, channel):
        """Сохраняет значения атрибутов экземпляра Channel в файл в формате JSON"""
        with open('filename', 'w') as f:
            json.dump({
                'channel_id': self.id,
                'channel_name': self.title,
                'channel_desс': self.description,
                'link': self.url,
                'subscribers': self.subscriber_count,
                'videos': self.video_count,
                'total': self.view_count
            }, f)
