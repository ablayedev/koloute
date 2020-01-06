from django.shortcuts import render,redirect
from .models import User_data
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return render(request,'dashboard/index.html')
    else:
        return redirect('utilisateur:home')

def rapport(request):
    if request.user.is_authenticated:
        id=0
        if User_data.objects.filter(user=request.user).exists():
            recup_id=User_data.objects.filter(user=request.user)
            for a in recup_id :
                id = a.id
            data=User_data.objects.get(id=id)
            print(data)
            context={
                'data':data,
            }
        else:
            context={}
        return render(request,'dashboard/rapport.html',context)
    else:
        return redirect('utilisateur:home')