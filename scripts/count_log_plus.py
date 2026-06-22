import sys
import json
from collections import defaultdict
#  判断是否输入文件名

if len(sys.argv) !=2:
#  如果参数数量不等于2,即程序名+文件名
    print("用法：python3 count_log_plus.py log.txt")
    sys.exit(1) #程序退出

file_path = sys.argv[1]  #获取用户输入的程序路径

keywords = ["error","warning","info"]  #定义关键词，并且可以随时扩展

result = defaultdict(int)
#自动初始化为0,不用if去判断

try:
    with open(file_path, "r", encoding="utf-8") as f:  #打开文件，按行读取后返回列表
        lines = f.readlines()

except FileNotFoundError:  #文件不存在则运行
    print(f"文件{file_path}不存在")
    sys.exit(1)

for line in lines:  #遍历每一行日志
    line = line.lower().strip()
#全部转为小写，去掉换行符和多余的空格

    for key in keywords:
        if key in line:
            result[key] += 1
for key in keywords:
    print(f"{key}:{result[key]}")

with open("report.txt", "w", encoding="utf-8") as f:
    f.write("LOG ANALYSIS REPROT\n")
    f.write("================\n")
    for key in keywords:
        f.write(f"{key}:{result[key]}\n")
print("/报告已生成：report.txt")


result_dict = dict(result)  #让json看的懂defaultdic
with open("report.json", "w", encoding="utf-8") as f:
    json.dump(result_dict, f, indent=4,ensure_ascii=False)  #把python字典写入json文件，美观json，防止中文乱码
print("/报告已生成：report.json")
