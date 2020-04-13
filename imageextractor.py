# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 05:50:29 2019

@author: USER
"""
from google_images_download import google_images_download
#instantiate the class
response = google_images_download.googleimagesdownload()
arguments = {"keywords":"sad boy,sad girl","limit":1000,"print_urls":True,"chromedriver":r"C:\Users\USER\Desktop\GAIP Project\chromedriver.exe"}
paths = response.download(arguments)
#print complete paths to the downloaded images
print(paths)