from django.apps import AppConfig
from django.contrib import admin
#from home.models import Contact

from django.apps import AppConfig

class MatcherConfig(AppConfig):
    name = 'matcher'
    verbose_name = 'Match-Making' # not directly importing contact in aaps.py , it will give error
    def ready(self):
        from home.models import Contact
        admin.site.register(Contact)
#admin.site.register(Contact)
class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
