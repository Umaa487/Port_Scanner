import ipaddress

def generate_ip_addresses_from_cidr(cidr_block):
    ip_network = ipaddress.ip_network(cidr_block, strict=False)
    return [str(ip) for ip in ip_network.hosts()]

''' cidr_block = "192.168.1.0/24"
print(generate_ip_addresses_from_cidr(cidr_block)) '''

