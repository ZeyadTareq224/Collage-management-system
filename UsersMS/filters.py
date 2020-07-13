import django_filters
from django.contrib.auth.models import User

class UserFilter(django_filters.FilterSet):
	username_filter = django_filters.CharFilter(field_name="username", lookup_expr='icontains', label='Search by username')
	class Meta:
		model = User
		fields = ['username_filter']