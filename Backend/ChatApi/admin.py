from django.contrib import admin
from . models import *

admin.site.register(Conversation)
admin.site.register(Participant)
admin.site.register(Message)
# Register your models here.