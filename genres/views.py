from rest_framework import generics
from genres.serializers import GenreSerializer
from genres.models import Genre

class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    

class GenreRetrieveUpdateDestoyView(generics.RetrieveUpdateDestroyAPIView):   
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
