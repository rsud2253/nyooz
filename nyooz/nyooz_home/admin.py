from django.contrib import admin
from nyooz_home.models import Local,Home,City

class LocalAdmin(admin.ModelAdmin):
	list_display=('priority', 'source_paper','headline','source_paper_date')
	search_fields=('headline','snapshot_of_news')
	date_hierarchy='source_paper_date'
	ordering=('priority',)

admin.site.register(Local,LocalAdmin)

admin.site.register(Home)
admin.site.register(City)
