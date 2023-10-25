from datetime import timedelta
import os
from googleapiclient.discovery import build
import isodate
import datetime


class PlayList:
    def __init__(self, playlist_id):
        self.id = playlist_id
        playlist_info = self.get_service().playlists().list(id=self.id,
                                                            part='snippet',
                                                            ).execute()
        self.__info_videos = self.get_service().playlistItems().list(playlistId=self.id,
                                                                     part='contentDetails, snippet',
                                                                     maxResults=50).execute()
        self.title = playlist_info['items'][0]['snippet']['title']
        self.url = 'https://www.youtube.com/playlist?list=' + self.id

    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('youtubeAPIkey')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    @property
    def total_duration(self):
        result = timedelta(seconds=0)
        for video in self.tracks:
            result += isodate.parse_duration()
        return result

    def show_best_video(self):
        if not self.tracks:
            return None
        best_video = max(self.tracks, key=lambda x: x['likes'])
        return best_video['link']


#pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
#print(pl.total_duration)
