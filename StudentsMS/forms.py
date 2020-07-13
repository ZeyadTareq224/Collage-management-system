from django import forms
from .models import Student, Attendance



class Courses_Reg_Form(forms.ModelForm):
	class Meta:
		model = Student
		fields = ['reg_courses']


class AssignStudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ['user', 'student_id']


class AttendanceForm(forms.ModelForm):
	class Meta:
		model = Attendance
		fields = ['course']
