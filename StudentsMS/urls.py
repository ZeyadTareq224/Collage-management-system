from django.urls import path
from . import views


urlpatterns = [
	path('studashboard/', views.studashboard, name="studashboard"),
	path('regcourses/', views.reg_courses, name="regcourses"),
	path('studetails/<str:pk>/', views.student_details, name="studetails"),
	path('stuassign/', views.student_assign, name="studentassign"),
	path('stureassign/<str:pk>', views.student_re_assign, name="studentreassign"),
	path('delete-student/<str:pk>/', views.delete_student, name="studentdelete"),
	path('atttendance/create/', views.create_attendance, name="create_attendance"),
	#path('att-create/<str:pk>/', views.update_attendance, name="update_attendance"),
]