from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, AccountSettingsForm, UpdateProfileImage, SystemUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from .models import Profile
from .filters import UserFilter
from todo.models import Task
from todo.filters import TaskFilter
from .decorators import allowed_users
from django.contrib.auth.decorators import login_required
from StudentsMS.models import Student
from StudentsMS.filters import StudentFilter









def home(request):

	context = {}
	return render(request, 'UsersMS/home.html', context)



def register(request):
	form = UserRegisterForm()
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Your account has been created, you can login now.")
			return redirect('login')

	context = {'form': form}	
	return render(request, 'UsersMS/register.html', context)				


def loginPage(request):	
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		manager_list = Group.objects.get(name='manager').user_set.all()
		student_list = Group.objects.get(name='student').user_set.all()
		teacher_list = Group.objects.get(name='teacher').user_set.all()

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.error(request, "Username Or Password Is Incorrect")
	context = {}
	return render(request, 'UsersMS/login.html', context)	


@login_required(login_url='login')
def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
def profile(request):
	profile = Profile.objects.get(user=request.user)
	form = UpdateProfileImage(instance=profile)
	if request.method == "POST":
		form = UpdateProfileImage(request.POST, request.FILES, instance=profile)
		if form.is_valid():
			form.save()
			return redirect('profile')
	context = {'form': form}
	return render(request, 'UsersMS/profile.html', context)

@login_required(login_url='login')
def account_settings(request):
	user = request.user
	manager_list = Group.objects.get(name='manager').user_set.all()
	student_list = Group.objects.get(name='student').user_set.all()
	teacher_list = Group.objects.get(name='teacher').user_set.all()
	form = AccountSettingsForm(instance=user)
	if request.method == "POST":
		form = AccountSettingsForm(request.POST, instance=user)
		if form.is_valid():
			form.save()
			if user in manager_list:
				return redirect('courses_list')
			elif user in teacher_list:
				return redirect('courses_list')	
			elif user in student_list:
				return redirect('courses_list')

	context = {'form': form}
	return render(request, 'UsersMS/account_settings.html', context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['manager'])
def system_users(request):

	tasks = Task.objects.all()
	task_filter = TaskFilter(request.GET, queryset=tasks)
	tasks = task_filter.qs

	users = User.objects.all()
	user_filter = UserFilter(request.GET, queryset=users)
	users = user_filter.qs

	students = Student.objects.all()
	stu_filter = StudentFilter(request.GET, queryset=students)
	students = stu_filter.qs


	context = {
	'users': users,
	'user_filter': user_filter,
	'tasks': tasks,
	'task_filter':task_filter,
	'students': students,
	'stu_filter':stu_filter,
	 }
	return render(request, 'UsersMS/sysusers.html', context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['manager'])
def update_sysusers(request, pk):
	user = User.objects.get(id=pk)
	form = SystemUserForm(instance=user)
	if request.method == "POST":
		form = SystemUserForm(request.POST, instance=user)
		if form.is_valid():
			form.save()
			return redirect('sysuser')
	context = {'form': form}
	return render(request, 'UsersMS/usersms_form.html', context)





@login_required(login_url='login')
@allowed_users(allowed_roles=['manager'])
def details_sysusers(request, pk):
	userd = User.objects.get(id=pk)

	context = {'userd': userd}
	return render(request, 'UsersMS/user_details.html', context)




@login_required(login_url='login')
@allowed_users(allowed_roles=['manager'])
def delete_sysusers(request, pk):
	userd = User.objects.get(id=pk)
	if request.method == "POST":
		userd.delete()
		return redirect('sysuser')

	context = {'userd': userd}	
	return render(request, 'UsersMS/delete_user.html', context)	


	