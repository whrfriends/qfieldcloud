from django.shortcuts import render

def index(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = "Guest"
    
    context = {'username': username}
    return render(request, 'myweb/index.html', context)