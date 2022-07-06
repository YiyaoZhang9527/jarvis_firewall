import os
import file_manager
date_strings,project_path,filename,file_path = file_manager.sys_file_info()

jarvis_firewall_path = "~/jarvis_firewall/"
# TODO : 基础软件数据路径
log_dir = os.path.expanduser("{}{}{}".format(jarvis_firewall_path,"basic_historical_data_folder",os.sep))
ipv4_query_dataset_from_ipapi = os.path.expanduser("{}{}".format(log_dir,"ipv4_query_history_from_ipapi.csv"))
ipv4_query_log_from_ipapi = os.path.expanduser("{}{}".format(log_dir,"ipv4_query_history_from_ipapi.log"))
last_and_lastb_history = os.path.expanduser("{}{}".format(log_dir,'last_and_lastb_history.csv'))

# TODO : shell 和 data 文件命令
shell_dir = os.path.expanduser("{}{}{}".format(jarvis_firewall_path,"log_data_folder",os.sep))
generator_keys_shell_path = os.path.expanduser("{}{}".format(shell_dir,"generator_keys.sh"))
download_file_path = os.path.expanduser("{}{}".format(shell_dir,"download_shell.sh"))
login_file_path = os.path.expanduser("{}{}".format(shell_dir,"login_shell.sh"))
#ipv4s_query_history_from_ipapi = os.path.expanduser("{}{}".format(shell_dir,"ipv4s_query_from_ipapi.csv"))

# TODO : 服务器信息表
cmd_table_path = os.path.expanduser("{}{}".format(shell_dir,"cmd_table.csv"))

# TODO : 目标服务器信息配置

servers_info = {
    "project_path":project_path
    ,"server_info":{
        "HuaweiJumpServer":{
            "HostName":"121.36.197.197",
            "User":"root",
            "Port":"22",
            "IdentityFile":"~/.ssh/HuaweiJumpServer9PC"
        },
        "AliCrawlerServer":{
            "HostName":"47.114.143.177",
            "User":"root",
            "Port":"22",
            "IdentityFile":"~/.ssh/AliCrawlerServer9PC"
        },
        "TencentServer5M":{
            "HostName":"81.70.149.204",
            "User":"root",
            "Port":"22",
            "IdentityFile":"~/.ssh/TencentServer5M9PC"
        },
        "TencentServer1M":{
            "HostName":"82.156.122.38",
            "User":"root",
            "Port":"22",
            "IdentityFile":"~/.ssh/TencentServer1M9PC"
        },
        "TencentNetworkServer5M":{
            "HostName":"118.195.231.139",
            "User":"root",
            "Port":"22",
            "IdentityFile":"~/.ssh/TencentNetworkServer5M9PC"
        }
    }     
}

# TODO : 本地ip信息数据库位置
dataset_path_of_city = os.path.expanduser("~/GeoLite2-City_20200901/GeoLite2-City.mmdb")

# TODO : 表头
headers_of_last_and_lastb_history = ",userName,connectionMethod,ipv4,ipv4First,ipv4Second,ipv4Third,ipv4Fourth,week,months,date,startTime,endTime,keepTime,intranetIP,extranetIP,serverName,fileDate,fileType"
headers_of_ipv4_query_log_from_ipapi = """,userName, connectionMethod, ipv4, ipv4First, ipv4Second,
       ipv4Third, ipv4Fourth, week, months, date, startTime,
       endTime, keepTime, intranetIP, extranetIP, serverName,
       fileDate, fileType, countries_from_geoip2,
       provinces_from_geoip2, city_from_geoip2, latitude_from_geoip2,
       longitude_from_geoip2, status_from_ipapi, country_from_ipapi,
       countryCode_from_ipapi, region_from_ipapi, regionName_from_ipapi,
       city_from_ipapi, zip_from_ipapi, lat_from_ipapi, lon_from_ipapi,
       timezone_from_ipapi, isp_from_ipapi, org_from_ipapi,
       as_from_ipapi"""

headers_of_ipv4_history = ",ipv4,countries_from_geoip2,provinces_from_geoip2,city_from_geoip2,latitude_from_geoip2,longitude_from_geoip2,status_from_ipapi,country_from_ipapi,countryCode_from_ipapi,region_from_ipapi,regionName_from_ipapi,city_from_ipapi,zip_from_ipapi,lat_from_ipapi,lon_from_ipapi,timezone_from_ipapi,isp_from_ipapi,org_from_ipapi,as_from_ipapi"
if __name__ == '__main__':
    print("程序日志文件夹路径",log_dir,
    "\nipapi网站ip信息查询历史数据集",ipv4_query_dataset_from_ipapi,
    "\nipapu网站ip信息查询历史日志",ipv4_query_log_from_ipapi,
    "\n当前系统运行信息为:",file_manager.sys_file_info())