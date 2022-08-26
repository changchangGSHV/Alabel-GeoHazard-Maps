from django_admin_inline_paginator.admin import TabularInlinePaginated
from django.contrib.auth.models import Group
from django.contrib import admin
from auxiliary.models import (
	Announcements, 
	History, 
	GeoHazard,
	Assessment,
	Hotlines,

)

class GeoHazardInline(admin.StackedInline):
	model = GeoHazard
	extra = 0


class AssessmentInline(TabularInlinePaginated):
	model = Assessment
	extra = 0
	per_page = 10


class HistoryAdmin(admin.ModelAdmin):
	inlines = [GeoHazardInline,AssessmentInline]


# admin.site.unregister(Group)
admin.site.register(Hotlines)
admin.site.register(Announcements)
admin.site.register(History, HistoryAdmin)






