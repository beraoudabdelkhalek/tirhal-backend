from rest_framework import serializers
from .models import Utilizer,Region,Place,Image,Favorite,Comment,Rating,Transport,Event

class UtilizerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Utilizer
        fields= "__all__"

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Region
        fields="__all__"
        depth=1
class RegionSerializer2(serializers.ModelSerializer):
    class Meta:
        model=Region
        fields="__all__"
class MiniRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Region
        fields=('id','code')
class MiniPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Place
        fields=('id','name','latitude','longitude')

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Place
        fields='__all__'
        depth=1

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Image
        fields='__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Favorite
        fields='__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=('id','idUtilizer','comment','pubdate')
        depth=1
class CommentSerializerOnadd(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=("id","idUtilizer","idPlace","comment")

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rating
        fields=('id','idUtilizer','value')
class RatingSerializerOnadd(serializers.ModelSerializer):
    class Meta:
        model=Rating
        fields='__all__'

class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transport
        fields='__all__'