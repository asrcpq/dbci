from subp import runch

def mkfs(efi, root):
	runch(["mkfs.vfat", efi])
	runch(["mkfs.ext4", root])
