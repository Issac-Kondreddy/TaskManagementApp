from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

def auth_view(request):
    signup_form = CustomUserCreationForm()
    login_form = AuthenticationForm()

    if request.method == 'POST':
        if 'login' in request.POST:  # Login form was submitted
            login_form = AuthenticationForm(data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect('task_list')  # Redirect to task list

        elif 'signup' in request.POST:  # Signup form was submitted
            signup_form = CustomUserCreationForm(request.POST)  # Use CustomUserCreationForm
            if signup_form.is_valid():
                user = signup_form.save(commit=False)
                user.first_name = signup_form.cleaned_data.get('first_name')
                user.last_name = signup_form.cleaned_data.get('last_name')
                user.save()  # Save user with first and last name
                login(request, user)
                return redirect('task_list')  # Corrected redirect to task list

    return render(request, 'UserAuthentication/auth.html', {
        'signup_form': signup_form,
        'login_form': login_form,
    })

@login_required
def logout_view(request):
    auth_logout(request)
    return redirect('auth')
