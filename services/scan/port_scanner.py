import subprocess
    
def start_nmap_scan(ip, port):
    command = f"nmap -p {port} {ip}"
    try:
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        stdout = result.stdout.decode("utf-8")
        stderr = result.stderr.decode("utf-8")
                
        if stdout:
            if "open" in stdout:
                return "open"
            elif "Host is up" in stdout:
                return "up"
            else:
                return "close"
        else:
            return stderr

    except Exception as e:
        return f"Error occurred: {str(e)}"
