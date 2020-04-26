from rest_framework import serializers
from common import models



class UserSerializer(serializers.ModelSerializer):
	username= serializers.ReadOnlyField()
	email=serializers.ReadOnlyField()
	class Meta:
		model = models.User
		fields = ["username", "email"]

class PostSerializer(serializers.ModelSerializer):
    updated_at = serializers.ReadOnlyField()
    is_notice = serializers.IntegerField(write_only = True)
    is_deleted = serializers.IntegerField(write_only = True) 
    club = serializers.ReadOnlyField(source='club.club_name')# 이게 맞는건지 확인
    class Meta:
        model = models.Posts
        fields = ["post_title_img_url","updated_at","post_title","post_content","is_deleted","is_notice","club","post_id"]

class addPost(serializers.ModelSerializer):
	class Meta:
		model = models.Posts
		fields = '__all__'


class PostDetailSerializer(serializers.ModelSerializer):
	#post_title_img_url = serializers.ReadOnlyField()
	created_at = serializers.ReadOnlyField()
	updated_at = serializers.ReadOnlyField()
	user = serializers.ReadOnlyField(source='user.username')
	is_notice = serializers.IntegerField(write_only = True)
	is_deleted = serializers.IntegerField(write_only = True)
	
	# user = serializers.CharField(source='user.username')
	class Meta:
		model = models.Posts
		fields = '__all__'


