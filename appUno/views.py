from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")
def root(request):
    return redirect("/blogs")
def index(request):
    return HttpResponse('<h2>placeholder para luego mostrar una lista de todos los blogs</h2>')
def new(request):
    return HttpResponse('<P>placeholder para mostrar un nuevo formulario para crear un nuevo blog <p>')
def create(request):
    return redirect("/")
def show(request, number):
    return HttpResponse(f"placeholder para mostrar el blog numero: {number}")
def edit(request, number):
    return HttpResponse(f"<H1>placeholder para editar el blog numero: {number}</H1>")
def destroy(request, number):
    return redirect("/blogs")
def jres(request):
    data =[{'Titulo': 'Blogs', 'Numero_blog': '1' },
           {'Titulo':'Parrafos', 'Numero_parrafo': '3'}]
    return JsonResponse({'data': data})