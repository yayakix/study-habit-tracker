from django.contrib import admin
# import your models here
from .models import Card, Feeding, Toy

# Register your models here
admin.site.register(Card)
admin.site.register(Feeding)
admin.site.register(Toy)