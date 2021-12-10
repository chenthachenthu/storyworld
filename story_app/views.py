from django.contrib import  messages
from django.contrib.auth.models import User,auth
from django.http import request
from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from story_app.forms import Storyforms
from story_app.models import story_teller
from django.core.files.storage import FileSystemStorage

def home(request):
    if request.method == "POST":
        user_name = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=user_name, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("story")
        else:
            messages.info(request, "invalid credentials")
            return redirect("home")
    else:
        return render(request,"home.html")


def registration(request):

    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password2 =request.POST['password2']
        if username=='':
            messages.info(request,"please enter the username")
            return redirect("registration")

        elif password=='' and password2=='':
            messages.info(request,"please enter the password")
            return redirect("registration")

        else:
            if password==password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request,"username taken")
                    return redirect("registration")
                elif User.objects.filter(email=email).exists():
                    messages.info(request, "email taken")
                    return redirect("registration")
                else:
                    user=User.objects.create_user(username=username,password=password,email=email)
                    user.first_name=firstname
                    user.last_name=lastname
                    user.save()
                    print('Registered')
            else:
                print("password not matched")
                messages.info(request,"password not matched")
                return redirect('registration')
            return redirect('/')
    else:
        return render(request,'registration.html')

def story(request):
    story=story_teller.objects.all()
    return render(request,"story.html",{'stories':story})

def my_name(request):
    username=None
    if request.user.is_authenticated:
        username=request.user.username
    return username

def crstory(request):
    story = story_teller.objects.filter(storyteller=request.user)
    print(request.user)
    if request.method == "POST" and request.FILES['myfile']:
        print(1)
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name,myfile)
        url = fs.url(filename)
        caption = request.POST.get('caption')
        user = User.objects.get(username=my_name(request))
        img = url
        desc=request.POST.get('desc')
        obj = story_teller.objects.create(caption=caption, storyteller=user, desc=desc)
        obj.image=img
        obj.save()
        return redirect("crstory")
    return render(request,"crstory.html",{"story":story})

def story_update(request,id):
    filepath = request.FILES['filepath'] if 'filepath' in request.FILES else False
    if request.method == 'POST' and filepath:
        myimg = request.FILES['myimg']
        fs = FileSystemStorage()
        filename = fs.save(myimg.name, myimg)
        url = fs.url(filename)
        img=url
        obj=story_teller.objects.get(id=id)
        obj.image=img
        obj.save()
    else:
        print(1)

    obj1 = story_teller.objects.get(id=id)
    form=Storyforms(request.POST or None,instance=obj1)
    if form.is_valid():
        form.save()
        return redirect('crstory')
    return render(request,"updatestory.html",{'obj':obj1,'form':form})

def story_delete(request,id):
        obj2 = story_teller.objects.get(id=id)
        if request.method == 'POST':
            obj2.delete()
            return redirect('crstory')
        return render(request, 'delete.html', {'obj': obj2})

def logout(request):
    auth.logout(request)
    return redirect('home')