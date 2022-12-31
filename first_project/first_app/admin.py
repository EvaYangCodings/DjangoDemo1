from django.contrib import admin
from first_app.models import Topic, Webpage, AccessRecord, Company, Employee, Project
# Register your models here.

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)

admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Project)