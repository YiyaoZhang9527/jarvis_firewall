from config import servers_info,generator_keys_shell_path,download_file_path,login_file_path,cmd_table_path
import pandas as pd
from file_manager import init_paths_for_jarvis
from os import sep
#import file_manager
#date_strings,project_path,filename,file_path = file_manager.sys_file_info()
#print(date_strings,project_path,filename,file_path)
init_paths_for_jarvis(generator_keys_shell_path) 
init_paths_for_jarvis(download_file_path)
init_paths_for_jarvis(login_file_path)
init_paths_for_jarvis(cmd_table_path)

def creat_last_log_path():
    '''
    last日志存储路径
    '''
    project_path = servers_info["project_path"]
    server_last_data_folder = "{}{}{}{}".format(project_path,sep,"log_data_folder",sep)
    server_last_datas = ["{}{}{}".format(server_last_data_folder,server_name,"lastlog.log") for server_name in servers_info["server_info"].keys()]
    return project_path,server_last_data_folder,server_last_datas

def creat_lastb_log_path():
    '''
    lastb日志存储路径
    '''
    project_path = servers_info["project_path"]
    server_lastb_data_folder = "{}{}{}{}".format(project_path,sep,"log_data_folder",sep)
    server_lastb_datas = ["{}{}{}".format(server_lastb_data_folder,server_name,"lastblog.log") for server_name in servers_info["server_info"].keys()]
    return project_path,server_lastb_data_folder,server_lastb_datas


def generator_last_shell():
    '''
    
    '''
    cmd_dict = {
        #"server_info":[],
        "server_name":[]
        ,"HostName":[]
        ,"User":[]
        ,"Port":[]
        ,"IdentityFile":[]
        ,"ssh_rsakey_cmd":[]
        ,"send_key_to_server_cmd":[]
        ,"ssh_login_cmd":[]
        ,"downlod_lsat_cmd":[]
        ,"downlod_lsatb_cmd":[]
        ,"downlod_secure_cmd":[]
        #,"last_log_path":[]
        #,"lastb_log_path":[]
        #,"downlod_secure_cmd":[]
        }
    project_path,server_lastb_data_folder,server_lastb_datas = creat_lastb_log_path()
    #print("server_lastb_data_folder:",server_lastb_data_folder)
    servers_info_ = servers_info["server_info"]

    for server_name,info in servers_info_.items():

        server_info = servers_info_[server_name]
        HostName = server_info["HostName"]
        User = server_info["User"]
        Port = server_info["Port"]
        IdentityFile = server_info["IdentityFile"]
        
        last_log_path = "{}{}{}".format(server_lastb_data_folder,server_name,'_last_`date +%Y%m%d`.log')
        lastb_log_path = "{}{}{}".format(server_lastb_data_folder,server_name,'_lastb_`date +%Y%m%d`.log')
        secure_log_path = "{}{}{}".format(server_lastb_data_folder,server_name,'_secure_log_`date +%Y%m%d`.secure')


        ssh_rsakey_cmd = "{}{}{}{}{}".format("ssh-keygen -t rsa -C ",server_name," -f ",IdentityFile," -b8192")
        send_key_to_server_cmd = "{}{}{}{}{}{}{}{}{}".format("cat ",IdentityFile,".pub | ssh ",User,"@",HostName," -p",Port," tee ~/.ssh/authorized_keys")
        ssh_login_cmd = "{}{}{}{}{}{}{}{}".format("ssh -i ",IdentityFile," ",User,"@",HostName," -p",Port)
        downlod_lsat_cmd = "{}{}{}".format(ssh_login_cmd,' "last" >> ',last_log_path)
        downlod_lsatb_cmd = "{}{}{}".format(ssh_login_cmd,' "lastb" >> ',lastb_log_path)
        downlod_secure_cmd = "{}{}{}".format(ssh_login_cmd,' "cat /var/log/secure" >> ',secure_log_path)
        
        #downlod_lsat_cmd = "{}{}{}{}{}".format('ssh ',server_name,' "last" >> ',server_name,'_last_`date +%Y%m%d%H`.log')
        #downlod_lsatb_cmd = "{}{}{}{}{}".format('ssh ',server_name,' "lastb" >> ',server_name,'_lastb_`date +%Y%m%d%H`.log')
        #downlod_secure_cmd = "{}{}{}{}{}".format('ssh ',server_name,' "cat /var/log/secure" >> ',server_name,'_secure_log.secure')
        #cmd_dict["server_info"].append(server_info)

        cmd_dict["server_name"].append(server_name)
        cmd_dict["HostName"].append(HostName)
        cmd_dict["User"].append(User)
        cmd_dict["Port"].append(Port)
        cmd_dict["IdentityFile"].append(IdentityFile)
        cmd_dict["ssh_rsakey_cmd"].append(ssh_rsakey_cmd)
        cmd_dict["send_key_to_server_cmd"].append(send_key_to_server_cmd)
        cmd_dict["ssh_login_cmd"].append(ssh_login_cmd)
        cmd_dict["downlod_lsat_cmd"].append(downlod_lsat_cmd)
        cmd_dict["downlod_lsatb_cmd"].append(downlod_lsatb_cmd)
        cmd_dict["downlod_secure_cmd"].append(downlod_secure_cmd)
        #cmd_dict["last_log_path"].append(last_log_path)
        #cmd_dict["lastb_log_path"].append(lastb_log_path)
        #cmd_dict["downlod_secure_cmd"].append(downlod_secure_cmd)

        '''
        print(server_name)
        print(ssh_rsakey_cmd)
        print(send_key_to_server_cmd)
        print(ssh_login_cmd)
        print(downlod_lsat_cmd)
        print(downlod_lsatb_cmd)
        print(downlod_secure_cmd)
        print("\n")
        '''
    #print(cmd_dict)
    df = pd.DataFrame(cmd_dict)
    generator_keys = open(generator_keys_shell_path,'w+')
    download_file = open(download_file_path ,"w+")
    login_file = open(login_file_path,"w+")
    for shell_name in df.columns:
        if "cmd" in shell_name:
            for cmd in df[shell_name]:
                if "ssh -i ~/.ssh/" in cmd:
                    if ">>" in cmd:
                        #print(cmd)
                        generator_keys.write(cmd+'\n')
                    else:
                        login_file.write(cmd+'\n')
                else:
                    download_file.write(cmd+'\n')
    generator_keys.close()
    download_file.close()
    login_file.close()

    df.to_csv(cmd_table_path)
    return df

if __name__ == '__main__':
    creat_last_log_path()
    creat_lastb_log_path()
    generator_last_shell()
   
