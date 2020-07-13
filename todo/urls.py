from django.urls import path
from . import views

urlpatterns = [
	path('create/', views.create_task, name='create_task'),
	path('update/<str:pk>', views.update_task, name='update_task'),
	path('delete/<str:pk>', views.delete_task, name='delete_task'),
]