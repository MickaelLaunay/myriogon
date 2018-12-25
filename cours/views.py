from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils import translation
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from cours.models import Cours
from cours.models import Module
from cours.models import Video, Qcm
from profils.models import Profil
from profils.models import UserCours
from profils.views import connexion

# Create your views here.

def index(request):
	form = connexion(request)
	if request.user.is_authenticated:
		profil = Profil.objects.get(user=request.user)
		encours = Cours.objects.filter(profil=profil, usercours__fav=1, langue=translation.get_language())
		conseils = Cours.objects.filter(niveau=0, langue=translation.get_language())
		return render(request, 'accueil.html', {'encours': encours, 'conseils': conseils})
	else:
		cours = Cours.objects.filter(niveau=0, langue=translation.get_language())
		return render(request, 'index.html', {'cours': cours, 'form': form})

def vue_tous(request):
	form = connexion(request)
	cours = Cours.objects.filter(langue=translation.get_language())
	return render(request, 'tous.html', {'cours': cours, 'form': form })

def vue_cours(request, id_cours, slug):
	form = connexion(request)
	cours = Cours.objects.get(id=id_cours, slug=slug)
	modules = Module.objects.filter(cours__id=id_cours)
	if request.user.is_authenticated:
		profil = Profil.objects.get(user=request.user)
		uc = profil.startcours(cours)
		isfav = ['/static/img/fav'+str(uc.fav)+".png",'/static/img/fav'+str(1-uc.fav)+".png"]
	else:
		isfav = []
	nbniv = modules[len(modules)-1].niveau
	modtri = []
	for x in range(nbniv+1):
		rang = modules.filter(cours__id=id_cours, niveau=x)
		rangico = []
		for mod in rang:
			if request.user.is_authenticated:
				rangico.append([mod,profil.icone(mod)])
			else:
				rangico.append([mod,mod.icone_0.url])
		modtri.append(rangico)
	prerequis = cours.prerequis.all()
	return render(request, 'menu_cours.html', {'cours': cours, "modules": modtri, "nbniv": nbniv, "form": form, "isfav": isfav, "prerequis": prerequis })


def favcours(request):
	coursid = request.GET.get('id', None)
	profil = Profil.objects.get(user=request.user)
	result = profil.favunfav(coursid)
	data = {
		'fav': result,
	}
	return JsonResponse(data)

def vue_video(request, id_module, slug):
	module = Module.objects.get(id=id_module, slug=slug)
	video = Video.objects.get(module__id=module.object_id)
	if request.user.is_authenticated:
		profil = Profil.objects.get(user=request.user)
		profil.solvemodule(module)
	return render(request, 'video.html', {'module': module, "video": video })


def vue_vraifaux(request, id_module, slug):
	module = Module.objects.get(id=id_module, slug=slug)
	video = Video.objects.get(module__id=module.object_id)
	if request.user.is_authenticated:
		profil = Profil.objects.get(user=request.user)
	return render(request, 'video.html', {'module': module, "video": video })

def vue_qcm(request, id_module, slug):
	module = Module.objects.get(id=id_module, slug=slug)
	qcm = Qcm.objects.get(id=module.object_id)
	urlqcm = "js/qcm/" + qcm.questions + ".js"
	return render(request, 'qcm.html', {'module': module, "qcm": urlqcm })
