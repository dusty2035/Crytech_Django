from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from accounts.forms import Edit_profile_form
from django.contrib import auth
import re 



# Create your views here.



def signup(request):
    if request.method == 'POST':
        chkbox = request.POST.getlist('signup_checkbox')
        name = request.POST['name']
        email = request.POST['email']
        try:

            user = User.objects.get(username = request.POST['name'])
            return render(request, 'signup.html' , {'error' : 'username has already been taken'})
        except User.DoesNotExist:
            password = request.POST['password1'] 
            if (len(password)<8): 
                return render(request, 'signup.html' , {'error' : 'password is short'})  
            elif not re.search("[a-z]", password): 
                return render(request, 'signup.html' , {'error' : 'password doesn\'t contain lowercase'})
            elif not re.search("[A-Z]", password): 
                return render(request, 'signup.html' , {'error' : 'password doesn\'t contain Uppercase'})
            elif not re.search("[0-9]", password): 
                return render(request, 'signup.html' , {'error' : 'password doesn\'t contain digits'})
            elif re.search("\s", password): 
                return render(request, 'signup.html' , {'error' : 'no spaces allowed'})
            else:
                if request.POST['password0'] == request.POST['password1'] :
                    if len(name) >= 4 :
                        if chkbox :
                            if re.match("^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email) :
                                user =  User.objects.create_user(request.POST['name'], password = request.POST['password1'], email= request.POST['email'])
                                auth.login(request,user)
                                return render(request, 'user_page.html', {"user" : user}) 
                            else :
                                return render(request, 'signup.html' , {'error' : 'Please enter your email'}) 
                        else :
                            return render(request, 'signup.html' , {'error' : 'you must agree to Term\'s of service'}) 
                    else :
                        return render(request, 'signup.html' , {'error' : 'user name is invalid'})
                else :
                    return render(request, 'signup.html' , {'error' : 'passwords dont match'})           
        


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username = request.POST['user'] , password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return render(request, 'user_page.html')
        elif User.objects.filter(username = request.POST['user']).exists() or User.objects.filter(password = request.POST['password']):
            return render(request , 'login_signup.html' , {'error1' : "user name or password is incorect"})
        else :
            return render(request , 'login_signup.html' , {'error1' : "user doesn't exist"})
    else :
        return render(request , 'login_signup.html')
    


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')


def loged_in(request):
    return render(request , 'user_page.html')


def edit_profile(request):
    if request.method == 'post':
        form = Edit_profile_form(request.POST , instance = request.user)

        if form.is_valid():
            form.save()
            return redirect('logedin')
    else :
        form = Edit_profile_form(instance = request.user)
        args = {'form' : form}
        return render(request , 'edit_profile.html' , args)