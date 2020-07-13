from django.apps import AppConfig


class UsersmsConfig(AppConfig):
    name = 'UsersMS'
    def ready(self):
    	import UsersMS.signals
