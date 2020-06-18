from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username):
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return HttpResponseRedirect('/profile/{}'.format(user.id))# Redirect to a success page.
            return HttpResponseRedirect('/signup/')
        else:
            return HttpResponseRedirect("/signup/")
    form=LoginForm()
    return render(request, 'registration/login.html', {'login_form': LoginForm})

class UserDetail(DetailView):
    model = User
    template_name = "algo/profile.html"

    def get_context_data(self, **kwargs):
        context = super(UserDetail, self).get_context_data(**kwargs)
        context['object_list'] = User.objects.exclude(username=self.request.user.username)
        return context
    def post(self, request, *args, **kwargs):
        user = request.POST.getlist('user')
        if User.objects.filter(id__in=user):
            username = User.objects.filter(id__in=user)[0].username
            User.objects.filter(id__in=user).delete()
            return HttpResponseRedirect(self.request.path_info)

class UserListView(ListView):
    model = User
    template_name = "algo/listview.html"

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['object_list'] = context['object_list'].exclude(username=self.request.user.username)
        return context

    def post(self, request, *args, **kwargs):
        user = request.POST.getlist('user')
        if User.objects.filter(id__in=user):
            username = User.objects.filter(id__in=user)[0].username
            User.objects.filter(id__in=user).delete()
            return HttpResponseRedirect(self.request.path_info)

#def logout(request):
    #return render(request, 'registration/logged_out.html', {'form': form})
