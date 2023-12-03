from django.contrib import admin
from .models import Books, Auther, Review
# Register your models here.
clay = [Auther, Books, Review]
for i in clay:
    admin.site.register(i)