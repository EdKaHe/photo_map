# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 12:43:03 2017

@author: Ediz
"""

#flask app
from flask import Flask, render_template
from photo_map import js, div, cdn_js, cdn_css

#create app instance
app=Flask(__name__) #__name__ is the name of the script

#create index page function
@app.route('/')
def index():
    return render_template('index.html', js=js, div=div, cdn_js=cdn_js, cdn_css=cdn_css)

#run the app
if __name__=='__main__':
    app.run(debug=True)
