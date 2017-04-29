from .constants import *
# os.chdir(args) will change the work directory into args

def cd(args):
    if len(args) >0:
        os.chdir(args[0])
    else:
        # if args is null , will change directory into user's home 
        os.chdir(os.getenv('HOME'))
    return SHELL_STATUS_RUN

