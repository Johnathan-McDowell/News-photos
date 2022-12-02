import requests
import json 
from newsapi.newsapi_client import NewsApiClient
import tkinter as tk
from PIL import Image,ImageTk
import numpy as np
import urllib.request   
import random
def printImages(date):
    root= tk.Tk()
    # Init
    newsapi = NewsApiClient(api_key='c4560a61b5144991b4d60a735e9f5812')

    # /v2/top-headlines
    top_headlines = newsapi.get_everything(sources='bbc-news',from_param=date,
                                        to=date)
    
    json_object = json.dumps(top_headlines) 
    readable_data = json.loads(json_object)
    images = []
    for i in range((len(readable_data['articles']))):
        images.append((readable_data['articles'][i]['urlToImage']))
    images = images[7:13]
    img = []
    img = Image.open(urllib.request.urlopen(images[0]))
    img1 = Image.open(urllib.request.urlopen(images[1]))
    img2 = Image.open(urllib.request.urlopen(images[2]))
    img3 = Image.open(urllib.request.urlopen(images[3]))
    img4 = Image.open(urllib.request.urlopen(images[4]))
    img5 = Image.open(urllib.request.urlopen(images[5]))
    newsize = (300, 300)
    canvas=tk.Canvas(root, height=600, width=900)
    img = img.resize(newsize)
    img1 = img1.resize(newsize)
    img2 = img2.resize(newsize)
    img3 = img3.resize(newsize)
    img4 = img4.resize(newsize)
    img5 = img5.resize(newsize)
    AppendedImg = np.hstack((img,img1,img2))
    gAppendedImg = np.hstack((img3,img4,img5))
   
    photo = ImageTk.PhotoImage(master = canvas,width = 900, height = 600,image=Image.fromarray(np.vstack((np.array(AppendedImg),np.array(gAppendedImg)))))
    canvas.create_image(0, 0, image=photo, anchor='nw')

    canvas.pack(side = tk.TOP, expand=True, fill=tk.BOTH)
    root.mainloop()
        
