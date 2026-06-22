import os
import json

# =========================
# 1. 定义日志目录
# =========================

log_dir = "logs"

# =========================
# 2. 定义要统计的关键词
# 后续可以随时扩展
# =========================

keywords = [
    "error",
    "warning",
    "info"
]

# =========================
# 3. 创建总结果字典
# V4开始使用嵌套字典
# =========================

result = {}

# =========================
# 4. 获取logs目录中的所有文件
# =========================

try:
    files = os.listdir(log_dir)

except FileNotFoundError:
    print(f"目录 {log_dir} 不存在")
    exit()

# =========================
# 5. 遍历每个日志文件
# =========================

for file in files:

    # 拼接完整路径
    path = os.path.join(log_dir, file)

    # 如果不是文件则跳过
    if not os.path.isfile(path):
        continue

    print(f"正在分析: {path}")

    # =========================
    # 给当前文件创建统计空间
    # =========================

    result[file] = {}

    # 初始化计数器
    for key in keywords:
        result[file][key] = 0

    # =========================
    # 读取日志文件
    # =========================

    try:

        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()

    except Exception as e:

        print(f"读取失败: {path}")
        print(e)

        continue

    # =========================
    # 遍历日志每一行
    # =========================

    for line in lines:

        line = line.lower().strip()

        # =========================
        # 遍历关键词
        # =========================

        for key in keywords:

            if key in line:

                # V4核心
                result[file][key] += 1

# =========================
# 6. 输出统计结果
# =========================

print("\n===== 分析结果 =====\n")

for file in result:

    print(f"===== {file} =====")

    for key in result[file]:

        print(f"{key}: {result[file][key]}")

    print()

# =========================
# 7. 生成TXT报告
# =========================

with open(
    "report.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write("LOG ANALYSIS REPORT\n")
    f.write("===================\n\n")

    for file in result:

        f.write(f"===== {file} =====\n")

        for key in result[file]:

            f.write(
                f"{key}: {result[file][key]}\n"
            )

        f.write("\n")

print("报告已生成: report.txt")

# =========================
# 8. 生成JSON报告
# =========================

with open(
    "report.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        result,
        f,
        indent=4,
        ensure_ascii=False
    )

print("报告已生成: report.json")
