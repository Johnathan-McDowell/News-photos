import requests
import json 
from newsapi.newsapi_client import NewsApiClient
import tkinter as tk
from PIL import Image,ImageTk
import numpy as np
import urllib.request   
import tkinter.messagebox

def printImages(org,info,date):
   
    
    root= tk.Tk()
    root.title("Your Week in The News")
    # Init
    newsapi = NewsApiClient(api_key='c4560a61b5144991b4d60a735e9f5812')

    # /v2/top-headlines
    top_headlines = newsapi.get_everything(
                                        from_param=date,
                                        to=date,
                                        domains=org, 
                                        q = info)
    
    json_object = json.dumps(top_headlines) 
    readable_data = json.loads(json_object)
    images = []
    for i in range((len(readable_data['articles']))):
        images.append((readable_data['articles'][i]['urlToImage']))
    images = images[0:6]
    try:
        img0 = Image.open(urllib.request.urlopen(images[0]))
        img1 = Image.open(urllib.request.urlopen(images[1]))
        img2 = Image.open(urllib.request.urlopen(images[2]))
        img3 = Image.open(urllib.request.urlopen(images[3]))
        img4 = Image.open(urllib.request.urlopen(images[4]))
        img5 = Image.open(urllib.request.urlopen(images[5]))
        newsize = (300, 300)
        canvas=tk.Canvas(root, height=600, width=900)
        img0 = img0.resize(newsize)
        img1 = img1.resize(newsize)
        img2 = img2.resize(newsize)
        img3 = img3.resize(newsize)
        img4 = img4.resize(newsize)
        img5 = img5.resize(newsize)
        AppendedImg = np.hstack((img0,img1,img2))
        gAppendedImg = np.hstack((img3,img4,img5))
    
        photo = ImageTk.PhotoImage(master = canvas,width = 900, height = 600,image=Image.fromarray(np.vstack((np.array(AppendedImg),np.array(gAppendedImg)))))
        canvas.create_image(0, 0, image=photo, anchor='nw')
        canvas.pack(side = tk.TOP, expand=True, fill=tk.BOTH)
    except:
        tkinter.messagebox.showinfo("ERROR.",  "Not enough pictures exist for this promp, please enter new values")
    
    
    root.mainloop()
   
        

   
        
