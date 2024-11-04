from services.scan import port_scanner as ps
from db_store.status import db_scan_status as ds
from utils import scan_time as st
from utils import db_connection as dc
from utils import scan_id

db = dc.get_db()
collection = db['open_ports']

uoid = scan_id.generate_uoid()

start_time = ""
end_time = ""

def db_scan_data(ip_addrs, ports):
    global start_time, end_time

    start_time = st.time_status()

    for ip in ip_addrs:
        port_status = []
        for port in ports:
            nmap_status = ps.start_nmap_scan(ip, port)
            port_status.append({
                f"{port}" : {
                "ipaddress" : ip,
                "port" : port,
                "status" : nmap_status
                }
                })
        
        port_scan_status = {
            "_id" : uoid,
            f"{ip}" : port_status
            }

        collection.insert_one(port_scan_status)
    
    end_time = st.time_status()
    
    return "Ports scanned successfully!!"

def resp_time():
    return start_time, end_time


