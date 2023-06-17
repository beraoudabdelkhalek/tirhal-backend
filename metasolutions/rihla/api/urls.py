from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/',views.register, name='to register user'),
    path('login/',views.login, name='to login user'),
    path('addregion/',views.addregion, name='to add region and assign it to an admin'),
    path('placeinregion/<int:id>',views.getAllPlaceInRegion,name=''),
    path('place/<int:id>',views.getPlace,name=''),
    path('favorite/',views.addfavourite,name='to add a place to the favorites'),
    path('myfavorite/<int:id>',views.getfavorite,name='to get favorites of a specific user'),
    path('comments/<int:id>',views.getcomments,name="get all comments for a place"),
    path('totalrating/<int:id>',views.gettotalrating,name="get the total rating of a place"),
    path('search/<int:id>',views.SearchPlaces,name='search places in a region by cat,theme, name'),
    path('addcomment/',views.addcomment,name=''),
    path('addrating/',views.addrating,name=''),
    path('regions/',views.getregions,name='to get all regions'),
    path('region/<int:code>',views.getregion,name='to get a region by id'),
    path('deletecomment/<int:id>',views.deletecomment,name='delete a comment'),
    path('deletefavorite/<int:id>',views.deletefavorite,name='delete favorite'),
    path('addplace/',views.addplace,name='add a place'),
    path('updateregion/<int:id>',views.updateregion,name='update region'),
    path("allplaces/",views.getallplaces,name="get all places"),
    path("deleteregion/<int:code>",views.deleteregion,name="delete a region")

]