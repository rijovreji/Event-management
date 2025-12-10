from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def user(request):
    if request.method=="POST":
        username=request.POST.get("username")
        email_id=request.POST.get("email")
        password=request.POST.get("password")
        conf_pass=request.POST.get("confirm_password")
        if password==conf_pass:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already taken")
                return redirect('register/')
            elif User.objects.filter(email=email_id).exists():
                messages.info(request,"email already taken")

                return redirect('register/')
            else:
                user_reg=User.objects.create_user(username=username,email=email_id,password=password)
                user_reg.save()
                messages.info(request,"successfuly created")

                return redirect('/')
        else:
            messages.info(request, "password doesn't match")

            return redirect('register/')





    return render(request,'reg.html')