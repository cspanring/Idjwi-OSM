"""
Translation rules for the Idjwi villages.
"""

def translateAttributes(attrs):
	if not attrs: return
	
	tags = {}
	
	tags.update({'place':'village'})
	tags.update({'source':'Dana Thompson'})
	
	"""
	HEALTH FACILITIES
	"""
	
	# Village name
	
	tags.update({'name': attrs['Village']})
	
	# Place parents
	
	tags.update({'is_in:country':'Democratic Republic of the Congo'})
	tags.update({'is_in:province': attrs['Prov']})
	tags.update({'is_in:territory': attrs['Territory']})
	tags.update({'is_in:sector': attrs['Sector']})

	return tags