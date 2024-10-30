from .models import User
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import Q
from movierecommendation.models import Movie
from musicrecommendation.models import Music
from magazinerecommendation.models import Magazine
from user.serializers import UserSerializer
from movierecommendation.seriailzers import MovieSerializer
from musicrecommendation.serializers import MusicSerializer
from magazinerecommendation.serializers import MagazineSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny




# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[AllowAny]
    
    def create(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
  


class RecommendationViewSet(viewsets.ViewSet):
    'A single viewset for recommending friends, music, movies, and magazines'
    permission_classes=[IsAuthenticated]
    def list(self,request):
        user=request.user  #It assumes that the user is authenticated
        
        #Recommending friends
        friends=User.objects.filter(~Q(id=user.id))[:5]  #Excluding self and limiting to 5
        friends_data=UserSerializer(friends,many=True).data
        
        
        #recommending movies based on user preferences
        movies=Movie.objects.filter(genre__in=user.favorite_genres.all()[:5])
        movies_data=MovieSerializer(movies,many=True).data
        
        
        #Recommending Music based on user preferences
        music=Music.objects.filter(genre__in=user.favorite_music_genres.all()) [:5]
        music_data=MusicSerializer(music,many=True).data
        
        #Recommending Magazines based on user prefernces
        magazines=Magazine.objects.filter(category__in=user.favorite_magazine_categories.all())[:5]
        magazines_data=MagazineSerializer(magazines,many=True).data
        
        #Combining all the recommendations inside a single response
        recommendations={
            "friends":friends_data,
            "movies":movies_data,
            "music":music_data,
            "magazines":magazines_data
        }
        
        return Response(recommendations)
