import pandas as pd

def process_kline_inclusion(df):
    """
    处理缠论中的K线包含关系
    """
    if len(df) < 2:
        return df
    
    new_klines = []
    # 初始K线
    curr_h = df.iloc[0]['high']
    curr_l = df.iloc[0]['low']
    curr_t = df.index[0]
    
    direction = "UP" # 初始假设向上
    
    for i in range(1, len(df)):
        next_h = df.iloc[i]['high']
        next_l = df.iloc[i]['low']
        
        # 判断包含关系
        is_inclusion = (curr_h >= next_h and curr_l <= next_l) or (next_h >= curr_h and next_l <= curr_l)
        
        if is_inclusion:
            # 包含处理：向上取高高，向下取低低
            if direction == "UP":
                curr_h = max(curr_h, next_h)
                curr_l = max(curr_l, next_l)
            else:
                curr_h = min(curr_h, next_h)
                curr_l = min(curr_l, next_l)
        else:
            # 不包含，记录前一根处理完的K线
            new_klines.append({'time': curr_t, 'high': curr_h, 'low': curr_l})
            # 更新趋势方向
            direction = "UP" if next_h > curr_h else "DOWN"
            curr_h, curr_l, curr_t = next_h, next_l, df.index[i]
            
    new_klines.append({'time': curr_t, 'high': curr_h, 'low': curr_l})
    return pd.DataFrame(new_klines).set_index('time')

if __name__ == "__main__":
    # 简单测试逻辑
    test_data = pd.DataFrame([
        {'high': 100, 'low': 90},
        {'high': 105, 'low': 95}, # 向上
        {'high': 102, 'low': 97}, # 包含
        {'high': 110, 'low': 100} # 向上
    ])
    processed = process_kline_inclusion(test_data)
    print("Processed K-lines:\n", processed)
