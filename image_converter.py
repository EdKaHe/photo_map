# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 20:22:43 2017

@author: Ediz
"""
from skimage.measure import block_reduce
import datetime
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import numpy as np
import glob2
import cv2
import pandas as pd

#create function to convert geolocation to latitude and longitude in units of degrees
def convert_2_degrees(value):
    degrees=value[0]
    degree=degrees[0]/degrees[1]
    
    minutes=value[1]
    minute=minutes[0]/minutes[1]
    
    seconds=value[2]
    second=seconds[0]/seconds[1]
    
    return degree+minute/60+second/3600

#create function to read exif data from images
def get_exif(fn):
    exif_dict = {}
    img = Image.open(fn)
    info = img._getexif()
    #iterate through all exif data
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        #format geo data
        if decoded=="GPSInfo":
            gps_data = {}
            for t in value:
                sub_decoded = GPSTAGS.get(t, t)
                gps_data[sub_decoded] = value[t]
            exif_dict["Latitude"] = convert_2_degrees(gps_data["GPSLatitude"])
            exif_dict["Longitude"] = convert_2_degrees(gps_data["GPSLongitude"])
        #format datetime data
        elif decoded=="DateTimeOriginal":
            exif_dict["Datetime"] = datetime.datetime.strptime(value, "%Y:%m:%d %H:%M:%S")
            exif_dict["Date_String"]=exif_dict["Datetime"].strftime("%d. %b. %y")
            exif_dict["Time_String"]=exif_dict["Datetime"].strftime("%H:%M")
#        else:
#            exif_dict[decoded]=value
    return exif_dict

#create function to downsample images
def downsample_image(img):
    height_block=25
    width_block=25
    rgb_block=1
    img_red=block_reduce(img, block_size=(height_block, width_block, rgb_block), func=np.mean)
    return img_red, img_red.shape[1], img_red.shape[0]

if __name__=="__main__":
    img_dir=".\\images"
    filepaths=glob2.glob("{}\\*.jpg".format(img_dir))
    
    #create list with img urls
    urls=dict(
          IMG_4470=r"https://www.instagram.com/p/BbeSeiRFz9a/?taken-by=ekh.94",
          IMG_4488=r"https://www.instagram.com/p/BbUtFTuFI6Z/?taken-by=ekh.94",
          IMG_4530=r"https://www.instagram.com/p/BbZTQhXF5qn/?taken-by=ekh.94",
          IMG_4537=r"https://www.instagram.com/p/BbPSIb3FyFw/?taken-by=ekh.94", 
          IMG_4542=r"https://www.instagram.com/p/BbWp_9ZF1WF/?taken-by=ekh.94",
          IMG_4602=r"https://www.instagram.com/p/BbSFoailnPg/?taken-by=ekh.94",
          IMG_4664=r"https://www.instagram.com/p/BbHHGfVlZup/?taken-by=ekh.94",
          IMG_4710=r"https://www.instagram.com/p/BbJ8VpqFYLz/?taken-by=ekh.94",
          IMG_4731=r"https://www.instagram.com/p/BbB3OHWF1hK/?taken-by=ekh.94",
          IMG_4737=r"https://www.instagram.com/p/BbEjFydFAeN/?taken-by=ekh.94",
          IMG_4749=r"https://www.instagram.com/p/Ba_MRkAls5B/?taken-by=ekh.94",
          IMG_4797=r"https://www.instagram.com/p/BbMn5U5F-UU/?taken-by=ekh.94",
          IMG_4822=r"https://www.instagram.com/p/BbhODbql5Za/?taken-by=ekh.94", 
          Porsche_3=r"https://www.instagram.com/p/BYMMO_Qgqnf/?taken-by=ekh.94",
          IMG_6368=r"https://www.instagram.com/p/BcpGg36lAPd/?taken-by=ekh.94",
          IMG_6486=r"https://www.instagram.com/p/Bcmh919FGRj/?taken-by=ekh.94",
          IMG_6844=r"https://www.instagram.com/p/Bcj5AP-FJVY/?taken-by=ekh.94",
          IMG_4908=r"https://www.instagram.com/p/BbmL-rjl-IA/?taken-by=ekh.94",
          IMG_7733=r"https://www.instagram.com/p/BbjoecilNh_/?taken-by=ekh.94",
          IMG_4406=r"https://www.instagram.com/p/Bayl51GlTpa/?taken-by=ekh.94",
          IMG_4403=r"https://www.instagram.com/p/Bav8kGuFXQw/?taken-by=ekh.94",
          IMG_4358=r"https://www.instagram.com/p/Baq0_mfFgaL/?taken-by=ekh.94",
          IMG_4381=r"https://www.instagram.com/p/BatQBKylGJ6/?taken-by=ekh.94",
          IMG_4412=r"https://www.instagram.com/p/Ba1cNRelJR9/?taken-by=ekh.94",
          IMG_0738=r"https://www.instagram.com/p/BYlNc82FdWv/?taken-by=ekh.94",
          IMG_3043=r"https://www.instagram.com/p/BZTNOxbFa-8/?taken-by=ekh.94",
          Orange_Blau_Schlossplatz_01=r"https://www.instagram.com/p/BaY3JJeF17H/?taken-by=ekh.94",
          IMG_1456=r"https://www.instagram.com/p/BY3xqz4FSAQ/?taken-by=ekh.94",
          IMG_1434=r"https://www.instagram.com/p/BY1auoNlAjW/?taken-by=ekh.94",
          IMG_2265=r"https://www.instagram.com/p/BZOClZqFQkL/?taken-by=ekh.94",
          IMG_2303=r"https://www.instagram.com/p/BabbwXrlqs8/?taken-by=ekh.94",
          IMG_2418=r"https://www.instagram.com/p/BagfkbulP9X/?taken-by=ekh.94",
          IMG_2497=r"https://www.instagram.com/p/BaeiZBuFbFm/?taken-by=ekh.94",
          IMG_2572=r"https://www.instagram.com/p/Bab5-EvFVle/?taken-by=ekh.94",
          IMG_2627=r"https://www.instagram.com/p/BahDhEvFpbt/?taken-by=ekh.94",
          IMG_2637=r"https://www.instagram.com/p/Bad64rHlFWU/?taken-by=ekh.94",
          IMG_2658=r"https://www.instagram.com/p/BZI2TyxFajG/?taken-by=ekh.94",
          IMG_3492=r"https://www.instagram.com/p/BZ0zChElo0W/?taken-by=ekh.94",
          IMG_3524=r"https://www.instagram.com/p/BZvm3xqFvG7/?taken-by=ekh.94",
          IMG_3532=r"https://www.instagram.com/p/BZ_RFz3ljpe/?taken-by=ekh.94",
          IMG_2089=r"https://www.instagram.com/p/BY5XSNElm1m/?taken-by=ekh.94",
          IMG_2208=r"https://www.instagram.com/p/BZEl5YRlINY/?taken-by=ekh.94",
          IMG_4040=r"https://www.instagram.com/p/BaHSOwvFfW2/?taken-by=ekh.94",
          IMG_4052=r"https://www.instagram.com/p/BaEvAzxlqHq/?taken-by=ekh.94",
          IMG_4019=r"https://www.instagram.com/p/BaBnO2pFR3Q/?taken-by=ekh.94",
          IMG_1295=r"https://www.instagram.com/p/BYsR5JwF4pc/?taken-by=ekh.94",
          IMG_3387=r"https://www.instagram.com/p/BZtS4B1FS2W/?taken-by=ekh.94",
          IMG_3534=r"https://www.instagram.com/p/BaJ-sd8l1ws/?taken-by=ekh.94",
          IMG_3453=r"https://www.instagram.com/p/BaMb2MflrNF/?taken-by=ekh.94",
          IMG_4205=r"https://www.instagram.com/p/BaTzjshl2bC/?taken-by=ekh.94",
          IMG_4293=r"https://www.instagram.com/p/BaltGIHFilr/?taken-by=ekh.94",
          IMG_4182=r"https://www.instagram.com/p/BaWMsHXFPql/?taken-by=ekh.94",
          IMG_4199=r"https://www.instagram.com/p/BaUIyp3F4dn/?taken-by=ekh.94",
          IMG_4950=r"https://www.instagram.com/p/BchWRxrlemH/?taken-by=ekh.94",
          IMG_5766=r"https://www.instagram.com/p/BcSIH3MFjdH/?taken-by=ekh.94",
          IMG_5916=r"https://www.instagram.com/p/BcNNdNvFgaY/?taken-by=ekh.94",
          IMG_6177=r"https://www.instagram.com/p/BcaQ0VtFU-u/?taken-by=ekh.94",
          IMG_6220=r"https://www.instagram.com/p/BccyYa2lf3J/?taken-by=ekh.94",
          IMG_4336=r"https://www.instagram.com/p/BaVzeHDlPdX/?taken-by=ekh.94",
          IMG_3146=r"https://www.instagram.com/p/BZjZFiwlTPL/?taken-by=ekh.94",
          )
    
    #create lists to append meta data
    imgs=[]
    imgs_ds=[]
    heights_ds=[]
    widths_ds=[]
    filenames_ds=[]
    filepaths_ds=[]
    
    #open files and read metadata
    for fp in filepaths:
        fn=fp.split("\\")[-1]
        fn_ds=fn
        imgs.append(get_exif(fp))
        img_ds,width_ds,height_ds=downsample_image(cv2.imread(fp))
        fp_ds="static/img/{}".format(fn_ds)
        cv2.imwrite(fp_ds, img_ds)
        imgs_ds.append(img_ds)
        widths_ds.append(width_ds)
        heights_ds.append(height_ds)
        filenames_ds.append(fn_ds)
        filepaths_ds.append(fp_ds)
    
    #collect data in pandas dataframe
    data=pd.DataFrame(data=imgs)
    data["Height"]=heights_ds
    data["Width"]=widths_ds
    data["Filepath"]=filepaths_ds
    data["Filename"]=filenames_ds
    url_list=[]
    for row in range(len(data)):
        for key in urls.keys():
            if data.loc[row,"Filename"]==key+".jpg":
                url_list.append(urls[key])
    data["Url"]=url_list
    
    #save meta data in json
    data.to_json(r"./meta/img_data.JSON",orient='records')
    