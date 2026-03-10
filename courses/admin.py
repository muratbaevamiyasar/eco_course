from django.contrib import admin
from .models import Lecture, Practice, Resource

admin.site.register(Lecture)
admin.site.register(Practice)
admin.site.register(Resource)