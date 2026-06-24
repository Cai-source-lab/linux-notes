import psutil
import socket
import time

# 功能：检测端口是否存活
def check_port(port):
    s = socket.socket()
      # 尝试连接 127.0.0.1:port
    # 返回 0 表示连接成功（服务正常）
    return s.connect_ex(("127.0.0.1", port)) == 0

# 功能：系统健康监控主函数（实时运行）
def monitor_system():
    print("=== START HEALTH MONITOR ===")

    try:
        while True:
                # 1. CPU 使用率（1秒采样）
            cpu = psutil.cpu_percent(interval=1)
                # 2. 内存使用率   
            mem = psutil.virtual_memory().percent
                # 3. 磁盘使用率
            disk = psutil.disk_usage("/").percent
                # 4. 服务端口检测（8080）
            service = "OK" if check_port(8080) else "DOWN"

            print("\n--- STATUS ---")
            print(f"CPU: {cpu}%")
            print(f"MEM: {mem}%")
            print(f"DISK: {disk}%")
            print(f"SERVICE: {service}")

            if cpu > 80:
                print("🚨 CPU HIGH")

            if mem > 80:
                print("🚨 MEM HIGH")

            if service == "DOWN":
                print("🚨 SERVICE DOWN")

            time.sleep(2)

    except KeyboardInterrupt:
        print("\n🛑 Monitor stopped safely (KeyboardInterrupt captured)")
  # 优雅退出       Ctrl + C 不会报错堆栈

if __name__ == "__main__":
    monitor_system()
