from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from cours.models import Cours
from cours.models import Module

# Create your models here.

class Profil(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")
	info = models.CharField(max_length=100, null=True)

	cours = models.ManyToManyField(
		Cours,
		through='UserCours',
		through_fields=('profil', 'cours')
	)

	modules = models.ManyToManyField(
		Module,
		through='UserModule',
		through_fields=('profil', 'module')
	)
	
	def startcours(self, cours):
		uc, created = UserCours.objects.get_or_create(profil=self, cours=cours)
		if created:
			self.unlockmodule(cours.pmodule())
			uc.solved=1
			uc.niveau=0
			uc.date_start=datetime.now()
			uc.save()
		return uc

	def favunfav(self, coursid):
		cours = Cours.objects.get(id=coursid)
		uc = UserCours.objects.get_or_create(profil=self, cours=cours)[0]
		uc.fav = 1-uc.fav
		uc.save()
		return uc.fav
	
	def unlockmodule(self, module):
		um = UserModule.objects.get_or_create(profil=self, module=module)[0]
		um.solved = 1
		um.save()

	def solvemodule(self, module):
		um = UserModule.objects.get_or_create(profil=self, module=module)[0]
		if um.solved <2:
			um.solved = 2
			um.save()
			self.actuniveau(module.cours)

	def icone(self, module):
		um = UserModule.objects.get_or_create(profil=self, module=module)[0]
		if um.solved==1:
			return module.icone_1.url
		if um.solved==2:
			return module.icone_2.url
		else:
			return module.icone_0.url
	
	def actuniveau(self, cours):
		uc = UserCours.objects.get_or_create(profil=self, cours=cours)[0]
		niv=uc.niveau
		modules = Module.objects.filter(cours=cours, niveau=niv)
		valideniv=True
		for mod in modules:
			um = UserModule.objects.get_or_create(profil=self, module=mod)[0]
			if um.solved<2:
				valideniv=False
		if valideniv:
			uc.niveau=niv+1
			moduless = Module.objects.filter(cours=cours, niveau=niv+1)
			if moduless.exists():
				for mod in moduless:
					self.unlockmodule(mod)
			else:
				uc.solved=2
		uc.save()

	def __str__(self):
	        return "Profil de {0}".format(self.user.username)

class Achievement(models.Model):
	nom = models.CharField(max_length=100)
	description = models.CharField(max_length=240)
	members = models.ManyToManyField(
		Profil,
		through='UserAchiev',
		through_fields=('achievement', 'profil'),
	)

	def __str__(self):
	        return "Achievement : ".format(self.nom)

class UserAchiev(models.Model):
	achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
	profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
	date = models.DateTimeField()

class UserModule(models.Model):
	profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
	module = models.ForeignKey(Module, related_name="usermodule", on_delete=models.CASCADE)
	solved = models.IntegerField(default=0)  # 0: module locked 1: module unlocked 2: module solved
	date_start = models.DateTimeField(null=True)
	date_end = models.DateTimeField(null=True)

class UserCours(models.Model):
	profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
	cours = models.ForeignKey(Cours, related_name="usercours", on_delete=models.CASCADE)
	fav = models.IntegerField(default=0) # 1: fav
	solved = models.IntegerField(default=0) # 1: cours commencé 2: cours validé
	niveau = models.IntegerField(default=0)
	date_start = models.DateTimeField(null=True)
	date_end = models.DateTimeField(null=True)

class Messages(models.Model):
	profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
	sujet = models.CharField(max_length=60, null=True)
	message = models.CharField(max_length=500, null=True)
	image = models.ImageField(null=True, blank=True, upload_to="img_messages/")
