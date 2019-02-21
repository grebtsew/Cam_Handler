import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(

     name='Cam_Handler',

     version='1.0',

     scripts=['Cam_Handler.py'] ,

     author="Grebtsew",

     author_email="daniel.grebtsew@gmail.com",

     description="A simple multithreaded camera stream capturer using opencv.",

     long_description=long_description,

   long_description_content_type="text/markdown",

     url="https://github.com/grebtsew/Cam_Handler",

     packages=setuptools.find_packages(),

     classifiers=[

         "Programming Language :: Python :: 3",

         "License :: OSI Approved :: MIT License",

         "Operating System :: OS Independent",

     ],

 )
