from rest_framework import status
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response
from utils import Change_data

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


@api_view(['GET'])
def book_content(request, book):
    """
    List all snippets, or create a new snippet.
    """
    
    label = request.REQUEST.get('watermark')
    template = "https://s3.eu-central-1.amazonaws.com/saxo-static/ebooks/{0}.epub"
    book_path = template.format(book)
    if request.method == 'GET':
        content = Change_data(book_path, label)
        if content is None:
        	return Response(status=status.HTTP_400_BAD_REQUEST)
        # Grab ZIP file from in-memory, make response with correct MIME-type
    	resp = HttpResponse(content['string'].getvalue())
    	# ..and correct content-disposition
    	resp['Content-Disposition'] = 'attachment; filename=%s' % content["zip_filename"]
        return resp
