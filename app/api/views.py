from rest_framework import generics
from rest_framework.response import Response

from api.models import Writer
from api.serializers import WriterSerializer


class WriterList(generics.ListAPIView):

    serializer_class = WriterSerializer

    def get(self, request, pk, *args, **kwargs):
        queryset = Writer.objects.get(pk=pk)
        serializer = WriterSerializer(queryset)
        return Response(serializer.data)