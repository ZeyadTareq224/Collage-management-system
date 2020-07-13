from django.forms import ModelForm
from .models import Course

class CourseForm(ModelForm):

	class Meta:
		model = Course
		fields = ['course_name', 'course_code', 'course_semster']