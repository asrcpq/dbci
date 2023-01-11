import subprocess

def runch(*args):
	subprocess.run(*args, check = True)

def outch(*args):
	return subprocess.check_output(*args) # check_output already have check
