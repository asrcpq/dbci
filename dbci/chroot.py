from subp import runch
import config

def invoke_chroot():
	cmd = """
		apt update;
		apt install -y python3 git util-linux;
		python3 /tmp/inst/installer /;
	"""
	runch(["chroot", config.config["mnt"], "/bin/sh", "-c", cmd])

def chroot_run():
	with open("/etc/apt/sources.list", "w") as f:
		print(
			"deb https://deb.debian.org/debian/ testing main contrib non-free",
			file = f,
		)
	runch(["apt", "update"])
	runch(["python3", "/tmp/inst/pcconf/apt.py", "server"])

	# fstab
	from fstab import fstab
	fstab()

	# root passwd
	runch(["passwd", "-d", "root"])

	# locale
	with open("/etc/locale.gen", "w") as f:
		print("en_US.UTF-8 UTF-8", file = f)
		runch(["locale-gen"])

	# grub
	runch(["grub-install", "/boot/efi"])
	runch(["update-grub"])
