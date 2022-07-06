
import os
from sys import float_repr_style
from typing import Counter
from ast import literal_eval
from numpy.lib.shape_base import split
from pandas.core.frame import DataFrame
from regular_expression_ip import regex_ipv4 ,regex_ipv6,regex_space,regex_ip_intr_extr,regex_legit_ip
import pandas as pd
from ip_information_query_tools import ipv4_query_from_geoip2,ipv4_query_from_ipapi,ipv4s_query_from_ipapi
from tqdm import tqdm
import numpy as np
from file_manager import sys_file_info
date_p,dirname,filename,file_path = sys_file_info()
import shell_generator
shell_generator.generator_last_shell()
from config import generator_keys_shell_path,download_file_path,login_file_path,last_and_lastb_history,headers_of_ipv4_query_log_from_ipapi
import subprocess
from config import ipv4_query_log_from_ipapi,ipv4_query_dataset_from_ipapi,cmd_table_path
from config import headers_of_ipv4_history ,headers_of_ipv4_query_log_from_ipapi ,headers_of_last_and_lastb_history
from shell_generator import creat_last_log_path,creat_lastb_log_path
project_path,server_lastb_data_folder,server_lastb_datas = creat_lastb_log_path()
project_path,server_last_data_folder,server_last_datas = creat_last_log_path()
pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)
from file_manager import filesize_float


def run_cmd(shell_path):
    shell_data = open(shell_path,'r').readlines()
    for cmd in shell_data:
        print("cmd:",cmd)
        action = subprocess.getoutput(cmd)
        print("\n",action)

def download_log_from_servers():
    run_cmd(generator_keys_shell_path)

def load_files(file_paths):
    '''
    读取文件
    '''
    return { dirname :open(path,'r').readlines() for path in file_paths }

def Merge(dict1, dict2): 
    '''
    合并字典
    '''
    res = {**dict1, **dict2} 
    return res 





def init_last_log(path):
    result = []
    counter = {}
    t = -1
    log = open(path,"r").readlines()
    for row in log:
        t += 1
        split_row = regex_space(row.replace('\n',""))
        len_ = len(split_row)
        if (t !=0)  and (t != (len(log)-1)):
            next_row = regex_space(log[t+1])
            last_row = regex_space(log[t-1])
        if len_ not in [0,7]:
            pass
        if len_ == 10:
            split_row = split_row
            result.append(split_row)
        elif (len_ == 1) and (len(next_row) == 9):
            split_row = split_row+next_row
            result.append(split_row)
        elif (len_== 9) and (len(last_row) > 1):
            split_row = ["user_empty_tag"]+split_row
            result.append(split_row)
        if len_ not in counter:
            counter.update({len_:[t]})
        else:
            counter[len_].append(t)
    return result,counter







def last_data_clearning(path):
    '''
    读取last日志文件并清洗整理
    '''
    log,counter = init_last_log(path)
    file_name = file_path.split(os.sep)[-1]
    server_name = file_name.split("_")[0]
    result = {"userName":[],"connectionMethod":[]
    ,"ipv4":[],"ipv4First":[],"ipv4Second":[]
    ,"ipv4Third":[],"ipv4Fourth":[]
    ,"week":[],"months":[]
    ,"date":[],"startTime":[],"endTime":[],"keepTime":[]
    ,"intranetIP":[],"extranetIP":[]
    ,"serverName":[],"fileDate":[],"fileType":[]}

    file_name = path.split(os.sep)[-1]
    file_name_split = file_name.split('_')
    server_name = file_name_split[0]
    file_type = file_name_split[1]
    file_date = file_name_split[2]

    for split_row in tqdm(log,desc="文件数据清理中:"+file_name):
        try:
            user_name = split_row[0]
            connection_method = split_row[1]
            ipv4 = split_row[2]

            if regex_legit_ip(ipv4):
                ipv4_split = ipv4.split('.')
                ipv4_first = ipv4_split[0]
                ipv4_second = ipv4_split[1]
                ipv4_third= ipv4_split[2]
                ipv4_fourth = ipv4_split[3]
            else:
                ipv4_first = None
                ipv4_second = None
                ipv4_third= None
                ipv4_fourth = None

            week= split_row[3]
            months = split_row[4]
            date = split_row[5]
            start_time = split_row[6]
            end_time = split_row[8]
            keep_time = split_row[9]
            
            intr_or_extr = regex_ip_intr_extr([ipv4])
            if intr_or_extr["extranet_ips"]:
                result["intranetIP"].append(1)
                result["extranetIP"].append(0)
            else:
                result["extranetIP"].append(1)
                result["intranetIP"].append(0)
            result["ipv4First"].append(ipv4_first)
            result["ipv4Second"].append(ipv4_second)
            result["ipv4Third"].append(ipv4_third)
            result["ipv4Fourth"].append(ipv4_fourth)
            result["userName"].append(user_name)
            result["connectionMethod"].append(connection_method)
            result["ipv4"].append(ipv4)
            result["week"].append(week)
            result["months"].append(months)
            result["date"].append(date)
            result["startTime"].append(start_time)
            result["endTime"].append(end_time)
            result["keepTime"].append(keep_time)
            result["serverName"].append(server_name)
            result["fileType"].append(file_type)
            result["fileDate"].append(file_date)
                
        except Exception as e:
            print(e,split_row)

    return result

