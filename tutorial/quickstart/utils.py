import requests, zipfile, StringIO
from datetime import datetime
import xml.etree.ElementTree as ET
import os
import shutil

def zipdir(path, ziph):
    # ziph is zipfile handle
    os.chdir('/tmp')
    for root, dirs, files in os.walk(path):
        for filename in files:
			ziph.write(os.path.join(root, filename).replace('/tmp/',''))

def Change_data(filename, label):
	try:
		r = requests.get(filename)
		z = zipfile.ZipFile(StringIO.StringIO(r.content))
	except Exception:
		return None
	foldername = filename.split('/')[-1].split('.')[0]
	z.extractall('/tmp/{}'.format(foldername))
	
	filename = '/tmp/{}/META-INF/container.xml'.format(foldername)
	current_time = datetime.now().isoformat()
	f = open(filename, 'a')
	comment = "\n <!-- date: {0} watermark: {1} -->".format(current_time, label)
	f.write(comment)
	f.close()
	path_template='/tmp/{0}'.format(foldername)
	zippath = '{0}.epub'.format(foldername)
	s = StringIO.StringIO()
	zipf = zipfile.ZipFile(s, 'w')
	
	zipdir('{0}/'.format(path_template), zipf)
	zipf.close()
	shutil.rmtree(path_template)
	return {'string': s, 'zip_filename': zippath}