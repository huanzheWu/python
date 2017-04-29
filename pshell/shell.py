import os
import sys
import shlex
import getpass
import socket
import signal   
import subprocess
import platform
from func import *

built_in_cmds={}

def register_command(name,func):
        built_in_cmds[name]=func

def init():
        register_command("cd",cd)
        register_command("exit",exit)
        register_command("getenv",getenv)
        register_command("history",history)

def shell_loop():
        status = SHELL_STATUS_RUN
        while status == SHELL_STATUS_RUN:
            display_cmd_prompt()
            ignore_signals()

            try:
                cmd = sys.stdin.readline()
                cmd_tokens=tokenize(cmd)
                cmd_tokens=preprocess(cmd_tokens)
                status = execute(cmd_tokens)

            except:
                _,err,_=sys.exc_inf()
                print(err)
def main():
        init()
        shell_loop()

if __name__=="__main__":
        main()
