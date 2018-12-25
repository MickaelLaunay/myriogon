from django.shortcuts import render, redirect
from django.utils import translation
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from profils.forms import ConnexionForm
from django.contrib.auth import authenticate, login, logout
from cours.models import Cours
from profils.models import Profil

# Create your views here.

def inscription(request):
	form = connexion(request)
	form_ins = UserCreationForm()
	return render(request, 'inscription.html', locals())

def connexion(request):
	error = False
	if request.method == "POST":
		form = ConnexionForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
			if user:  # Si l'objet renvoyé n'est pas None
				login(request, user)  # nous connectons l'utilisateur
			else: # sinon une erreur sera affichée
				error = True
		retour = error
	else:
	        retour = ConnexionForm()
	return retour

def creationuser(request):
	if request.method == "POST":
		form_ins = UserCreationForm(request.POST)
		if form_ins.is_valid():
			user = form_ins.save()
			login(request, user)
			profil = Profil(user=user)
			profil.save()
			return redirect('/')
	else:
		return inscription(request)
		

def profil(request):
	return render(request, 'profil.html')

def deconnexion(request):
	logout(request)
	return redirect('/')
