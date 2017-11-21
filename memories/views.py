from django.shortcuts import render

# Create your views here.

def sign_in(request):
    return render(request, 'memories/sign_in.html')

def personal_page(request):
    return render(request, 'memories/personal_page.html')

def stories(request):
    return render(request, 'memories/stories.html')

def post_story(request):
    return render(request, 'memories/post_story.html')
