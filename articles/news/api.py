
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import renderers
from rest_framework import status

from news.models import News
from news.serializers import NewsSerializer

class HomeViewSet(APIView):

	def get(self, request):
		start = int(request.GET.get('start', 0))
		count = int(request.GET.get('count', 10))

		all_news = News.objects.all()
		all_news = all_news[start: start+count]
		serializer = NewsSerializer(all_news, many=True)
		return Response(serializer.data)