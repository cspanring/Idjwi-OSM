"""
Translation rules for the Idjwi (CD) road and health infrastructure data.
"""

def translateAttributes(attrs):
	if not attrs: return
	
	tags = {}
	
	tags.update({'source':'Dana Thompson'})
	
	"""
	==== R O A D S ====
	"""
	
	# inventing some new OSM tags
	
	tags.update({'moto_speed': attrs['MotoKM_H']})
	tags.update({'foot_speed': attrs['WalkKM_H']})
	
	# translate road type to OSM tags
	
	if attrs['type'] == 'drivable':
		tags.update({'highway':'unclassified'})
		
	if attrs['type'] == 'primary path':
		tags.update({'highway':'track'})
		tags.update({'tracktype':'grade5'})
		tags.update({'surface':'dirt'})

	if attrs['type'] == 'secondary path':
		tags.update({'highway':'path'})
		tags.update({'surface':'ground'})

	return tags