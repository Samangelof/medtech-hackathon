from django.contrib import admin
from .models import Maternity, UserNet, Doctors

admin.site.register(Doctors)
admin.site.register(UserNet)
admin.site.register(Maternity)

