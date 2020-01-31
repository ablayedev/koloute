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
                'all':User_data.objects.filter(user=request.user)
            }
        else:
            context={}
        if request.POST.get('post_date'):
            id_post=request.POST.get('id_date')
            print(id_post)
            data_post=User_data.objects.get(id=id_post)
            context={
                'data':data_post,
                'all':User_data.objects.filter(user=request.user)
            }
        return render(request,'dashboard/rapport.html',context)
    else:
        return redirect('utilisateur:home')

def historique(request):
    if request.user.is_authenticated:
        recup=User_data.objects.filter(user=request.user).order_by('-date')[:2]
        print(recup)
        context={
            'recup':recup
        }
        return render(request,'dashboard/historique.html',context)
    else:
        return redirect('utilisateur:home')