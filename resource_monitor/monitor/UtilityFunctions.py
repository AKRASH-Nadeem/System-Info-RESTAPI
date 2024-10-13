import os
import psutil

def list_processes():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        processes.append({
            'pid': proc.info['pid'],
            'name': proc.info['name'],
            'user': proc.info['username'],
        })
    return processes

def cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    return {'cpu_usage_percent': cpu_percent}

def memory_usage():
    memory = psutil.virtual_memory()
    return {
        'total_memory': round(memory.total / (1024 ** 3),2),
        'available_memory': round(memory.available / (1024 ** 3),2),
        'used_memory': round(memory.used / (1024 ** 3),2),
        'memory_percentage': memory.percent,
        "Unit": "GB"
    }

def network_usage():
    net_io = psutil.net_io_counters()
    return {
        'bytes_sent': round(net_io.bytes_sent / 1024,2),
        'bytes_recv': round(net_io.bytes_recv / 1024,2),
        "Unit":"kB/s"
    }

def temperature():
    if hasattr(psutil, "sensors_temperatures"):
        temp = psutil.sensors_temperatures()
        return temp
    else:
        return {"error": "Temperature information not available."}

