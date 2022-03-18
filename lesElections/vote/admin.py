from django.contrib import admin
from .models import Penseur, Idees, Chevelure, Roles, Votants, Voter

# Register your models here.
admin.site.register(Penseur)
admin.site.register(Idees)
admin.site.register(Chevelure)
admin.site.register(Roles)
admin.site.register(Votants)
admin.site.register(Voter)