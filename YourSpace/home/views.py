from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import DetailView, CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth import logout as django_logout


from .models import *
from .forms import *

# Create your views here.
def home(request):
	return redirect('startpage', permanent = True)

def start(request):
	context = {
		'title': "Let's start!", 
	} 
	return render(request, 'home/homepages/start.html', context = context)

def guides(request): 
	context = {
		'title': "Guides & Tutorials", 
	} 
	return render(request, 'home/homepages/guides.html', context = context)

class signin(LoginView):
	form_class = signinform
	template_name = 'home/homepages/signin.html'
	extra_context = {'title': "Sign In"}

	def get_success_url(self):
		return reverse_lazy('userredirect')

def userredirect(request):
	return redirect('profile', slug = request.user.username)

class signup(CreateView):
	form_class = signupform
	template_name = 'home/homepages/signup.html'
	success_url = reverse_lazy('signin')
	extra_context = {'title': "Sign Up"}

	def form_valid(self, form):
		user = form.save()
		user.slug = user.username
		user.profile_pic = "images/profile/defava.png"
		user.cover_pic = "images/profile/defcover.png"
		user.descr = "Description"
		user = form.save()
		login(self.request, user)
		return redirect('profile', slug = user.username)



def Profile(request, slug):
	p_user = get_object_or_404(User, slug=slug)

	if request.method == 'POST':
		form = AddText(request.POST)
		if form.is_valid():
			try:
				form.name="name"
				f = form.save(commit=False)
				f.name = "name"
				f.save()
				f.name = str(request.user.username)+".text"+str(f.pk)
				f.save()

				c = ProfileContent(profile=request.user, name=f.name, conttype=ContentType.objects.get(pk=1))
				c.save()
				form = AddText()

			except:
				form.add_error(None, 'Ошибка добавления')
			return redirect('userredirect')


		form1 = AddImg(request.POST, request.FILES)
		if form1.is_valid():
			try:
				form1.name="name"
				f1 = form1.save(commit=False)
				f1.name = "name"
				f1.user = request.user
				f1.save()
				f1.name = str(request.user.username)+".img"+str(f1.pk)
				f1.save()

				c1 = ProfileContent(profile=request.user, name=f1.name, conttype=ContentType.objects.get(pk=2))
				c1.save()
				form1 = AddImg()

			except:
				form1.add_error(None, 'Ошибка добавления')
			return redirect('userredirect')

	else: 
		form = AddText()
		form1 = AddImg()

	context = {
		'title': p_user,
		'p_user': p_user,
		'form': form,
		'form1': form1,
	}

	return render(request, 'home/profilepages/mainprofile.html', context=context)

def profileedit(request):
	if request.method == 'POST':
		formedit = ProfileEditForm(request.POST, request.FILES)
		if formedit.is_valid():
			try:
				print('мяу')
				#request.user
				formedit = ProfileEditForm()
			except:
				formedit.add_error(None, 'Ошибка редактирования')
			return redirect('profuleedit')
	else:
		formedit = ProfileEditForm()	

	context = {
		'title': "Редактирование профиля",
		'form': formedit,
	}

	return render(request, 'home/profilepages/profileedit.html', context = context)		

def delete(request, o_id):
	obj = ProfileContent.objects.get(pk=o_id)
	objname = obj.name
	if obj.conttype == ContentType.objects.get(pk=1):
		tobj = TextContent.objects.get(name=objname)
		obj.delete()
		tobj.delete()
	elif obj.conttype == ContentType.objects.get(pk=2):
		iobj = ImgContent.objects.get(name=objname)
		obj.delete()
		iobj.delete()
	return redirect('profile', slug = request.user.username)


class info_focus(DetailView):
	model = Info
	template_name = 'home/homepages/infofocus.html'
	context_object_name = "post"

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = context['post']
		return context

	def get_queryset(self):
		return Info.objects.filter(is_pub=True)

def logout(request):
    django_logout(request)
    return redirect('home')


def pageNotFound(request, exception):
	return HttpResponseNotFound("<h1>Страница не найдена</h1>")