from subp import runch, outch
import os
import config

dev = config.config["disk"]

def mkpart_gpt():
	efi_size = "64MiB"
	parted = ["parted", "--script", dev]
	cmd = ["mklabel", "gpt"]
	runch(parted + cmd)
	cmd = ["mkpart", "primary", "", "fat32", "1MiB", efi_size]
	runch(parted + cmd)
	cmd = ["mkpart", "primary", "", "ext4", efi_size, "100%"]
	runch(parted + cmd)

def mkpart():
	mkpart_gpt()
	runch(["partprobe", dev])
	# strange, partprobe is still not enough to wait for the change on a usb stick
	from time import sleep
	sleep(1.0)

def getparts():
	cmd = ["lsblk", "-o", "PATH", "-n", dev]
	dd = []
	for line in outch(cmd).decode().split('\n'):
		line = line.strip()
		if not line:
			continue
		if line == dev:
			continue
		dd.append(line)
	assert len(dd) == 2
	return dd
