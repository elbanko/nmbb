from django.contrib import admin
from .models import Posting
from .models import State
from .models import LegalField
# Register your models here.
admin.site.register(Posting)
admin.site.register(LegalField)
admin.site.register(State)