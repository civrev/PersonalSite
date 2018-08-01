'''
Functions for working with resource loading
'''

def get_static_path(content_type, file_name):
	return '../static/'+content_type+'/'+file_name+'.'+content_type