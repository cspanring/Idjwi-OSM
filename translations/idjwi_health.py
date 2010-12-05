"""
Translation rules for the Idjwi health infrastructure data.
"""

def translateAttributes(attrs):
	if not attrs: return
	
	tags = {}
	
	tags.update({'source':'Dana Thompson'})
	
	"""
	HEALTH FACILITIES
	"""
	
	# Facility name
	
	tags.update({'name': attrs['Name']})
	
	# translate HSPHtype to OSM tags
	
	if attrs['HSPHtype'] == 'Health Post':
		tags.update({'amenity':'pharmacy'})
		tags.update({'dispensing':'no'})
		
	if attrs['HSPHtype'] == 'Health Center':
		tags.update({'amenity':'clinic'})

	if attrs['HSPHtype'] == 'Hospital':
		tags.update({'amenity':'hospital'})
		tags.update({'emergency':'no'})

	return tags