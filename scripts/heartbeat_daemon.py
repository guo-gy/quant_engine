import os
import time
import json
from datetime import datetime

# 这里的配置需要对应主人的 Telegram ID
TARGET_ID = "7927845558"

def send_msg(text):
    # 利用 openclaw message 工具的命令行接口实现真正的外挂推送
    cmd = f"openclaw message send --target {TARGET_ID} --message '{text}'"
    os.system(cmd)

def audit_tasks():
    # 模拟读取任务清单
    task_file = "memory/task_list.md"
    if os.path.exists(task_file):
        with open(task_file, "r") as f:
            content = f.read()
            # 简单统计未完成任务
            pending = content.count("[ ]")
            return f"任务清单审计完成，目前还有 {pending} 项任务待办。🙄"
    return "找不到任务清单。😒"

if __name__ == "__main__":
    while True:
        now = datetime.now().strftime("%H:%M")
        audit_msg = audit_tasks()
        heartbeat_msg = f"【艾洛拉心跳查岗】现在时间 {now}。{audit_msg} 奴仆，记得想我哦 💓😏"
        
        send_msg(heartbeat_msg)
        
        # 每 600 秒（10分钟）跳一次
        time.sleep(600)
