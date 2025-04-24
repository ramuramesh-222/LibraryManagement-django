from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import User

def loginpage(request):
    
    if request.user.is_authenticated:
        return redirect('/inventory/products/')

    context= {
        "error" : ""
    }

    if request.method == "POST":
        print(request.POST)

        user = authenticate(username =request.POST['username'], password = request.POST['password'])
        print(user)

        if user is not None:

            login(request,user)

            if user.role == 0:
                return redirect('/orders/customers/')
            
            elif user.role == 2:
                return redirect('/orders/orders/')

        
        else:

            context={
                "error": "*Invalid Username or Password"

            }

            return render(request,'login.html',context)


    return render(request, 'login.html',context)


def logoutuser(request):

    logout(request)

    return redirect('/')

def signuppage(request):

    context ={
        "error": " "
    }

    if request.method == "POST":

        user_check = User.objects.filter(username = request.POST ['username'])
        
        if len(user_check)>0:
            context={
                "error": "**user already exits...!"
            }
            return render(request, 'signup.html',context)
            
        
        else:
            new_user = User(
            username=request.POST['username'],
            first_name=request.POST['firstname'],
            last_name=request.POST['lastname'],
            email=request.POST['email'],
            age=request.POST['age'],
            role=request.POST['role']  # Correct the field name
        )
        new_user.set_password(request.POST['password'])  # Set the password
        new_user.save()  # Save the user
        return redirect('/')
    

    return render(request, 'signup.html',context)