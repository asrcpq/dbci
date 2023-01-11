import sys
from run import run, chroot_run, cleanup
import traceback

if len(sys.argv) >= 2:
	if sys.argv[1] == "/":
		chroot_run()
	else:
		try:
			run()
		except Exception as e:
			print(traceback.format_exc())
			print(e)
		finally:
			cleanup()
