import django_filters
from .models import Task


class TaskFilter(django_filters.FilterSet):
	task_title_filter = django_filters.CharFilter(field_name='title', lookup_expr='icontains', label='Search by task title..')
	class Meta:
		model = Task
		fields = ['task_title_filter']