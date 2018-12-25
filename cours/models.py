from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import User

class Cours(models.Model):
	titre = models.CharField(max_length=200)
	slug = models.SlugField(max_length=100, null=True)
	langue = models.CharField(max_length=10, default='fr')
	icone = models.ImageField(upload_to='img', default='img/default.jpg')
	resume = models.TextField(null=True)
	niveau = models.IntegerField(default=0)
	prerequis = models.ManyToManyField("self", symmetrical=False)

	def pmodule(self):
		module = Module.objects.get(cours=self,niveau=0,rang=0)
		return module

	class Meta:
	        verbose_name = "Cours"
	        ordering = ['id']

	def __str__(self):
	        return self.titre


class Module(models.Model):
	cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
	titre = models.CharField(max_length=200)
	slug = models.SlugField(max_length=100, null=True)
	icone_0 = models.ImageField(upload_to='img', default='img/default.jpg')
	icone_1 = models.ImageField(upload_to='img', default='img/default.jpg')
	icone_2 = models.ImageField(upload_to='img', default='img/default.jpg')
	niveau = models.IntegerField(default=0)
	rang = models.IntegerField(default=0)

	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
	object_id = models.PositiveIntegerField(null=True)
	content_object = GenericForeignKey()

	class Meta:
	        verbose_name = "Les modules"
	        ordering = ['niveau', 'rang']

	def __str__(self):
	        return self.titre



class Video(models.Model):
	module = GenericRelation(Module)
	video = models.CharField(max_length=200, null=True)

class Vraifaux(models.Model):
	module = GenericRelation(Module)
	questions = models.CharField(max_length=200, null=True)

class Qcm(models.Model):
	module = GenericRelation(Module)
	questions = models.CharField(max_length=200, null=True)
