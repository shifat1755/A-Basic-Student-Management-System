from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import CustomUser

def home(request):
    return render(request, "index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        user_type = request.POST.get('options', None)
        if user_type == "opt1":
            user_type = "Teacher"
        else:
            user_type = "Student"

        if all([username, first_name, last_name, email, pass1, pass2, user_type]):
            # Check if passwords match
            if pass1 == pass2:
                # Create user
                myuser = CustomUser.objects.create_user(username, email, pass1)
                myuser.first_name = first_name
                myuser.last_name = last_name
                myuser.user_type = user_type
                myuser.save()

                # Save user type in session
                request.session['user_type'] = user_type

                messages.success(request, "Your account has been created")
                return redirect('signin')
            else:
                messages.error(request, "Passwords do not match")
        else:
            messages.error(request, "Please fill in all required fields")

    return render(request, "signup.html")




def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']  # Assuming password1 is the name attribute for the password field

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return loggedin(request)
        else:
            messages.error(request, "Username and password are incorrect")
            return redirect('home')

    return render(request, "signin.html")

def loggedin(request):
    if request.user.is_authenticated:
        usertype = request.session.get('user_type', None)
        students=None
        if request.user.user_type == 'Teacher':
            students = CustomUser.objects.filter(user_type='Student')
        return render(request, 'loggedin.html', {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'usertype': request.user.user_type,
            'email': request.user.email,
            'students':students
        })
    else:
        return redirect('home')
