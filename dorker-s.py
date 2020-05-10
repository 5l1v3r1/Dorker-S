import argparse
from os import system, name
import os
import sys
def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')

print ("")
A = """
                    ██████   ██████  ██████  ██   ██ ███████ ██████        ███████ 
                    ██   ██ ██    ██ ██   ██ ██  ██  ██      ██   ██       ██      
                    ██   ██ ██    ██ ██████  █████   █████   ██████  █████ ███████ 
                    ██   ██ ██    ██ ██   ██ ██  ██  ██      ██   ██            ██ 
                    ██████   ██████  ██   ██ ██   ██ ███████ ██   ██       ███████

                     -:: It's Simple Python Script For Dorker Mining Tool ::-
                      :*: Tool Desinged By Black_Skull Hackers Team 💀 :*:

usage: dorker-s.py [-h] [-g] [-t]

optional arguments:
  -h, --help    show this help message and exit
  -g, --google  google mode

  """
print ("")
print(A)

parser = argparse.ArgumentParser("dorker-s.py",formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-g","--google", help="google mode", action='store_true' )

args = parser.parse_args()

if args.google :
 clear()
 from Modes import google
