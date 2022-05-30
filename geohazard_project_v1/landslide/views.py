from django.shortcuts import render
from django.views import View
from .models import Landslide_Dropdown
from folium import plugins, IFrame
from auxiliary.models import Warning_Devices, Evac_Centers, Warning_Signs
import folium


class landslide(View):
	template_name = 'landslide/landslide.html'
	layers_dir = "landslide/static/data/"
	center_coord = [6.1726,125.3671]
	landslide_fields = Landslide_Dropdown.objects.all()
	warning_devices = Warning_Devices.objects.all()
	evac_centers = Evac_Centers.objects.all()
	warning_signs = Warning_Signs.objects.all()

	def post(self, request):
		return render(request,self.template_name)


	def get(self, request):

		landslide_map = folium.Map(location=self.center_coord,zoom_start=11,control_scale=True,zoom_control=True,max_bounds=True,tiles=None)

		mapBorderStyle = {'color':'#555555','weight':1,'fillColor':'rgba(0,0,0,0)'}
		highStyle = {'weight':0,'fillColor':'red','fillOpacity':0.5}
		modStyle = {'weight':0,'fillColor':'green','fillOpacity':0.5}
		lowStyle = {'weight':0,'fillColor':'yellow','fillOpacity':0.5}
		
		high_lvl_file = f"{self.layers_dir}High.geojson"
		mod_lvl_file = f"{self.layers_dir}Mod.geojson"
		low_lvl_file = f"{self.layers_dir}Low.geojson"
		map_border_file = f"{self.layers_dir}Municipal Boundary.geojson"

		folium.GeoJson(high_lvl_file,name='High',style_function=lambda x:highStyle).add_to(landslide_map)
		folium.GeoJson(mod_lvl_file,name='Moderate',style_function=lambda x:modStyle).add_to(landslide_map)
		folium.GeoJson(low_lvl_file,name='Low',style_function=lambda x:lowStyle).add_to(landslide_map)
		folium.GeoJson(map_border_file,name='Municipal Boundary',control=False,style_function=lambda x:mapBorderStyle).add_to(landslide_map)


		# Map Layers	
		folium.raster_layers.TileLayer(tiles='Stamen Terrain',name='Auxiliary Map',min_zoom=11,overlay=True,control=False).add_to(landslide_map)		
		folium.raster_layers.TileLayer(tiles='Open Street Map',name='Flood GeoHazard Map',min_zoom=11,overlay=False).add_to(landslide_map)


		for field in self.landslide_fields:

			map_img = "/media/{}".format(field.map_marker_img)
			barangay_name = field.barangay_name
			level = "{} Susceptibility".format(field.barangay_suscep_level)
			info = field.map_marker_info

			html = (
				"<b><center><img src="+map_img+" height=150 width=150></center></b>"
				"<b><center><h3>"+barangay_name+"</h3></center></b>"
				"<b><center><small>"+level+"</small></center></b>"
				"<b><p>"+info+"</p></b>"	
			)

			popup = folium.Popup(html, max_width=200, max_height=300)

			barangay_markers = folium.Marker(
				location=[field.latitude,field.longitude],
				popup=popup,
				tooltip="Click For More",
				icon=folium.Icon(color="green",icon="glyphicon-flag")).add_to(landslide_map)


		# Emergency and Warning Systems Markers
		device_group = folium.FeatureGroup(name="Warning Systems & Evac Centers",overlay=False)
		evac_group = plugins.FeatureGroupSubGroup(device_group,control=False)
		sign_group = plugins.FeatureGroupSubGroup(device_group,control=False)

		list_devices = []
		list_centers = []
		list_signs = []

		# Warning Systems
		for device in self.warning_devices:

			img = '/media/{}'.format(device.device_img)
			name = device.device_name
			location = device.location
			info = device.device_info

			html = (
				"<b><center><img src="+img+" height=150 width=150></center></b>"
				"<b><center><h3>"+name+"</h3></center></b>"
				"<b><center><small>"+location+"</small></center></b>"
				"<b><p>"+info+"</p></b>"
			)

			popup = folium.Popup(html, max_width=200, max_height=300)

			device_markers = folium.Marker(
				location=[device.latitude,device.longitude],
				popup=popup,
				icon=folium.Icon(color="red",icon="glyphicon-bullhorn"))

			list_devices.append(device_markers)

			for device in list_devices:
				device.add_to(device_group)



		# Evacuation Centers
		for building in self.evac_centers:

			img = '/media/{}'.format(building.building_img)
			name = building.building_name
			location = building.location


			html = (
				"<b><center><img src="+img+" height=150 width=150></center></b>"
				"<b><center><h3>"+name+"</h3></center></b>"
				"<b><center><small>"+location+"</small></center></b>"
			)

			popup = folium.Popup(html, max_width=200, max_height=300)

			evac_markers = folium.Marker(
				location=[building.latitude,building.longitude],
				popup=popup,
				icon=folium.Icon(color="orange",icon="glyphicon-home"))

			list_centers.append(evac_markers)
				
			for building in list_centers:
				building.add_to(evac_group)



		# Warning Signs
		for sign in self.warning_signs:

			img = '/media/{}'.format(sign.sign_img)
			name = sign.sign_name
			location = sign.location

			html = (
				"<b><center><img src="+img+" height=150 width=150></center></b>"
				"<b><center><h3>"+name+"</h3></center></b>"
				"<b><center><small>"+location+"</small></center></b>"
			)

			popup = folium.Popup(html, max_width=200, max_height=300)

			sign_markers = folium.Marker(
				location=[sign.latitude,sign.longitude],
				popup=popup,
				icon=folium.Icon(color="blue",icon="glyphicon-exclamation-sign"))

			list_signs.append(sign_markers)
				
			for sign in list_signs:
				sign.add_to(sign_group)


		# Adds Marker Groups to Map
		device_group.add_to(landslide_map)
		evac_group.add_to(landslide_map)
		sign_group.add_to(landslide_map)

		# add minimap to map
		minimap = plugins.MiniMap(toggle_display=True)
		landslide_map.add_child(minimap)

		# add full screen button to map
		plugins.Fullscreen(position='topleft').add_to(landslide_map)

		
		# add latitude and longitude tool to map
		landslide_map.add_child(folium.LatLngPopup())

		folium.LayerControl().add_to(landslide_map)

		landslide_map = landslide_map._repr_html_()


		context = {'landslide_fields':self.landslide_fields,'landslide_map':landslide_map,'title':'Landslide Map'}

		return render(request,landslide.template_name, context)

