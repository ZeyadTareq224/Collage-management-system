from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required
from UsersMS.decorators import allowed_users

@login_required(login_url='login')
@allowed_users(allowed_roles=['manager'])
def create_task(request):
	user = request.user
	form = TaskForm()
	if request.method == "POST":
		form = TaskForm(request.POST)
		if form.is_valid():
			form.instance.user = user
			form.save()
			return redirect('sysuser')
	context = {'form': form}		
	return render(request, 'todo/task_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['manager'])
def update_task(request, pk):
	task = Task.objects.get(id=pk)
	form = TaskForm(instance=task)
	if request.method == "POST":
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('sysuser')


	context = {'form': form}
	return render(request, 'todo/task_form.html', context)	



@login_required(login_url='login')
@allowed_users(allowed_roles=['manager'])
def delete_task(request, pk):
	task = Task.objects.get(id=pk)
	if request.method == "POST":
		task.delete()
		return redirect('sysuser')

	context = {'task': task}
	return render(request, 'todo/delete_task.html', context)
