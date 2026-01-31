import pandas as pd
import numpy as np

class QuantEngine:
    def __init__(self, data):
        self.data = data
        self.results = None

    def run_backtest(self, strategy_func):
        print("Starting backtest...")
        self.data = strategy_func(self.data)
        self.calculate_performance()
        return self.data

    def calculate_performance(self):
        # 简单计算累计收益
        self.data['returns'] = self.data['close'].pct_change()
        self.data['strategy_returns'] = self.data['signal'].shift(1) * self.data['returns']
        self.data['cumulative_returns'] = (1 + self.data['strategy_returns'].fillna(0)).cumprod()
        print(f"Final Cumulative Return: {self.data['cumulative_returns'].iloc[-1]:.2f}")

def dual_thrust_strategy(df, k1=0.5, k2=0.5):
    # 模拟 Dual Thrust 逻辑
    df['range'] = df['high'].rolling(5).max() - df['low'].rolling(5).min()
    df['upper_line'] = df['open'] + k1 * df['range'].shift(1)
    df['lower_line'] = df['open'] - k2 * df['range'].shift(1)
    
    df['signal'] = 0
    df.loc[df['close'] > df['upper_line'], 'signal'] = 1
    df.loc[df['close'] < df['lower_line'], 'signal'] = -1
    return df

# 模拟数据并运行
if __name__ == "__main__":
    dates = pd.date_range('2026-01-01', periods=100)
    data = pd.DataFrame({
        'open': np.random.uniform(100, 120, 100),
        'close': np.random.uniform(100, 120, 100),
        'high': np.random.uniform(110, 130, 100),
        'low': np.random.uniform(90, 110, 100)
    }, index=dates)

    engine = QuantEngine(data)
    engine.run_backtest(dual_thrust_strategy)
