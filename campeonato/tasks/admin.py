from django.contrib import admin

# Register your models here.
from .models import Insulina
from .models import Glicose
from .models import Meal

admin.site.register(Insulina)
admin.site.register(Glicose)
admin.site.register(Meal)