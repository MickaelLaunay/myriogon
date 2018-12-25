from django.contrib import admin
from cours.models import Cours
from cours.models import Module
from cours.models import Video
from cours.models import Qcm

admin.site.register(Cours)
admin.site.register(Module)
admin.site.register(Video)
admin.site.register(Qcm)
