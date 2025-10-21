
import random
from datetime import datetime

IPS = ["192.168.1.10","10.0.0.5","172.16.0.2","203.0.113.45","198.51.100.7"]
USERS = ["admin","user1","guest","test","root","svc"]
PATHS = ["/", "/login", "/admin", "/api/data", "/favicon.ico", "/notfound", "/error500"]
STATUS = [200, 200, 200, 200, 404, 403, 500, 400]

def generar_evento():
    
    return {
        "timestamp": datetime.now().isoformat(),
        "ip": random.choice(IPS),
        "user": random.choice(USERS),
        "path": random.choice(PATHS),
        "status_code": random.choice(STATUS)
    }
