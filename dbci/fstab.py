from subp import runch, outch
import config

def findmnt(path):
	s = outch(["findmnt", "-n", "-o", "UUID", path])
	s = s.decode()
	s = s.strip()
	return f"UUID={s}"

def fstab():
	efi = findmnt("/boot/efi")
	root = findmnt("/")
	with open("/etc/fstab", "w") as f:
		print(root, "/", "ext4", "rw,noatime", 0, 1, file = f)
		print(efi, "/boot/efi", "vfat", "rw,noatime,errors=remount-ro", 0, 2, file = f)
