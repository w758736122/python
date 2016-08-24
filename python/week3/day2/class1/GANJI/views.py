from django.shortcuts import render
from GANJI.models import ArtiInfo
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    limit =  1
    arti_info =ArtiInfo.objects[:1]
    paginator = Paginator(arti_info,limit)
    page = request.GET.get('page',1)
    load = paginator.page(page)
    context={
        'ArtiInfo' : load
    }
    return render(request,'index.html',context)

