
int check_ipv4_subnet(
    ipv4,
    ipv4_subnet
){
    int i;
    for(i = 0; i < 4; i++){
        if(ipv4[i] & ipv4_subnet[i] != ipv4[i])
            return 0;
    }
    return 1;
}