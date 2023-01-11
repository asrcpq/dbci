from subp import runch

def md(path):
	from pathlib import Path
	Path(path).mkdir(exist_ok = True, parents = True)

def chroot_mounter(root):
	md(f"{root}/proc")
	runch(["mount", "--types", "proc", "/proc", f"{root}/proc"])
	md(f"{root}/sys")
	runch(["mount", "--make-rslave", "--rbind", "/sys", f"{root}/sys"])
	md(f"{root}/dev")
	runch(["mount", "--make-rslave", "--rbind", "/dev", f"{root}/dev"])

def mounter(part, loc):
	md(loc)
	runch(["mount", part, loc])

def umounter(part):
	try:
		runch(["umount", "-R", part])
	except Exception as e:
		print(e)
