from django.urls import path

from . import views

urlpatterns = [
	path('', views.profil, name='profil'),
	path('profil', views.profil, name='profil'),
	path('inscription', views.inscription, name='inscription'),
	path('creationuser', views.creationuser, name='creationuser'),
	path('deconnexion', views.deconnexion, name='deconnexion'),
]
