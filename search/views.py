from django.shortcuts import render

# Create your views here.
def index(request):
    #return HttpResponse("Hello, world. You're at the Search index.")    
    return render(request, 'index.html',context=None)
