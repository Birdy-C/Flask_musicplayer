# -*- coding: UTF-8 -*-
"""
Routes and views for the flask application.
"""
import os
'''from ID3 import ID3'''
from flask import Flask
from flask import render_template
# from Flask_DAM import app
from mutagen.id3 import ID3

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


app = Flask(__name__)

@app.route('/')
@app.route('/list1')
def list1():
    """Renders the home page."""
    file = music_list('./Flask_DAM/static/list1/')
    filelist = [];
    for i in range(len(file)):
        """for i in range(1):"""
        subfile = dict(index=i+1,fileInfo=file[i])
        filelist.append(subfile)

    return render_template(
        'layout.html',
        list = filelist,
        length = len(file),
        herf = "list2"
           )



@app.route('/list2')
def list2():
    """Renders the home page."""
    file = music_list('./Flask_DAM/static/list2/')
    filelist = [];
    for i in range(len(file)):
        """for i in range(1):"""
        subfile = dict(index=i+1,fileInfo=file[i])
        filelist.append(subfile)


    return render_template(
        'layout.html',
        list = filelist,
        length = len(file), 
        herf = "list1",
           
           )

@app.route('/cover')
def cover():
    return render_template(
        'cover.html'
           )


@app.route('/cat')
def cat():

    return render_template(
        'cat.html'
           )


def music_list(folder):
    file_list = []
    for root,directors,files in os.walk(folder):
        for filename in files:
            filepath = os.path.join(root,filename)
            if filepath.endswith(".mp3"):
                id3info = ID3(filepath)
                f = open(filepath[:-4]+".txt",'r')
                lyrics = [];
                for line in f:
                    lyrics.append(line)
                fileInfo = dict(path = filepath[11:-4],artist=id3info['TPE1'].text[0],title=id3info['TIT2'].text[0],album=id3info['TALB'].text[0],txt = lyrics)
                file_list.append(fileInfo)
    return file_list
    

if __name__ == '__main__':
    app.run()
    
