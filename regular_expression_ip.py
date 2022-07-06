import re

def regex_ipv4(string,display=False):
    """
    example:
        string_ipv4 = "is this 236.168.192.1 ip 12321"
        print(regex_ipv6(string_ipv4))
    """
    result = re.findall(r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b", string) 
    if result:
        return result
    else:
        if display:
            print("re cannot find ip")


def regex_ipv6(string,display=False):
    """
    example:
        string_IPv6="1050:0:0:0:5:600:300c:326b" 
        print(regex_ipv6(string_IPv6))
    """
    #匹配是否满足IPv6格式要求,请注意例子里大小写不敏感
    if re.match(r"^(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}$", string,re.I):
        if display:
            print("IPv6 vaild")
        result = re.findall(r"(?<![:.\w])(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}(?![:.\w])", string, re.I) #打印提取结果
        return result
    else:
        if display:
            print("IPv6 invaild")


def regex_space(string,display=False):
    """
    example:
        string_space = "cirros   ssh:notty    211.36.141.237   Mon Apr 26 04:22 - 04:22  (00:00) " 
        print(regex_space(string_space))
    """
    test_split_space = re.split(" ",string)
    if test_split_space:
        return list(filter(lambda  ls : ls != "",test_split_space))
    else:
        if display:
            print("split space invested")

def regex_legit_ip(_ip):
    '''
    判断合法ip
    '''
    compile_ip = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if compile_ip.match(_ip):
        return True
    else:
        return False

def regex_ip_intr_extr(huanggr):
    '''
    判断是内网ip还是外网ip
    '''
    intr = [10,172,192]
    intranet_ips = []
    extranet_ips = []
    for i in huanggr:
        for ii in intr:
            _ip = re.match( r'%s.*' %(ii), i)
            if _ip:
                intranet_ips.append(_ip.group())
    extranet_ips = list(set(huanggr)-set(intranet_ips))
    return {"intranet_ips":intranet_ips,"extranet_ips":extranet_ips}

if __name__ == '__main__':
    _legit_ip = []
    _input = ['10.12.16.224', '10.256.8.56', '192.168.257.1', '172.56.25.2', '183.18.46.53', '86.17.46.12',
              '213.49.56.38']
    for _ip in _input:
        if regex_legit_ip(_ip):
            _legit_ip.append(_ip)
    print(regex_ip_intr_extr(_legit_ip)["intranet_ips"])
    print(regex_ip_intr_extr(_legit_ip)["extranet_ips"])
    string_space = "cirros   ssh:notty    211.36.141.237   Mon Apr 26 04:22 - 04:22  (00:00) " 
    print(regex_space(string_space))


