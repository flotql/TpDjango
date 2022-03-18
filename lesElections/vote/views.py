from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Idees
# Create your views here.
def index(request):
    choixIdees = Idees.objects.order_by('dateIdee')
    context = {'listIdees': choixIdees}
    return render(request, 'vote/index.html',context)

def detail(request):
    idee = get_obj_or_404(Idees, pk=idIdees)
    return render(request, 'vote/detail.html', {'idees': idee})