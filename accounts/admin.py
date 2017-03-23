from django.contrib import admin
from accounts.models import *

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(PreposeResidentielProfile)
admin.site.register(PreposeAffaireProfile)

admin.site.register(ClientAffaire)
admin.site.register(ClientResidentiel)
