from django.shortcuts import render
import numpy as np
#import pandas as pd
import os
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt
import docx2txt
from striprtf.striprtf import rtf_to_text

def index(request):
    return render(request,'index.html')


def home(request):
    if request.method=="POST":
        text=request.POST.get('text')
        image=request.FILES.get('image')
        stopw=request.POST.get('stopw')
        stop=request.POST.get('stop')
        color=request.POST.get('color')
        custom=request.POST.get('custom')
        color=str(color)
        print(color)
        if custom!=None:
            color=custom
        #text="Tkinter is lightweight and relatively painless to use compared to other frameworks. This makes it a compelling choice for building GUI applications in Python, especially for applications where a modern shine is unnecessary, and the top priority is to build something that’s functional and cross-platform quickly. To understand Tkinter better, we will create a simple GUI. "
        #wcloud = WordCloud().generate(text)
        if image!=None and stopw==None:
            mask = np.array(Image.open(image))
            wcloud = WordCloud(background_color="white",max_font_size=100, mask=mask, contour_width=1).generate(text)
            image_colors = ImageColorGenerator(mask)
            wcloud.recolor(color_func=image_colors)
            wcloud.to_file("media/save3.png")
            return render(request,'output.html')
        elif stopw!=None and image==None:
            stopword=set(STOPWORDS)
            if stop!=None:
                stop=str(stop).replace(" ","")
                #print(stop)
                li = list(stop.split(","))
                stopword.update(li)
                #print(li)
            #stopword.update(["early","text","NLP"])
            wcloud= WordCloud(background_color="white",max_font_size=100, stopwords=stopword, contour_width=1).generate(text)
            wcloud.to_file("media/save3.png")
            return render(request,'output.html')
        elif stopw!=None and image!=None:
            stopword=set(STOPWORDS)
            if stop!=None:
                stop=str(stop).replace(" ","")
                #print(stop)
                li = list(stop.split(","))
                stopword.update(li)
                #print(li)
            #stopword.update(["early","text","NLP"])
            mask = np.array(Image.open(image))
            wcloud = WordCloud(background_color="white",max_font_size=100, mask=mask, stopwords=stopword, contour_width=1).generate(text)
            image_colors = ImageColorGenerator(mask)
            wcloud.recolor(color_func=image_colors)
            wcloud.to_file("media/save3.png")
            return render(request,'output.html')
        elif image==None and stopw==None:
            # s=str(doc)
            # if s.endswith(".rtf"):
            #     with open(s) as infile:
            #         content = infile.read()
            #         text = rtf_to_text(content)
            wcloud= WordCloud(background_color="white",max_font_size=100, contour_width=1).generate(text)
            wcloud.to_file("media/save3.png")
            return render(request,'output.html')
    return render(request,'home.html')