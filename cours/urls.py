from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('tous', views.vue_tous),
	path('menu/<int:id_cours>-<slug:slug>', views.vue_cours),
	path('video/<int:id_module>-<slug:slug>', views.vue_video),
	path('vraifaux/<int:id_module>-<slug:slug>', views.vue_vraifaux),
	path('qcm/<int:id_module>-<slug:slug>', views.vue_qcm),
	path('ajax/favcours', views.favcours),
]
