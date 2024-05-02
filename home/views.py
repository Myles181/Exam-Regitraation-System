from django.shortcuts import render, redirect
from django import forms
from home.models import Examiner, Admin, Applicant
from .forms import RegForm, LoginForm
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login


from django.views import generic


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            userdet = form.cleaned_data
            reg_no = userdet['reg_no']
            password = userdet['password']

            val = request.POST.getlist('user')

            errflag = 0
            user = None

            if val[0] == 'c1':
                if not Applicant.objects.filter(reg_no=reg_no).exists():
                    errflag = 1
                else:
                    user = Applicant.objects.get(reg_no=reg_no)
                    #cyril22emmanuel
            if val[0] == 'c2':
                if not Examiner.objects.filter(reg_no=reg_no).exists():
                    errflag = 1
                else:
                    user = Examiner.objects.get(reg_no=reg_no)
            elif val[0] == 'c3':
                if not Admin.objects.filter(reg_no=reg_no).exists():
                    errflag = 1
                else:
                    user = Admin.objects.get(reg_no=reg_no)

            if errflag == 1:
                return render(request, 'home/index.html', {'msg': 'Please enter valid UserId'})
            else:
                if check_password(password, user.password):
                    if val[0] == 'c1':
                        request.session['id'] = user.id
                        return redirect('/shome/')
                    elif val[0] == 'c2':
                        request.session['id'] = user.id
                        return redirect('/examiner/examhome/')
                        #return render(request, 'home/index.html', {'msg': 'c2 is selected'})
                    elif val[0] == 'c3':

                        #return render(request, 'home/index.html', {'msg': 'c3 is selected'})
                        request.session['id'] = user.id
                        return redirect('/adminhome/')
                    else:
                        return render(request, 'home/index.html', {'msg': 'Please choose login type'})
                else:
                    return render(request, 'home/index.html', {'msg': 'Enter a valid  Password'})
        else:
            return render(request, 'home/index.html', {'msg': 'Select all the required fields'})
    else:
        return render(request, 'home/index.html', None)



def register(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            user_data = form.cleaned_data

            # Check if user exists
            if Applicant.objects.filter(username=user_data['username']).exists():
                errors = 'Username already exists'
            elif Applicant.objects.filter(reg_no=user_data['reg_no']).exists():
                errors = 'Registration number already exists'
            elif Applicant.objects.filter(email=user_data['email']).exists():
                errors = 'Email already exists'
            elif Applicant.objects.filter(mobile_no=user_data['phno']).exists():
                errors = 'Phone number already exists'
            elif user_data['password'] != user_data['rpassword']:
                errors = 'Passwords do not match'
            elif len(user_data['phno']) < 10:
                errors = 'Please enter a valid phone number'
            else:
                # Create user
                Applicant.objects.create(
                    username=user_data['username'],
                    reg_no=user_data['reg_no'],
                    email=user_data['email'],
                    password=make_password(user_data['password']),
                    mobile_no=user_data['phno']
                )
                return render(request, 'home/registration.html', {'success': True})
            return render(request, 'home/registration.html', {'errors': errors, 'form': form})
    else:
        form = RegForm()
    return render(request, 'home/registration.html', {'form': form})


