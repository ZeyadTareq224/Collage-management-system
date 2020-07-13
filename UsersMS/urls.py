from django.urls import path, include
from . import views

urlpatterns = [
	path('home/', views.home, name='home'),
	path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('account/', views.account_settings, name='account_settings'),
    path('sysusers/', views.system_users, name='sysuser'),
    path('sysusers/update/<str:pk>', views.update_sysusers, name='sysuser_update'),
    path('sysusers/details/<str:pk>', views.details_sysusers, name='sysuser_details'),
    path('sysusers/delete/<str:pk>', views.delete_sysusers, name='sysuser_delete'),

]
