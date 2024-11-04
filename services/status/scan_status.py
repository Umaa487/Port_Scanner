from routes.scan import scanner_api as sc

status = sc.api_status()
def api_scan_status():
    global status

    return status