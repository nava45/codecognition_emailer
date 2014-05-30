from django.contrib import admin

from emailer.models import *

admin.site.register(Project)
admin.site.register(MailTemplate)

# Register your models here.
