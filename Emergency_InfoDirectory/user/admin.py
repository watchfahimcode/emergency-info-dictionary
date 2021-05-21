from django.contrib import admin
from .models import Profile
from .models import Division
from .models import District
from .models import Subdistrict

# Register your models here.
admin.site.register(Profile)
admin.site.register(Division)
admin.site.register(District)
admin.site.register(Subdistrict)