import os
import datetime
import sys



import os
import re
from subprocess import getoutput
import numpy as np
import pandas as pd
from tqdm import tqdm
import time


def filesize_float(filepath):
    '''
    获得文件大小
    Args:
        filepath:

    Returns:

    '''
    return os.path.getsize(filepath) / float(1024 ** 2)

def filesize_to_MB(filepath):
    '''
    获得文件大小的MB单位
    Args:
        filepath:

    Returns:

    '''
    return "%.10f MB" % (os.path.getsize(filepath) / float(1024 ** 2))

def filesize_to_GB(filepath):
    '''
    获得文件大小的GB单位
    Args:
        filepath:

    Returns:

    '''
    return "%.10f GB" % (os.path.getsize(filepath) / float(1024 ** 3))

def filesize_to_TB(filepath):
    '''
    获得文件大小的TB单位
    Args:
        filepath:
    Returns:
    '''
    return "%.10f TB" % (os.path.getsize(filepath) / float(1024 ** 4))

def get_filename(filepath):
    '''
    从路径中获得文件名
    Args:
        filepath:

    Returns:
    '''
    return os.path.splitext(filepath)[-1]

def get_filetype(filepath
                               , types=['.py', 'txt', 'log', 'csv'
                                        ,'docx','doc'
                                        , 'dp' , "pdf",'ipynb',"jpeg"
                                        ,'raw',"jpg" ,'bmp','jpg'
                                        ,'svg','png','tif','gif'
                                        ,'pcx','tga','exif','fpx'
                                        ,'psd','cdr','pcd','dxf'
                                        ,'ufo','eps','ai','WMF'
                                        ,'webp']):
    '''
    从文件名中获得疑似的文件类型
    Args:
        filename: 文件的绝对路径地址
        types: 选择的文件类型

    Returns:

    '''
    file_type =  os.path.splitext(filepath)[-1].split('.')[-1]
    if file_type in types:
        return file_type
    else:
        return False
    
def get_time_stamp_to_time(timestamp):
    """
    把时间戳转化为时间
    """
    time_struct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S',time_struct)
    
def get_access_time(filepath):
    """
    获取访问时间
    """
    return os.path.getatime(filepath)

def get_create_time(filepath):
    """
    获取创建时间
    """
    return os.path.getctime(filepath)

def get_modify_time(filepath):
    """
    获取修改时间
    """
    return os.path.getmtime(filepath)

def floa_time(strptime):
    """
    时间戳转浮点数
    """
    return time.mktime(time.strptime(strptime,'%Y-%m-%d %H:%M:%S'))
    
def sys_file_info():
    '''
    反馈当前层级系统信息
    '''
    date_time_p = datetime.datetime.now().date()
    date_strings = str(date_time_p).replace("-","") 
    os.path.abspath(sys.argv[0])#得到执行文件的绝对路径： 
    dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
    file_path = os.path.join(dirname,filename)
    return date_strings,dirname,filename,file_path

def mkdir_for_jarvis(dir_path):
    '''
    检查文件夹是否存在，如果存在返回路径，如果不存在，递归创建后返回路径
    '''
    if os.path.isdir(dir_path):
        return dir_path
    else:
        os.makedirs(dir_path)
        return dir_path

def toch_for_jarvis(file_path):
    '''
    创建文件
    '''
    if os.path.isfile(file_path):
        return file_path
    else:
        os.mknod(file_path)
        return file_path


def init_paths_for_jarvis(paths):
    '''
    检查文件是否存在，如不存在，则创建之
    '''
    if isinstance(paths,str):
        paths = [paths]
    else:
        pass 
    for path in paths:
        folder_path , file_path = os.path.split(path)
        if os.path.exists(folder_path):
            print("检查文件夹:"+folder_path+"\t已存在")
        else:
            mkdir_for_jarvis(folder_path)
            print("正在创建文件夹:",folder_path)
        if os.path.exists(path):
            print("检查文件:"+path+"\t已存在")
        else:
            toch_for_jarvis(path)
            print("正在创建文件:",path)



if __name__ == '__main__':
    date_strings,dirname,filename,file_path = sys_file_info()
    print("当前系统时间戳:",date_strings
    ,"\n当前运行的文件在",dirname,"文件夹下"
    ,"\n当前运行的文件名是:",filename
    ,"\n当前运行的文件路径在:",file_path)




