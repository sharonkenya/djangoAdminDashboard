from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import MyModel

admin.site.register(MyModel)
from django.contrib import admin
from .models import Resume,Service

admin.site.register(Resume)
admin.site.register(Service)


