ssh -i ~/.ssh/HuaweiJumpServer9PC root@121.36.197.197 -p22 "last" >> /home/zhangmanman/jarvis_firewall/log_data_folder/HuaweiJumpServer_last_`date +%Y%m%d`.log
ssh -i ~/.ssh/AliCrawlerServer9PC root@47.114.143.177 -p22 "last" >> /home/zhangmanman/jarvis_firewall/log_data_folder/AliCrawlerServer_last_`date +%Y%m%d`.log
ssh -i ~/.ssh/TencentServer5M9PC root@81.70.149.204 -p22 "last" >> /home/zhangmanman/jarvis_firewall/log_data_folder/TencentServer5M_last_`date +%Y%m%d`.log
ssh -i ~/.ssh/TencentServer1M9PC root@82.156.122.38 -p22 "last" >> /home/zhangmanman/jarvis_firewall/log_data_folder/TencentServer1M_last_`date +%Y%m%d`.log
ssh -i ~/.ssh/TencentNetworkServer5M9PC root@118.195.231.139 -p22 "last" >> /home/zhangmanman/jarvis_firewall/log_data_folder/TencentNetworkServer5M_last_`date +%Y%m%d`.log
ssh -i ~/.ssh/HuaweiJumpServer9PC root@121.36.197.197 -p22 "lastb" >> /home/zhangmanman/jarvis_firewall/log_data_folder/HuaweiJumpServer_lastb_`date +%Y%m%d`.log
ssh -i ~/.ssh/AliCrawlerServer9PC root@47.114.143.177 -p22 "lastb" >> /home/zhangmanman/jarvis_firewall/log_data_folder/AliCrawlerServer_lastb_`date +%Y%m%d`.log
ssh -i ~/.ssh/TencentServer5M9PC root@81.70.149.204 -p22 "lastb" >> /home/zhangmanman/jarvis_firewall/log_data_folder/TencentServer5M_lastb_`date +%Y%m%d`.log
ssh -i ~/.ssh/TencentServer1M9PC root@82.156.122.38 -p22 "lastb" >> /home/zhangmanman/jarvis_firewall/log_data_folder/TencentServer1M_lastb_`date +%Y%m%d`.log
ssh -i ~/.ssh/TencentNetworkServer5M9PC root@118.195.231.139 -p22 "lastb" >> /home/zhangmanman/jarvis_firewall/log_data_folder/TencentNetworkServer5M_lastb_`date +%Y%m%d`.log
ssh -i ~/.ssh/HuaweiJumpServer9PC root@121.36.197.197 -p22 "cat /var/log/secure" >> /home/zhangmanman/jarvis_firewall/log_data_folder/HuaweiJumpServer_secure_log_`date +%Y%m%d`.secure
ssh -i ~/.ssh/AliCrawlerServer9PC root@47.114.143.177 -p22 "cat /var/log/secure" >> /home/zhangmanman/jarvis_firewall/log_data_folder/AliCrawlerServer_secure_log_`date +%Y%m%d`.secure
ssh -i ~/.ssh/TencentServer5M9PC root@81.70.149.204 -p22 "cat /var/log/secure" >> /home/zhangmanman/jarvis_firewall/log_data_folder/TencentServer5M_secure_log_`date +%Y%m%d`.secure
ssh -i ~/.ssh/TencentServer1M9PC root@82.156.122.38 -p22 "cat /var/log/secure" >> /home/zhangmanman/jarvis_firewall/log_data_folder/TencentServer1M_secure_log_`date +%Y%m%d`.secure
ssh -i ~/.ssh/TencentNetworkServer5M9PC root@118.195.231.139 -p22 "cat /var/log/secure" >> /home/zhangmanman/jarvis_firewall/log_data_folder/TencentNetworkServer5M_secure_log_`date +%Y%m%d`.secure
