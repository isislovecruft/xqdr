## ttyfromandroidtoarduino.py
## Written by Isis Lovecruft, isis@patternsinthevoid.net
##

"""This script pipes bash syntax commands from the Python Android Scripting
Environment to a TTY shell, which communicates serially with an Arduino.

The user must set up a listening STTY shell by doing (in Linux):

     user@host:~$ stty -F /dev/ttyACM0 cs8 9600 ignbrk -brkint -imaxbel -opost -onlcr -isig -icanon -iexten -echo -echoe -echok -echoctl -echoke noflsh -ixon -crtscts
     user@host:~$ screen /dev/ttyACM0 9600

where /dev/ttyACM0 is the location of the Arduino device, and 9600 is the 
baud rate.
"""

def bash_it_up(script, stdin=None):
    """Returns (stdout, stderr), raises error on non-zero return code."""
    import subprocess
    # NOTE: By using a list here (['bash',...]) we avoid quoting problems,
    # because the arguments are passed in exactly this order.
    proc = subprocess.Popen(['bash', '-c', script],
                            stdout=subprocess.PIPE, 
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    if proc.returncode:
        raise ScriptException(proc.returncode, stdout, stderr, script)
    return stdout, stderr

class ScriptExeception(Exception):
    def __init__(self, returncode, stdout, stderr, script):
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr
        Exception.__init__('Error in script')

if __name__ == "__main__":
    usercmd = raw_input('--> ')
    while(1): 
        bash_it_up(usercmd)
    # This gives us a tty shell, but it ceaces the customized prompt after 
    # one command. Also, you need to define a command or keyboard interrupt
    # to exit the shell.


