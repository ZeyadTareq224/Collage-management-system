from django.db import models
from django.contrib.auth.models import User
from CoursesMS.models import Course

class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	phone = models.CharField(max_length=12, null=True)
	student_id = models.CharField(max_length=10, null=True)
	reg_courses = models.ManyToManyField(Course, verbose_name="Register Yout Courses")

	def __str__(self):
		return self.user.username



class Attendance(models.Model):

	att_time = models.DateTimeField(auto_now_add=True)
	student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
	course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		obj_name = f'{self.student}: {self.course}'
		return obj_name