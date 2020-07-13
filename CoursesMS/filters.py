import django_filters
from .models import Course

class CourseFilter(django_filters.FilterSet):
	course_code_filter = django_filters.CharFilter(field_name='course_code', lookup_expr='icontains', label='Search by course code..')
	course_name_filter = django_filters.CharFilter(field_name='course_name', lookup_expr='icontains', label='Search by course name..')
	class Meta:
		model = Course
		fields = ['course_code_filter', 'course_semster', 'course_name_filter']	