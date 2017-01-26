from rest_framework import serializers
from newrelic.models import api_key, rest_url
from django.contrib.auth.models import User
import datetime

class api_keySerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	sitename = serializers.CharField(required=True, allow_blank=False, max_length=100)
	key = serializers.CharField(required=True, allow_blank=False, max_length=100)

	def create(self, validated_data):
		return api_key.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.sitename = validated_data.get('sitename', instance.sitename)
		instance.key = validated_data.get('key', instance.key)
		instance.created = datetime.datetime.now()
		instance.save()
		return instance
		
class rest_urlSerializer(serializers.Serializer):
        id = serializers.IntegerField(read_only=True)
        mode = serializers.CharField(required=True, allow_blank=False, max_length=100)
        action = serializers.CharField(required=True, allow_blank=False, max_length=100)
	url = serializers.CharField(required=True, allow_blank=False, max_length=200)

        def create(self, validated_data):
                return api_key.objects.create(**validated_data)

        def update(self, instance, validated_data):
                instance.mode = validated_data.get('mode'. instance.mode)
                instance.action = validated_data.get('action'. instance.action)
                instance.url = validated_data.get('url'. instance.url)
                instance.save()
                return instance

class UserSerializer(serializers.ModelSerializer):
	api_keys = serializers.PrimaryKeyRelatedField(many=True, queryset=api_key.objects.all())
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = User
		fields = ('id', 'username', 'api_keys', 'owner',)

#class api_keySerializer(serializers.HyperlinkedModelSerializer):
#    owner = serializers.ReadOnlyField(source='owner.username')
#    highlight = serializers.HyperlinkedIdentityField(view_name='api_key-highlight', format='html')

#    class Meta:
#        model = api_key
#        fields = ('id', 'sitename', 'owner', 'highlight',)


#class UserSerializer(serializers.HyperlinkedModelSerializer):
#    api_keys = serializers.HyperlinkedRelatedField(many=True, view_name='api_key-detail', read_only=True)

#    class Meta:
#        model = User
#        fields = ('url', 'id', 'username', 'api_keys')
		
