# youtube_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer
from googleapiclient.discovery import build

class YouTubeAPI(APIView):
    def get_youtube_data(self, query):
        # Set your YouTube API key
        api_key = 'YOUR_YOUTUBE_API_KEY'

        # Create a service object for interacting with the API
        youtube = build('youtube', 'v3', developerKey=api_key)

        # Define parameters for the search request
        search_response = youtube.search().list(
            q=query,
            part='id,snippet',
            order='date',
            type='video',
            maxResults=10,  # You can adjust the number of results as needed
        ).execute()

        # Extract relevant information from the search response
        videos = []
        for search_result in search_response.get('items', []):
            video_id = search_result['id']['videoId']
            video_response = youtube.videos().list(
                id=video_id,
                part='snippet,contentDetails',
            ).execute()

            video_info = {
                'title': video_response['items'][0]['snippet']['title'],
                'description': video_response['items'][0]['snippet']['description'],
                'published_at': video_response['items'][0]['snippet']['publishedAt'],
                'thumbnail_url': video_response['items'][0]['snippet']['thumbnails']['default']['url'],
            }
            videos.append(video_info)

        return videos

    def get(self, request):
        # Define your YouTube search query
        youtube_query = request.query_params.get('query', 'Python Programming')
        youtube_data = self.get_youtube_data(youtube_query)

        # Process and store YouTube data in your Video model
        for video_info in youtube_data:
            Video.objects.create(
                title=video_info['title'],
                description=video_info['description'],
                published_at=video_info['published_at'],
                thumbnail_url=video_info['thumbnail_url'],
            )

        # Retrieve stored videos
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)

        return Response(serializer.data)
