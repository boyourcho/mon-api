from rest_framework import generics, renderers
from rest_framework.decorators import permission_classes, api_view
from rest_framework import permissions
from rest_framework.reverse import reverse
from rest_framework.response import Response
from newrelic.models import api_key, rest_url
from newrelic.serializers import api_keySerializer, rest_urlSerializer, UserSerializer
from django.contrib.auth.models import User
from newrelic.permissions import IsOwnerOrReadOnly

class api_key_list(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	queryset = api_key.objects.all()
	serializer_class = api_keySerializer

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class api_key_detail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
	queryset = api_key.objects.all()
	serializer_class = api_keySerializer

class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'newrelic': reverse('newrelic-list', request=request, format=format)
    })#@permission_classes((permissions.AllowAiny,))

#class newrelicHighlight(generics.GenericAPIView):
#    queryset = api_key.objects.all()
#    renderer_classes = (renderers.StaticHTMLRenderer,)

#    def get(self, request, *args, **kwargs):
#        api_key = self.get_object()
#        return Response(snippet.highlighted)
