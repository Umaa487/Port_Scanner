from services.scan import cidr_gen as ip
from db_store.scan import db_scan_data as db
from db_store.status import db_scan_status as ds

ip_addresses = []
status = ""

def scan_response(data):
    global status

    ipaddrs = data.get('ipaddrs', [])
    if isinstance(ipaddrs, str):
        ipaddrs = [ipaddrs]

    ports = data.get('ports', [])
    if isinstance(ports, int):
        ports = [ports]

    cidr = data.get('cidr')

    if ports:
        if ipaddrs:
            ip_addresses.extend(ipaddrs)

        elif cidr:
            ip_addresses.extend(ip.generate_ip_addresses_from_cidr(cidr))
    
        else:
            status = "IP Adrress or CIDR block not provided"
    
    else:
        status = "Port numbers not provided"
    
    status = db.db_scan_data(ip_addresses , ports)
    ds.db_scan_status_data()

def api_status():
    return status

