from django.http import HttpResponse
from django.shortcuts import render,render_to_response

def hello(request):
    return render_to_response( 'index.html')
#	return HttpResponse("Hello world ! ")
