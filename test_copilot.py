from asyncio import subprocess
import re

def make_sure_ipv4_is_a_string(ipv4):
    """
    Makes sure the IP address is a string.
    """
    if type(ipv4) == str:
        return ipv4
    else:
        return str(ipv4)

def check_ipv4(ip_addr):
    """
    Checks if the IP address is valid.
    """
    if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip_addr):
        return True
    else:
        return False

def check_if_is_an_intranet_address(ip_addr):
    """
    Checks if the IP address is an intranet address.
    """
    if re.match(r"^(127|192\.168|10\.|172\.(1[6-9]|2[0-9]|3[0-1]))\.", ip_addr):
        return True
    else:
        return False


def check_if_is_an_extranet_address(ip_addr):
    """
    Checks if the IP address is an intranet address.
    """
    if re.match(r"^(?!(10|127|192\.168|172\.(1[6-9]|2[0-9]|3[0-1])))\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip_addr):
        return True
    else:
        return False

#检查IP地址是否合法
def check_ip_addr(ip_addr):
    """
    Checks if the IP address is valid.
    """
    if check_ipv4(ip_addr):
        if check_if_is_an_intranet_address(ip_addr):
            return "intranet"
        elif check_if_is_an_extranet_address(ip_addr):
            return "extranet"
        else:
            return "private"
    else:
        return "invalid"


#检查当前系统代理是否打开
def check_proxy_status():
    return subprocess.check_output("env|grep -i proxy", shell=True)


def Regular_extraction_of_mobile_phone_numbers(string):
    """
    Regular extraction of mobile phone numbers.
    """
    return re.findall(r"1[345789]\d{9}", string)


def Regular_extraction_of_email_addresses(string):
    """
    Regular extraction of email addresses.
    """
    return re.findall(r"[\w\.-]+@[\w\.-]+", string)

def Regular_extraction_of_ipv4_addresses(string):
    """
    Regular extraction of ip addresses.
    """
    return re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", string)

def Regular_extraction_of_urls(string):
    """
    Regular extraction of urls from chinese.
    """
    return re.findall(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", string)

def Regular_extraction_of_chinese(string):
    """
    Regular extraction of chinese.
    """
    return re.findall(r"[\u4e00-\u9fa5]+", string)

def Regular_extraction_of_chinese_and_english(string):
    """
    Regular extraction of chinese and english.
    """
    return re.findall(r"[\u4e00-\u9fa5]+|[a-zA-Z]+", string)

def Regular_extraction_of_chinese_and_english_and_number(string):
    """
    Regular extraction of chinese and english and number.
    """
    return re.findall(r"[\u4e00-\u9fa5]+|[a-zA-Z]+|[0-9]+", string)

def Regular_extraction_of_english(string):
    """
    Regular extraction of english.
    """
    return re.findall(r"[a-zA-Z]+", string)

def Regular_extraction_of_number(string):
    """
    Regular extraction of number.
    """
    return re.findall(r"[0-9]+", string)

def Regular_extraction_of_Russian(string):
    """
    Regular extraction of Russian.
    """
    return re.findall(r"[А-Яа-я]+", string)

def Regular_extraction_of_Japanese(string):
    """
    Regular extraction of Japanese.
    """
    return re.findall(r"[ぁ-ん]+", string)

def Regular_extraction_of_Korean(string):
    """
    Regular extraction of Korean.
    """
    return re.findall(r"[가-힣]+", string)

def Regular_extraction_of_Arabic(string):
    """
    Regular extraction of Arabic.
    """
    return re.findall(r"[أ-ي]+", string)

def Regular_extraction_of_Thai(string):
    """
    Regular extraction of Thai.
    """
    return re.findall(r"[ก-๙]+", string)

def Regular_extraction_of_Vietnamese(string):
    """
    Regular extraction of Vietnamese.
    """
    return re.findall(r"[ạ-ỹ]+", string)

def Regular_extraction_of_French(string):
    """
    Regular extraction of French.
    """
    return re.findall(r"[à-ÿ]+", string)

def Regular_extraction_of_German(string):
    """
    Regular extraction of German.
    """
    return re.findall(r"[ä-ü]+", string)

def Regular_extraction_of_Spanish(string):
    """
    Regular extraction of Spanish.
    """
    return re.findall(r"[á-ú]+", string)

def Regular_extraction_of_Italian(string):
    """
    Regular extraction of Italian.
    """
    return re.findall(r"[à-ù]+", string)

def Regular_extraction_of_Portuguese(string):
    """
    Regular extraction of Portuguese.
    """
    return re.findall(r"[ã-õ]+", string)


def Regular_extraction_of_ipv6_addresses(string):
    """
    Regular extraction of ipv6 addresses.
    """
    return re.findall(r"\b(?:[0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4}\b", string)

def Regular_extraction_of_identity_card(string):
    """
    Regular extraction of identity card.
    """
    return re.findall(r"\d{17}[\d|x|X]|\d{15}", string)


def Regular_extraction_of_identity_card(string):
    """
    Regular extraction of identity card.
    """
    return re.findall(r"\d{15}|\d{18}", string)






print(Regular_extraction_of_mobile_phone_numbers("这是一个手机号码13865548523"))
print(Regular_extraction_of_email_addresses("这是一个邮箱地址))408903228@qq.com"))
print(Regular_extraction_of_ipv4_addresses("这是一个IP地址114.114.116.113hahahaha"))
print(Regular_extraction_of_urls("这是一个网址https://www.runoob.com/cprogramming/c-data-types.html章京东"))
print(Regular_extraction_of_chinese("zaskdjwskladhjash中哦ingguo深刻安康的发送asjkldjasd"))
print(Regular_extraction_of_identity_card("这是一个身份证号码3206811991212121223123123"))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
