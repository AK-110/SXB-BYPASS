import os, platform, time

try:

    import requests

except:

    os.system('pip install requests')

os.system('git pull')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    import fuck_sxb

elif bit == '32bit':

    import fuck_sxb
