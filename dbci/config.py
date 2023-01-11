import os, sys

def get_config():
	config = {
		"mnt": "/mnt/chroot",
	}
	if os.path.exists("/tmp/chroot.json"):
		import json
		j = json.load(open("/tmp/chroot.json"))
		config = dict(j)
	i = 1
	while i < len(sys.argv):
		if sys.argv[i].startswith("--"):
			key = sys.argv[i].removeprefix("--")
			i += 1
			value = sys.argv[i]
			config[key] = value
		i += 1
	return config

config = get_config()
print(config)
