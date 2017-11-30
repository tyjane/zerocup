from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Memory
from .forms import UserForm, MemoryForm
from django.views.decorators.csrf import csrf_protect
from django.utils import timezone


@csrf_protect
def sign_in_and_personal_page(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if not form.is_valid():
            inputedData = {}
            inputedData["name"] = request.POST.get("name", "")
            inputedData["password"] = request.POST.get("password", "")
            return render(request, 'memories/sign_in.html', {'inputedData': inputed})
        else:
            user = authenticate(\
                username=form.cleaned_data["name"],\
                password=form.cleaned_data["password"])
            isUserExist = False
            if user is not None:
                if user.is_active:
                    login(request, user)
                    isUserExist = True
            if isUserExist:
                memories = Memory.objects.filter(author = request.user.username)
                return render(request, 'memories/personal_page.html', {"memories": memories})
            else:
                error = {"msg": "The name or password is incorrect."}
                return render(request, 'memories/sign_in.html', error)
    else:
        backToLogin = True
        if request.user.is_authenticated():
            if request.GET.get("_logout", "") == "log out":
                logout(request)
            else:
                backToLogin = False
        if backToLogin:
            return render(request, 'memories/sign_in.html')
        else:
            memories = Memory.objects.filter(author = request.user.username)
            return render(request, 'memories/personal_page.html', {"memories": memories})

def stories(request):
    m = Memory.objects.all()
    return render(request, 'memories/stories.html', {'memories': m})

def user_stories(request):
    m = Memory.objects.filter(author = request.user.username)
    return render(request, 'memories/stories.html', {'memories': m})

def post_story(request):
    if request.method == 'POST':
        form = MemoryForm(request.POST)
        if form.is_valid():
            m = Memory.objects.create(\
                title = form.cleaned_data['title'],\
                content = form.cleaned_data['content'],\
                author = form.cleaned_data['author'])
            m.post()
    o = {}
    o["author"] = request.user.username
    return render(request, 'memories/post_story.html', o)

def sign_up(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(\
                username = form.cleaned_data['name'],\
                email = form.cleaned_data['email'],\
                password = form.cleaned_data['password'])
            user.save()
    return render(request, 'memories/sign_up.html')

def log_out(request):
    return render(request, 'memories/sign_in.html')
