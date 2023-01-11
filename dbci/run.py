import os, sys, shutil
from mounter import mounter, umounter, chroot_mounter
from parter import mkpart, getparts
from chroot import invoke_chroot, chroot_run
import config

part_efi = None
part_root = None

def part():
	mkpart()

def getpart():
	global part_efi, part_root
	[part_efi, part_root] = getparts()

def mroot():
	mounter(part_root, config.config["mnt"])

def deboot():
	from deboot import deboot
	deboot()

def mother():
	mounter(part_efi, f'{config.config["mnt"]}/boot/efi')
	chroot_mounter(config.config["mnt"])

def mkfs2():
	from mkfs import mkfs
	mkfs(part_efi, part_root)

def cpthis():
	if os.path.exists(f'{config.config["mnt"]}/tmp/inst'):
		shutil.rmtree(f'{config.config["mnt"]}/tmp/inst')
	shutil.copytree(os.getcwd(), f'{config.config["mnt"]}/tmp/inst')
	import json
	json.dump(
		config.config,
		open(f'{config.config["mnt"]}/tmp/chroot.json', "w"),
	)

def part1():
	part()
	getpart()
	mkfs2()
	mroot()
	deboot()
	mother()
	cpthis()

def part1_reuse():
	getpart()
	mroot()
	mother()
	cpthis()

def run():
	part1()
	#part1_reuse()
	invoke_chroot()

def cleanup():
	umounter(config.config["mnt"])
