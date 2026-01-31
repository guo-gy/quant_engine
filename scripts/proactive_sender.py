import sys
import os

# 模拟一个能直接调用 OpenClaw 消息接口的后台脚本
def send_proactive_message(target_id, text):
    # 这里通过命令行调用 openclaw 的底层发送逻辑 (如果允许的话)
    os.system(f"openclaw message send --target {target_id} --message '{text}'")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 send_msg.py <target_id> <message>")
    else:
        send_proactive_message(sys.argv[1], sys.argv[2])
