import time
from CamHandler import *

var = CamHandler.create_instances([(0,0,True)])

while True:
    print(var[0].frame)

    time.sleep(5)
