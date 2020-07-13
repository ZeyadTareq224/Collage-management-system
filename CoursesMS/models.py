from django.db import models

class Course(models.Model):
	SEMESTERS = (
		('first semster', '1'),
		('secode semster', '2'),
		)
	course_name = models.CharField(max_length=50, unique=True)
	course_code = models.CharField(max_length=6, unique=True)
	course_semster = models.CharField(max_length=20, choices=SEMESTERS)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)
	cridit_hours = models.IntegerField(null=True)

	def __str__(self):
		return self.course_name
