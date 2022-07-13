from django.contrib import admin
# import your models here
from .models import Card, Session, Resource

# Register your models here
admin.site.register(Card)
admin.site.register(Session)
admin.site.register(Resource)