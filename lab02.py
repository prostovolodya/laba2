#!/usr/bin/python
from spyre import server

import pandas as pd
import urllib2
import json
from numpy import *
import matplotlib.pyplot as plt
import math
import pylab
from matplotlib import mlab
from frame import *
import matplotlib.pyplot as plt

area = ["Cherkasy","Chernihiv","Chernivci","Crimea","Dnipropetrovs'k","Donets'k","Ivano-Frankivs'k","Kharkiv","Kherson",
        "Khmel'nyts'kyy","Kiev","Kiev City","Kirovohrad","Luhans'k"," L'viv","Mykolayiv","Odessa","Poltava"," Rivne",
        "Sevastopol'","Sumy","Ternopil'","Transcarpathia","Vinnytsya","Volyn","Zaporizhzhya","Zhytomyr"]

areaNumber=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21',
            '22','23','24','25','26','27']

Index = ['VCI','TCI','VHI']

df = pd.read_csv('provinces/vhi_id_15.csv',index_col=False, header=1)
w=df[df['year']==1981]
print w
class DataAnalyze(server.App):
    title = "Analyze Ukraine drought"

    inputs = [{     "input_type":'dropdown',
                    "label": 'Area ',
                    "options" : [ {"label": area[0], "value":areaNumber[0]},
                                  {"label": area[1], "value":areaNumber[1]},
                                  {"label": area[2], "value":areaNumber[2]},
                                  {"label": area[3], "value":areaNumber[3]},
                                  {"label": area[4], "value":areaNumber[4]},
                                  {"label": area[5], "value":areaNumber[5]},
                                  {"label": area[6], "value":areaNumber[6]},
                                  {"label": area[7], "value":areaNumber[7]},
                                  {"label": area[8], "value":areaNumber[8]},
                                  {"label": area[9], "value":areaNumber[9]},
                                  {"label": area[10], "value":areaNumber[10]},
                                  {"label": area[11], "value":areaNumber[11]},
                                  {"label": area[12], "value":areaNumber[12]},
                                  {"label": area[13], "value":areaNumber[13]},
                                  {"label": area[14], "value":areaNumber[14]},
                                  {"label": area[15], "value":areaNumber[15]},
                                  {"label": area[16], "value":areaNumber[16]},
                                  {"label": area[17], "value":areaNumber[17]},
                                  {"label": area[18], "value":areaNumber[18]},
                                  {"label": area[19], "value":areaNumber[19]},
                                  {"label": area[20], "value":areaNumber[20]},
                                  {"label": area[21], "value":areaNumber[21]},
                                  {"label": area[22], "value":areaNumber[22]},
                                  {"label": area[23], "value":areaNumber[23]},
                                  {"label": area[24], "value":areaNumber[24]},
                                  {"label": area[25], "value":areaNumber[25]},
                                  {"label": area[26], "value":areaNumber[26]},
                                 ],
                    "variable_name": 'ticker',
                    "action_id": "update_data",

              }



        ,{ "input_type":"text",
            "variable_name":"min",
            "label": "MIN week",
            "value":4,
            "action_id":"update_data"},
        { "input_type":"text",
            "variable_name":"max",
            "label": "MAX week",
            "value":6,
            "action_id":"update_data"}
          ,

              {     "input_type":'dropdown',
                    "label": 'Filter area for plot',
                    "options" : [ {"label": area[0], "value":areaNumber[0]},
                                  {"label": area[1], "value":areaNumber[1]},
                                  {"label": area[2], "value":areaNumber[2]},
                                  {"label": area[3], "value":areaNumber[3]},
                                  {"label": area[4], "value":areaNumber[4]},
                                  {"label": area[5], "value":areaNumber[5]},
                                  {"label": area[6], "value":areaNumber[6]},
                                  {"label": area[7], "value":areaNumber[7]},
                                  {"label": area[8], "value":areaNumber[8]},
                                  {"label": area[9], "value":areaNumber[9]},
                                  {"label": area[10], "value":areaNumber[10]},
                                  {"label": area[11], "value":areaNumber[11]},
                                  {"label": area[12], "value":areaNumber[12]},
                                  {"label": area[13], "value":areaNumber[13]},
                                  {"label": area[14], "value":areaNumber[14]},
                                  {"label": area[15], "value":areaNumber[15]},
                                  {"label": area[16], "value":areaNumber[16]},
                                  {"label": area[17], "value":areaNumber[17]},
                                  {"label": area[18], "value":areaNumber[18]},
                                  {"label": area[19], "value":areaNumber[19]},
                                  {"label": area[20], "value":areaNumber[20]},
                                  {"label": area[21], "value":areaNumber[21]},
                                  {"label": area[22], "value":areaNumber[22]},
                                  {"label": area[23], "value":areaNumber[23]},
                                  {"label": area[24], "value":areaNumber[24]},
                                  {"label": area[25], "value":areaNumber[25]},
                                  {"label": area[26], "value":areaNumber[26]},
                                 ],
                    "variable_name": 'ticker3',
                    "action_id": "plot",


              }
,
        { "input_type":"text",
            "variable_name":"year",
            "label": "year",
            "value":1981,
            "action_id":"plot"}
        ,

              {     "input_type":'dropdown',
                    "label": 'Index',
                    "options" : [ {"label": "vci", "value":Index[0]},
                                  {"label": "tci", "value":Index[1]},
                                  {"label": "vhi", "value":Index[2]}],
                    "variable_name": 'ticke',
                    "action_id": "plot" }
        ]

    tabs = ["Plot", "Table"]
    outputs = [
                {    "output_type" : "plot",
                    "output_id" : "plot",
                    "control_id" : "update_data",
                    "tab" : "Plot",  # must specify which tab each output should live in
                    "on_page_load" : True },
                {   "output_type" : "table",
                    "output_id" : "update_data",
                    "control_id" : "update_data",
                    "tab" : "Table",
                    "on_page_load" : True }]

    def getData(self, params):
        ticker = str(params['ticker'])

        max = float(params['max'])
        min = float(params['min'])
        df = pd.read_csv('provinces/vhi_id_%s.csv'%ticker,index_col=False, header=1)
        a = df[df["week"]<=max ]
        b=a[df["week"]>=min]
        c = b[df['year']!=0]
        z=c[df['VHI']!=-1]
        z
        return z
    def getPlot(self, params):
        ticke= str(params['ticke'])
        ticker3 = str(params['ticker3'])
        year = float(params['year'])
        df = pd.read_csv('provinces/vhi_id_%s.csv'%ticker3,index_col=False, header=1)
        if year!=0:
            w=df[df['year']==year]
        else:
            w=df
        x=w[[ticke]]
        y =w['week']
        plt = x.plot(y)
        fig = plt.get_figure()
        return fig
app = DataAnalyze()
app.launch(port=9094)