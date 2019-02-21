# Cam_Handler
A cam_handler pip package python3 for handling camera streams.

# Install
Download and run the following command in dist folder:
```
pip install Cam_Handler-1.0-py3-none-any.whl
```
The reason i won't upload this package to PyPi is that it's only a test.
How to create your own pip packages?
Check this great tutorial:
https://dzone.com/articles/executable-package-pip-install

# Functions

* create_instances( source_list ) - where source_list is a list containing list(address,name,viz) or just address. It return a list of all created threads.
* in thread Camera:
play()
pause()
run()
stop()

Image can be recieved from Camera.frame!

# Examples

Start camera and show frames
```
import time
from CamHandler import *


// three ways of adding camera to list (address,name,viz)
source_list = [0, "rtsp://username:password@ip:port/path", (0,0,True)]

// Create instances, var will contain list to all threads
var = CamHandler.create_instances(source_list)

while True:
    print(var[0].frame)
    time.sleep(5)
```

Start camera only
```
Camera( address = 0, name= 0, visualize = True).start()
```

# Other
This is my first made pip package!
Hope you enjoy it!
