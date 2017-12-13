# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 13:02:09 2017

@author: Ediz
"""

from bokeh.io import output_file, show
from bokeh.models import GMapPlot, GMapOptions, ColumnDataSource, Circle, Range1d, PanTool, WheelZoomTool, TapTool, BoxSelectTool, HoverTool
from bokeh.models.callbacks import CustomJS
import pandas as pd
from bokeh.embed import components
from bokeh.resources import CDN

#read all data
data=pd.read_json(r'./meta/img_data.JSON')

#create columndatasource from data dataframe
source = ColumnDataSource(data=data)

#create the map        
map_options = GMapOptions(lat=48.775424024724984, lng=9.182596206665039, map_type="terrain", zoom=12)
fig = GMapPlot(x_range=Range1d(), y_range=Range1d(), map_options=map_options,plot_height=600, plot_width=900)
fig.output_backend="webgl"
fig.outline_line_color="orange"
fig.outline_line_alpha=0.7
fig.outline_line_width=8
fig.border_fill_color="black"

#style the tools
hover_tool=HoverTool(tooltips="""
                <div id="popup">
                    <div>
                        <img
                        src="static/icons/longitude.png" height="25" alt="static/icons/longitude.png" width="25"
                        style="vertical-align: middle;"
                        ></img>
                        <pbokeh style="vertical-align: middle; font-size: 15px; font-weight: bold;">@Longitude°</pbokeh>
                        
                        <img 
                        src="static/icons/latitude.png" height="25" alt="static/icons/latitude.png" width="25"
                        style="vertical-align: middle; margin: 0px px 0px 0px;"
                        ></img>
                        <pbokeh style="vertical-align: middle; font-size: 15px; font-weight: bold;">@Latitude</pbokeh>
                    </div>
                    <div>
                        <img
                        src="@Filepath" height="@Height" alt="@Filepath" width="@Width"
                        style="vertical-align: middle; float: left; margin: 0px 15px 15px 0px;"
                        border="1"
                        ></img>
                    </div>
                    <div>
                        <img 
                        src="static/icons/date.png" height="25" alt="static/icons/date.png" width="25"
                        style="vertical-align: middle;"
                        ></img>
                        <pbokeh style="vertical-align: middle; font-size: 15px; font-weight: bold;">@Date_String<pbokeh>
                        
                        <img 
                        src="static/icons/time.png" height="25" alt="static/icons/time.png" width="25"
                        style="vertical-align: middle;"
                        ></img>
                        <pbokeh style="vertical-align: middle; font-size: 15px; font-weight: bold;">@Time_String</pbokeh>
                    </div>
                </div>
""")
wheel_zoom_tool=WheelZoomTool()
box_select_tool=BoxSelectTool()
callback=CustomJS(args=dict(source=source), code="""
                  var selected=source.selected['1d']['indices']
                  window.open(source.data.Url[selected]);                  
""")
tap_tool=TapTool(callback=callback)
pan_tool=PanTool()
fig.toolbar_location='above'
fig.toolbar.logo=None
fig.add_tools(pan_tool, wheel_zoom_tool, box_select_tool, hover_tool, tap_tool)
fig.toolbar.active_scroll= wheel_zoom_tool
fig.toolbar.active_drag=pan_tool
fig.toolbar.active_inspect=hover_tool

#set the google api key
fig.api_key = "AIzaSyC-YD_HJvpTGXZhq0gaoOaFZFguYy5B9Ic"

#draw circles on the map
circle=Circle(x="Longitude", y="Latitude", size=10, fill_color="blue", fill_alpha=0.3, line_color="orange", line_width=3, line_alpha=0.9)
renderer=fig.add_glyph(source, circle)

#define style of selected and non selected marker
nonselected_circle = Circle(size=10, fill_color="blue", fill_alpha=0.3, line_color="orange", line_width=3, line_alpha=0.9)
selected_circle = Circle(size=10, fill_color="orange", fill_alpha=0.8, line_color="orange", line_width=3, line_alpha=0.9)
renderer.selection_glyph = selected_circle
renderer.nonselection_glyph = nonselected_circle

##output figure
#output_file("photo_map.html")
#show(fig)

cdn_js=CDN.js_files[0]
cdn_css=CDN.css_files[0]
js, div=components(fig)