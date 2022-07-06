#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   IP_log.py
@Time    :   2020/09/04 13:26:35
@Author  :   ManmanZhang
@Version :   1.0
@Contact :   408903228@qq.com
@Desc    :   None
'''

# here put the import lib
import os
import geoip2.database
import subprocess
import pandas as pd
from tqdm import tqdm
import time
from config import ipv4_query_dataset_from_ipapi,ipv4_query_log_from_ipapi,dataset_path_of_city,headers_of_ipv4_query_log_from_ipapi
from file_manager import init_paths_for_jarvis
init_paths_for_jarvis(ipv4_query_log_from_ipapi)

def getLoc(ip,dataset_path_of_city=dataset_path_of_city):
    '''
    本地数据库ip信息查询
    '''
    try:
        reader = geoip2.database.Reader(dataset_path_of_city)
        ip_object = reader.city(ip)
        #print(ip_object)
        if ip_object == None:
            return  {"ip地址":{}
            ,"国家":{}
            ,"省份":{}
            ,"城市":{}
            ,"纬度":{}
            ,"经度":{}}
        return  {"ip地址":ip_object.traits.ip_address
    ,"国家":ip_object.country.names
    ,"省份":ip_object.subdivisions.most_specific.names
    ,"城市":ip_object.city.names
    ,"纬度":ip_object.location.latitude
    ,"经度":ip_object.location.longitude}
    except Exception as e:
        return {"ip地址":{ip}
            ,"国家":{" not in the database"}
            ,"省份":{" not in the database"}
            ,"城市":{" not in the database"}
            ,"纬度":{" not in the database"}
            ,"经度":{" not in the database"}}


def change_language_logic(info):
    '''
    本地数据库ip信息查询的语言选择逻辑
    '''
    if 'zh-CN' in info:
        return info['zh-CN']
    elif 'en' in info:
        return info['en']
    elif 'es' in info:
        return info['es']
    elif 'fr' in info:
        return info['fr']
    elif 'de' in info:
        return info['de']
    elif 'ru' in info:
        return info['ru']
    elif 'ja' in info:
        return info['ja']
    elif 'pt-BR' in info:
        return info['pt-BR']
    else:
        return None


def getIpv4Info(ipv4):
    '''
    整理本地查询的ip信息
    '''
    #languages = {'pt-BR', 'ru', 'de', 'zh-CN', 'es', 'en', 'fr', 'ja'}
    ip_info = getLoc(ipv4)
    ipv4 = ip_info['ip地址']
    init_countries = change_language_logic(ip_info['国家'])
    init_provinces = change_language_logic(ip_info["省份"])
    init_city = change_language_logic(ip_info["城市"])
    latitude = ip_info['纬度']
    longitude = ip_info['经度']
    return {"countries":init_countries,"provinces":init_provinces
    ,"city":init_city,"latitude":latitude,"longitude":longitude}


def ipv4_query_from_geoip2(ipv4s):
    """
    批量整理ipv4查询数据
    """
    table = {"ipv4":[],"countries_from_geoip2":[],"provinces_from_geoip2":[]
    ,"city_from_geoip2":[],"latitude_from_geoip2":[],"longitude_from_geoip2":[]}
    for ipv4 in tqdm(ipv4s,desc="ip infomation from geoip2.database ……"):
        init_info = getIpv4Info(ipv4)
        table["ipv4"].append(ipv4)
        table["countries_from_geoip2"].append(init_info["countries"])
        table["provinces_from_geoip2"].append(init_info["provinces"])
        table["city_from_geoip2"].append(init_info["city"])
        table["latitude_from_geoip2"].append(init_info["latitude"])
        table["longitude_from_geoip2"].append(init_info["longitude"])
    return table


## TODO: English info for IPv4

from urllib.request import urlopen
import json 

def ipv4_query_from_ipapi(ipv4):
    '''
    网络ip查询函数，数据来自ip-api.com
    '''
    Error_return =  {'status':None,'country':None,'countryCode':None
        ,'region':None,'regionName':None,'city':None,'zip':None
        ,'lat':None,'lon':None,'timezone':None,'isp':None
        ,'org':None,'as':None,'query':ipv4}

    t = 0
   
    try:
        url = "http://ip-api.com/json/"+ipv4
        urlObj = urlopen(url)
        pageContent = urlObj.read().decode('utf-8')
        
        f = open(ipv4_query_log_from_ipapi,"a+")
        dict_data = json.loads(pageContent)
        
        str_data = dict_data.__repr__()+'\n'
        f.write(str_data)
        f.close()
        if dict_data['status'] != 'fail':
            return dict_data
        else:
            return Error_return
    except Exception as e: 
        t += 1
        print("ipv4",ipv4,"error:",e,"t:",t)
        if t < 5:
            return ipv4_query_from_ipapi(ipv4)
        else:
            return Error_return
            

def ipv4s_query_from_ipapi(ipv4s):
    '''
    批量网络ip查询函数
    '''
    ip_query_table = {'status_from_ipapi': [], 'country_from_ipapi': [], 'countryCode_from_ipapi': [], 
    'region_from_ipapi': [], 'regionName_from_ipapi': [], 'city_from_ipapi': [], 'zip_from_ipapi': [],
     'lat_from_ipapi': [], 'lon_from_ipapi': [], 'timezone_from_ipapi': [], 'isp_from_ipapi': []
     , 'org_from_ipapi': [], 'as_from_ipapi': [],'ipv4': []}
     
    for ipv4 in tqdm(ipv4s,desc="ip infomation from ip api ……"):
        time.sleep(1)
        ip_query = ipv4_query_from_ipapi(ipv4)
        #print(ip_query,ipv4)
        ip_query_table['status_from_ipapi'].append(ip_query['status'])
        ip_query_table['country_from_ipapi'].append(ip_query['country'])
        ip_query_table['countryCode_from_ipapi'].append(ip_query['countryCode'])
        ip_query_table['region_from_ipapi'].append(ip_query['region'])
        ip_query_table['regionName_from_ipapi'].append(ip_query['regionName'])
        ip_query_table['city_from_ipapi'].append(ip_query['city'])
        ip_query_table['zip_from_ipapi'].append(ip_query['zip'])
        ip_query_table['lat_from_ipapi'].append(ip_query['lat'])
        ip_query_table['lon_from_ipapi'].append(ip_query['lon'])
        ip_query_table['timezone_from_ipapi'].append(ip_query['timezone'])
        ip_query_table['isp_from_ipapi'].append(ip_query['isp'])
        ip_query_table['org_from_ipapi'].append(ip_query['org'])
        ip_query_table['as_from_ipapi'].append(ip_query['as'])
        ip_query_table['ipv4'].append(ip_query['query'])

    ip_query_table = pd.DataFrame(ip_query_table)

    init_paths_for_jarvis(ipv4_query_dataset_from_ipapi)
    try:
        head_check = open(ipv4_query_dataset_from_ipapi).readlines()[0]
        if headers_of_ipv4_query_log_from_ipapi in head_check:
            ip_query_table.to_csv(ipv4_query_dataset_from_ipapi,mode="a+",header=None)
        else:
            ip_query_table.to_csv(ipv4_query_dataset_from_ipapi,mode="a+")
    except Exception as e:
        ip_query_table.to_csv(ipv4_query_dataset_from_ipapi,mode="a+")

    return ip_query_table


if __name__ == '__main__':  
    print(getLoc("106.55.145.106"))
    print(getIpv4Info("106.55.145.106").keys())
    print(ipv4_query_from_geoip2(["106.55.145.106","106.55.145.106"]))
    print(ipv4_query_from_ipapi('country'))
    print(ipv4s_query_from_ipapi(['country',"36.59.54.237","106.55.145.106"]))