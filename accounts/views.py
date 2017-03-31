from django.shortcuts import render, redirect, HttpResponse, render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required
from lab5 import settings
from .models import ClientResidentiel, ClientAffaire

def lock_out(request):
    return render(request, 'accounts/lock_out.html')

#@login_required
def home(request):
    if request.user.is_authenticated:
        return render(request, 'accounts/home.html')

    else:
        return redirect('/account/login/')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/account/success/')

        #SI le form n'est pas bon
        else:
            return redirect('/account/register/')

    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)

#@login_required #decorateur pour que seulement les loged in users peuvent voir la page
def view_profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)

#view pour la page de changement d'info du user
#@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            password_confirmation = form.cleaned_data['password_confirmation']
            if request.user.check_password(password_confirmation):
                form.save()
                return redirect('/account/profile/')
            else:
                logout(request)
                return redirect('/account/login/')

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

#page pour account successful created
def success(request):
    return render(request, 'accounts/success.html')

#View pour le changement de password d'un user
#@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user) #garde la session active mm quand on change le password
            return redirect('/account/profile/')

        else:
            return redirect('/account/change-password/')

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)


def client_list(request):

    print(request.user.username)
    print(request.user.has_perm('accounts.view_all_clients'))

    #Si le user a les permission de voir tout les clients
    if request.user.has_perm('accounts.view_all_clients') or request.user.is_superuser:
        client_list_res = ClientResidentiel.objects.order_by('email')
        client_list_aff = ClientAffaire.objects.order_by('email')

        args = {'client_list_res': client_list_res, 'client_list_aff': client_list_aff }
        return render(request, 'accounts/client_list.html', args)

    else:
        client_list_aff = ClientAffaire.objects.order_by('email')
        args = {'client_list_aff': client_list_aff }
        return render(request, 'accounts/client_list.html', args)
