from django.shortcuts import render
from .models import Relay
# Create your views here.
def relay_list(request):
    relays = Relay.objects.all()
    return render(request,'relay_list.html',{'relays':relays})
