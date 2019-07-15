from django.urls import path

from .views import signup, sign_in, log_out

app_name = 'users'
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('sign_in/', sign_in, name='sign_in'),
    path('logout/', log_out, name='logout'),
]