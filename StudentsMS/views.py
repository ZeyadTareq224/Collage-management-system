from django.shortcuts import render, redirect
from .forms import Courses_Reg_Form,  AssignStudentForm, AttendanceForm
from .models import Student, Attendance
from CoursesMS.models import Course
from django.contrib.auth.models import Group
from CoursesMS.filters import CourseFilter
from django.http import HttpResponse

# Create your views here.
def studashboard(request):

	courses = Course.objects.all()
	course_filter = CourseFilter(request.GET, queryset=courses)
	courses = course_filter.qs


	user = request.user
	student = Student.objects.get(user=user) 
	reg_courses =  student.reg_courses.all()

	#statistics
	not_regestered_courses = courses.count() - reg_courses.count()




	att = Attendance.objects.all().filter(student=student)

	context = {
	'courses': courses,
	'course_filter':course_filter,
	'regcourses': reg_courses,
	'not_regestered_courses': not_regestered_courses,
	'att':att
	}
	return render(request, 'StudentsMS/studashboard.html', context)


def reg_courses(request):
	student = Student.objects.get(user=request.user)
	user = request.user

	form = Courses_Reg_Form(instance=student)
	if request.method == "POST":
		form = Courses_Reg_Form(request.POST, instance=student)
		if form.is_valid():
			form.instance.user = user
			form.save()
			return redirect('studashboard')

	context = {'form': form}
	return render(request,'StudentsMS/reg_courses_form.html', context)


def student_details(request, pk):
	student = Student.objects.get(id=pk)

	regcourses = student.reg_courses.all()


	context = {'student': student, 'regcourses': regcourses}
	return render(request, 'StudentsMS/student_details.html', context)


def student_assign(request):
	form = AssignStudentForm()
	if request.method == "POST":
		form = AssignStudentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('sysuser')


	context = {'form': form}
	return render(request, 'StudentsMS/stu_assign_form.html', context)


def student_re_assign(request, pk):
	student = Student.objects.get(id=pk)
	form = AssignStudentForm(instance=student)
	if request.method == "POST":
		form = AssignStudentForm(request.POST, instance=student)
		if form.is_valid():
			form.save()
			return redirect('sysuser')
	context = {'form': form, 'student':student}
	return render(request, 'StudentsMS/stu_assign_form.html', context)


def delete_student(request, pk):
	student = Student.objects.get(id=pk)
	if request.method == "POST":
		student.delete()
		return redirect('sysuser')

	context = {'student': student}
	return render(request, 'StudentsMS/delete_student.html', context)



def create_attendance(request):
	student = Student.objects.get(user=request.user)
	reg_courses = list(student.reg_courses.all())
	att_form = AttendanceForm()
	if request.method == "POST":
		att_form = AttendanceForm(request.POST)
		if att_form.is_valid():
			att_form.instance.student = student
			att_form.save()
			return redirect('studashboard')
			

	context = {'att_form': att_form, 'student': student}
	return render(request, 'StudentsMS/attendance_form.html', context)


'''
def update_attendance(request, pk):
	course = Course.objects.get(id=pk)
	student = Student.objects.get(id=request.user.id)
	att_obj = Attendance.objects.get(course=course, student=student)
	att_form = AttendanceForm(instance=att_obj)
	if request.method == "POST":
		att_form = AttendanceForm(request.POST, instance=att_obj)
		if att_form.is_valid():
			att_form.save()
			return redirect('studashboard')

	context = {'att_form': att_form}
	return render(request, 'StudentsMS/attendance_form.html', context)	
'''	

