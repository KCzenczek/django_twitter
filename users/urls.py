from django.conf.urls import url

from users import views

urlpatterns = [
    url(r'^login/',
        views.LoginView.as_view(), name='login-user'),
    url(r'^logout/',
        views.LogoutView.as_view(), name='logout-user')

]
