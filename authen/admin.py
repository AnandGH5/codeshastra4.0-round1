from django.contrib import admin
from .models import *

admin.site.register(Profile)
admin.site.register(Hospital)
admin.site.register(Facility)
admin.site.register(Doctor)
admin.site.register(Medicine)
admin.site.register(Ward)