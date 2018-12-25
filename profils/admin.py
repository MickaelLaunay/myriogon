from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from profils.models import Profil
from profils.models import Achievement
from profils.models import UserCours
from profils.models import UserModule

class ProfilsUser(admin.StackedInline):
    model = Profil
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = (ProfilsUser,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Achievement)
admin.site.register(UserCours)
admin.site.register(UserModule)
admin.site.register(Profil)
