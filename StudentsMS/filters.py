import django_filters
from .models import Student



class StudentFilter(django_filters.FilterSet):
	stu_id_filter = django_filters.CharFilter(field_name='student_id', lookup_expr='icontains', label='Search by student id')
	class Meta:
		model = Student
		fields = ['stu_id_filter']
