from django.conf.urls import url
from . import views
#from password_policies.views import PasswordChangeFormView
#from password_policies.views import PasswordChangeDoneView
from django.contrib.auth.views import (
login, logout, password_reset, password_reset_done, password_reset_confirm,
password_reset_complete, password_change, password_change_done,
)


## Part 23 Django Max Goodridge
#TODO Restrindre client-list aux utilisateurs non autorisé
urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}),
    url(r'^register/$', views.register, name='register'),
    url(r'^success/$', views.success, name='success'),
    url(r'^profile/password-change-done/$', password_change_done, name='password_change_done'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^profile/password/$', views.change_password, name='change_password'), #pour le link change password
    url(r'^profile/password/$', views.change_password, name='change_password'), #TODO remove after tests
    url(r'^reset-password/$', password_reset, name='reset_password'),
    url(r'^reset-password/done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset-password/complete/$', password_reset_complete, name='password_reset_complete'),
    url(r'^lock-out/$', views.lock_out, name='lock_out'),
    url(r'^client-list/$', views.client_list, name='client_list'),
    url(r'^accounts/password/change/$', password_change, {'template_name': 'registration/password_change_form.html'},name='password_change'),
    url(r'^accounts/password/change/done/$', password_change_done,{'template_name': 'registration/password_change_done.html'},name='password_change_done'),

]
