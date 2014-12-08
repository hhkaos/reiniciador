from django.contrib.auth.models import User, Group
from ..models import Member
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.Field(source='owner')

    class Meta:
        model = Member
        fields = ('user', 'photo', 'bio')
