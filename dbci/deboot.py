from subp import runch
import config

def deboot():
	import os, shutil
	# probably some dir like lost+found 
	# not use a variable to prevent data loss
	for filename in os.listdir(config.config["mnt"]):
		file_path = f'{config.config["mnt"]}/{filename}'
		if os.path.isfile(file_path) or os.path.islink(file_path):
			os.unlink(file_path)
		elif os.path.isdir(file_path):
			shutil.rmtree(file_path)
	runch(["mmdebstrap", "--arch=amd64", "testing", config.config["mnt"]])
