from django.shortcuts import render
from .models import User
from .forms import UserForm
from django.views.decorators.csrf import csrf_protect

# Create your views here.

@csrf_protect
def sign_in(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = User.objects.create(name = form.cleaned_data['name'], email = form.cleaned_data['email'], password = form.cleaned_data['password'])
            user.register()
    return render(request, 'memories/sign_in.html')

def personal_page(request):
    return render(request, 'memories/personal_page.html')

def stories(request):
    return render(request, 'memories/stories.html')

def post_story(request):
    return render(request, 'memories/post_story.html')

def sign_up(request):
    return render(request, 'memories/sign_up.html')
