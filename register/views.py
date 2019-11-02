from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from register.models import Station,Box,Location
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def accueil(request):
    if request.POST.get('conect'):
        email=request.POST.get('email_c')
        password=request.POST.get('password_c')
        user=authenticate(request,username=email,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('register:option')
        else:
            print('no')
        
    if request.POST.get('sign'):
        full_name = request.POST.get('full_name')
        email=request.POST.get('email_s')
        password=request.POST.get('password_s')
        if User.objects.filter(username=email).exists():
           print('deja inscrit')
        else:
            user=User.objects.create_user(username=email,email=email,password=password,first_name=full_name)
            user.save()
            login(request,user)
            return redirect('register:option')
           
    return render(request,'register/accueil.html')

def deconect(request):
    logout(request)
    return redirect('register:accueil')

def option(request):
    return render(request,'register/options.html')

def locations(request):
    stations=Station.objects.all()
    message=""
    if request.method == "POST":
        box_id=request.POST.get('box-id')
        code=request.POST.get('code')
        jh=request.POST.get('jh')
        njh=request.POST.get('njh')
        box=get_object_or_404(Box,id=str(box_id))
        location=Location()
        location.box=box 
        location.user=request.user
        location.code=code 
        location.jh=jh
        location.njh=njh
        location.save()
        Box.objects.filter(id=str(box_id)).update(libre="non") 
        message="La location du box{} à étè  effecté avec succés.Vous pouvez vous rendre à la station {} avec le code {} pour l'utiliser".format(box_id,box.station.nom_station,code)
    context={
        'stations':stations,
        'message':message,
    }       
    return render(request,'register/location.html',context)
@csrf_exempt
def update_box(request):
    if request.method == "POST":
        id=int(request.POST.get('id'))
        box=get_object_or_404(Box,id=id)
        Box.objects.filter(id=id).update(libre="yes")
    return render(request,'register/location.html')