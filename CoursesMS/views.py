from django.shortcuts import render, redirect
from .models import Course
from .forms import CourseForm
from django.contrib.auth.models import Group
from .filters import CourseFilter
from django.contrib.auth.decorators import login_required
from UsersMS.decorators import allowed_users

@login_required(login_url='login')
@allowed_users(allowed_roles=['manager'])
def index(request):
	courses = Course.objects.all()
	number_of_courses = courses.count()
	course_filter = CourseFilter(request.GET, queryset=courses)
	courses = course_filter.qs

	context = {'courses': courses, 'number_of_courses': number_of_courses, 'course_filter': course_filter}
	return render(request, 'CoursesMS/index.html', context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['manager'])
def course_create(request):
	form = CourseForm()
	if request.method == "POST":
		form = CourseForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('courses_list')
	context = {'form': form}
	return render(request, 'CoursesMS/course_form.html', context)




@login_required(login_url='login')
@allowed_users(allowed_roles=['manager'])
def course_update(request, pk):
	course = Course.objects.get(id=pk)
	form = CourseForm(instance=course)
	if request.method == "POST":
		form = CourseForm(request.POST, instance=course)
		if form.is_valid():
			form.save()
			return redirect('courses_list')

	context = {'form': form, 'course': course}
	return render(request, 'CoursesMS/course_form.html', context)




@login_required(login_url='login')
@allowed_users(allowed_roles=['manager'])
def course_delete(request, pk):
	course = Course.objects.get(id=pk)
	if request.method == "POST":
		course.delete()
		return redirect('courses_list')
	context = {'course': course}
	return render(request, 'CoursesMS/delete_course.html', context)




@login_required(login_url='login')
@allowed_users(allowed_roles=['manager', 'student'])
def course_details(request, pk):
	course = Course.objects.get(id=pk)

	course_students = course.student_set.all()
	context = {
	'course': course,
	'course_students': course_students,
	}
	return render(request, 'CoursesMS/course_details.html', context)

