from  rest_framework import serializers

from django.contrib.auth.models import User

from news.models import News



class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('first_name', 'last_name')


class NewsSerializer(serializers.ModelSerializer):
	user = serializers.SerializerMethodField()

	class Meta:
		model = News
		exclude = ()

	def get_user(self, obj):
		return UserSerializer(obj.user).data