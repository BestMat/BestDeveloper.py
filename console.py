import os
os.system("")
# Does not run on IDLE.
def log(a):
  print(a)
def error(a):
  CRED = '\033[91m'
  CEND = '\033[0m'
  print(CRED +a+ CEND)
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
def warn(a):
 print(style.YELLOW + a)
def info(a):
 print(style.CYAN + a)
def success(a):
 print(style.GREEN + a)
