from django.contrib import admin
from .models import Bugs, Comments, Features
# Register your models here.

admin.site.register(Bugs)
admin.site.register(Features)
admin.site.register(Comments)