def check_header(file_path,headers):
    if os.path.isfile(file_path):
        open_file = open(file_path,'r').readlines()
        try:
            if len(open_file) > 0:
                pass
            else:
                f = open(file_path,'w')
                f.write(headers +'\n')
                f.close()
            check_file = open_file[0].replace("\n","")
            if headers != check_file:
                with open(file_path, 'r+') as f:
                    content = f.read()        
                    f.seek(0, 0)
                    f.write(headers +'\n'+content)
            else:
                pass
        except Exception as e:
            if e == IndexError:
                f = open(file_path,'w')
                f.write(headers +'\n')
                f.close()
    else:
        f = open(file_path,'w')
        f.write(headers +'\n')
        f.close()

def Merge_ipv4_query(ipv4s):
    histroy_data_set = "ipv4_info_dataset.csv"
    last_log_ipv4s_tmp = set(ipv4s)
    check_header(histroy_data_set,headers_of_ipv4_history)
    databases = pd.read_csv(histroy_data_set,error_bad_lines=False) #)
    databases = databases.drop(columns=["Unnamed: 0"])
    databases = databases.reset_index(drop=True)
    databases.to_csv(histroy_data_set)
    print(databases)
    if len(last_log_ipv4s_tmp) > 0:
        last_log_ipv4s = []
        query_history = []
        for ipv4 in last_log_ipv4s_tmp:
            if ipv4 in set(databases.ipv4):
                query_history.append(ipv4)
            else:
                last_log_ipv4s.append(ipv4)

        lenght_of_query , lenght_of_history = len(last_log_ipv4s),len(query_history)
        if lenght_of_query > 0: 
            ipv4_query_from_geoip2_ = pd.DataFrame(ipv4_query_from_geoip2(last_log_ipv4s))
            ipv4s_query_from_ipapi_ = ipv4s_query_from_ipapi(last_log_ipv4s)
            merge_query = pd.merge(ipv4_query_from_geoip2_,ipv4s_query_from_ipapi_,how='outer',on='ipv4')
            merge_query.to_csv(histroy_data_set,header=None,mode="a+")
        if lenght_of_history > 0:
            ipv4_index = pd.DataFrame({"ipv4":query_history}).ipv4
            check_table = databases[databases['ipv4'].isin(ipv4_index)]
            check_table = check_table[databases["status_from_ipapi"]=="success"]
        if lenght_of_history > 0 and lenght_of_query > 0:
            Merge_query = pd.merge(merge_query,check_table,how='outer',on='ipv4')
            Merge_query.drop(columns=["Unnamed: 0"])
        elif lenght_of_history > 0 and lenght_of_query == 0:
            Merge_query = check_table
        elif lenght_of_query > 0 and lenght_of_history == 0:
            Merge_query = merge_query
    Merge_table = Merge_query.drop_duplicates(['ipv4'], keep='last')
    return Merge_table
    

def init_last_path(date=date_p):
    '''
    '''
    result = {}
    
    for name in os.listdir(server_last_data_folder):
        if "last" in name and ".log" in name and str(date) in name:
            result.update({name:"{}{}".format(server_last_data_folder,name)})
    return result #{name:"{}{}".format(server_last_data_folder,name) for name in os.listdir(server_last_data_folder) }#if ("_last" in name) and  (".log" in name) and  (str(date) in name)}

def Query_last(date_=date_p):
    logs_path = init_last_path(date_)
    for name,path in logs_path.items():
        filesize = filesize_float(path)
        if filesize:
            print("\tfilesize:",filesize)
            data_clearning = pd.DataFrame(last_data_clearning(path))
            
            ipv4s = list(data_clearning.ipv4)
            server_ipv4_query = Merge_ipv4_query(ipv4s)
            ssh_last_info_table = pd.merge(data_clearning,server_ipv4_query, how="outer", on="ipv4")
            ssh_last_info_table.to_csv(last_and_lastb_history,mode="w+")
        
    
    load_tmp = pd.read_csv(last_and_lastb_history)
    tmp_index = load_tmp[load_tmp.userName=="userName"]
    drop_1= load_tmp.drop(tmp_index.index)
    re_index = drop_1.reset_index(drop=True)
    drop_2 = re_index.drop(columns=["Unnamed: 0"])
    drop_2.to_csv("ssh_last_info_table.csv",mode="a+")
    
    
    




if __name__ == '__main__':
    #print(check_ipv4_history(['122,97,179,132','country',"36.59.54.237","106.55.145.106"]))
    
    (init_last_log("/home/zhangmanman/jarvis_firewall/log_data_folder/TencentServer5M_lastb_20210515.log"))
    #pass
    #print(Merge_ipv4_query(['country',"36.59.54.237","106.55.145.106"]))
    #download_log_from_servers()
    print(init_last_path())
    print(Query_last(20210517))




    