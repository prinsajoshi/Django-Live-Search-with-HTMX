from django.shortcuts import render
from .models import Movie

# Create your views here.
def index(request):
    return render(request,'index.html',{})

def list(request):
    keyword=request.POST.get("keyword")
    movies=Movie.objects.filter(title__icontains=keyword)
    return render(request,'list.html',{'movies': movies})
    
