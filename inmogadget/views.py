from django.shortcuts import redirect

def index(request):
    response = redirect('calculator:index')
    return response

