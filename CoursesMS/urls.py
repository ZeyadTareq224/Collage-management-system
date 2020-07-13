from django.urls import path
from . import views

urlpatterns = [
	path('list/', views.index, name='courses_list'),
	path('create/', views.course_create, name='courses_create'),
	path('update/<str:pk>', views.course_update, name='courses_update'),
	path('delete/<str:pk>', views.course_delete, name='courses_delete'),
	path('details/<str:pk>', views.course_details, name='courses_details'),

]