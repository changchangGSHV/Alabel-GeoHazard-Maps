from django.contrib import admin
from flood.models import (
	Flood,
	Flood_Dropdown,
	Flood_Evac_Procedures

)

# admin.site.register(Flood)
admin.site.register(Flood_Dropdown)
# admin.site.register(Flood_Guidelines)
admin.site.register(Flood_Evac_Procedures)



from landslide.models import (
	Landslide,
	Landslide_Dropdown,
	Landslide_Guidelines,
	Landslide_Evac_Procedures

)

# admin.site.register(Landslide)
admin.site.register(Landslide_Dropdown)
admin.site.register(Landslide_Guidelines)
admin.site.register(Landslide_Evac_Procedures)


from auxiliary.models import Warning_Devices, Evac_Centers, Warning_Signs, History, HistoryAdmin

admin.site.register(Warning_Devices)
admin.site.register(Evac_Centers)
admin.site.register(Warning_Signs)
admin.site.register(History,HistoryAdmin)


