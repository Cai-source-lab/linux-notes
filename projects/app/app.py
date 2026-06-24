import time
import random
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

# =========================
# 模拟日志文件
# =========================
LOG_FILE = "logs/app.log"

def write_log(level, message):
    """写入日志"""
    with open(LOG_FILE, "a") as f:
        log = f"[{level}] {time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n"
        f.write(log)
        print(log.strip())


# =========================
# 模拟业务逻辑
# =========================
def business_logic():
    """模拟后台业务"""
    while True:
        time.sleep(2)

        event = random.randint(1, 10)

        if event <= 6:
            write_log("INFO", "request processed successfully")
        elif event <= 8:
            write_log("WARNING", "slow response detected")
        else:
            write_log("ERROR", "database connection failed")


# =========================
# 模拟故障（关键加分点）
# =========================
def fault_injector():
    """随机制造故障"""
    while True:
        time.sleep(10)

        fault = random.randint(1, 10)

        if fault == 1:
            write_log("ERROR", "SERVICE CRASHED (simulated)")
        elif fault == 2:
            write_log("ERROR", "PORT CONFLICT DETECTED")
        elif fault == 3:
            write_log("WARNING", "HIGH CPU USAGE DETECTED")
        else:
            write_log("INFO", "system running normally")


# =========================
# HTTP服务（模拟真实接口）
# =========================
class SimpleHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            write_log("INFO", "GET / request received")

            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Service is running")

        elif self.path == "/error":
            write_log("ERROR", "manual error triggered")

            self.send_response(500)
            self.end_headers()
            self.wfile.write(b"Internal Server Error")

        else:
            write_log("WARNING", f"unknown endpoint: {self.path}")

            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")


# =========================
# 启动服务
# =========================
def start_server():
    server = HTTPServer(("0.0.0.0", 8080), SimpleHandler)
    write_log("INFO", "HTTP server started on port 8080")
    server.serve_forever()


# =========================
# 主程序
# =========================
if __name__ == "__main__":

    write_log("INFO", "service starting...")

    # 启动业务线程
    threading.Thread(target=business_logic, daemon=True).start()

    # 启动故障注入线程
    threading.Thread(target=fault_injector, daemon=True).start()

    # 启动HTTP服务
    start_server()
