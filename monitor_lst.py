import json
import time

def check_lst_peg():
    """
    模拟监控 LST 锚定情况。
    在真实场景中，我会调用 Jupiter 或 Birdeye API 获取实时报价。
    """
    # 模拟数据
    data = {
        "SOL": 117.38,
        "JitoSOL": 128.52, # 假设汇率 1.0949
        "mSOL": 135.12,   # 假设汇率 1.1511
        "bSOL": 125.40    # 假设汇率 1.0683
    }
    
    # 理论汇率 (示例)
    theoretical = {
        "JitoSOL": 1.0950,
        "mSOL": 1.1515,
        "bSOL": 1.0685
    }
    
    report = []
    for lst, price in data.items():
        if lst == "SOL": continue
        actual_rate = price / data["SOL"]
        diff = (actual_rate - theoretical[lst]) / theoretical[lst] * 100
        report.append(f"{lst}: 实际汇率 {actual_rate:.4f}, 偏离度 {diff:.4f}%")
        
    return "\n".join(report)

if __name__ == "__main__":
    print("--- LST Peg Monitor (Simulated) ---")
    print(check_lst_peg())
    print("-----------------------------------")
