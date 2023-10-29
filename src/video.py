import os
from googleapiclient.discovery import build


class Video:

    def __init__(self, video_id):
        self.video_id = video_id
        try:
            video_response = self.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                   id=video_id
                                                   ).execute()
            self.title = video_response['items'][0]['snippet']['title']
            self.view = video_response['items'][0]['statistics']['viewCount']
            self.like = video_response['items'][0]['statistics']['likeCount']
            self.link = f'https://www.youtube.com/watch?v={video_id}'
        except:
            self.title = None
            self.url = None
            self.view_count = None
            self.like_count = None

    def __str__(self):
        return self.title

    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('youtubeAPIkey')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube


class PLVideo(Video):

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
