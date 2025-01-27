from django.shortcuts import render



def index(request):
    return render(request, 'engine/index.html')

def contact(request):
    return render(request, 'engine/contact.html')