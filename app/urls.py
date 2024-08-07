from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListView,GenreRetrieveUpdateDestoyView
from actors.views import ActorCreateListView, ActorRetrieveUpdateDestroyView
from movies.views import MovieCreateListView, MovieRetriveUpdateDestroyView
from reviews.views import ReviewCreateListView, ReviewRetrieverUpdateDestroyView
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('genres/', GenreCreateListView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestoyView.as_view(), name='genre-detail-view'),
    
    path('actors/', ActorCreateListView.as_view(), name='actor-create-list' ),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail-view'),
    
    path('movies/', MovieCreateListView.as_view(), name='movie-create-view'),
    path('movies/<int:pk>', MovieRetriveUpdateDestroyView.as_view(), name='movie-detail-view'),

    path('reviews/', ReviewCreateListView.as_view(), name='review-create-list'),
    path('reviews/<int:pk>/', ReviewRetrieverUpdateDestroyView.as_view(), name='review-detail-view'),
]

