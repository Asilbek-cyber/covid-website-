from django.shortcuts import render

# home_view,about_view,action_view,contact_view,doctores_view,news_view

def home_view(request):
    return render(request,"index.html")

def about_view(request):
    return render(request,"about.html")

def action_view(request):
    return render(request,"action.html")

def contact_view(request):
    return render(request,"contact.html")

def doctores_view(request):
    return render(request,"doctores.html")

def news_view(request):
    return render(request,"news.html")