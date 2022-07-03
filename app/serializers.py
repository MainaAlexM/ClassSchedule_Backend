from rest_framework import serializers
from .models import User, Profile, Comment, Module, Session, Announcement


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ModuleSerializer(serializers.ModelSerializer):
    technical_mentor = UserSerializer(read_only=True)

    class Meta:
        model = Module
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    modules = ModuleSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'



class SessionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True) 
    module = ModuleSerializer(read_only =True )
    class Meta:
        model=Session
        fields='__all__'



class AnnouncementSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True) 
    class Meta:
        model=Announcement
        fields='__all__'



class CommentSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only = True) 
    class Meta:
        model=Comment
        fields=('id','likes','date_created','comment','session')
        read_only_fields=['user']
        
    # create_comment=Comment.objects.create()