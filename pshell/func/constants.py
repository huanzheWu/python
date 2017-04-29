import os
SHELL_STATUS_RUN = 1
SHELL_STATUS_STOP = 0

# os.path.expanduser('~') will replace ~ to user's home directory,like /home/ortonwu

# os.sep is equal to '/'

# for my mechine ,HISTORY_PATH is /home/ortonwu/.ortonwu_shell_history

HISTORY_PATH = os.path.expanduser('~')+os.sep + '.ortonwu_shell_history'
