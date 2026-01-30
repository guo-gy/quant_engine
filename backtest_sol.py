import backtrader as bt
import pandas as pd
import yfinance as yf
from datetime import datetime

class BollingerBandsStrategy(bt.Strategy):
    params = (('period', 20), ('devfactor', 2.0),)

    def __init__(self):
        self.bb = bt.indicators.BollingerBands(self.data.close, period=self.p.period, devfactor=self.p.devfactor)

    def next(self):
        if not self.position:
            if self.data.close[0] > self.bb.lines.top[0]:
                self.buy()
        else:
            if self.data.close[0] < self.bb.lines.bot[0]:
                self.sell()

def run_backtest(symbol='SOL-USD'):
    data = yf.download(symbol, start='2025-01-01', end=datetime.now().strftime('%Y-%m-%d'), interval='1h')
    if data.empty:
        print("数据下载失败")
        return
    
    # 修复 pandas 2.0+ 导致的多重索引或格式问题
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)
    
    data.columns = [str(x).lower() for x in data.columns]
    
    feed = bt.feeds.PandasData(dataname=data)
    cerebro = bt.Cerebro()
    cerebro.addstrategy(BollingerBandsStrategy)
    cerebro.adddata(feed)
    cerebro.broker.setcash(1000.0)
    cerebro.broker.setcommission(commission=0.001) # 模拟千一手续费

    print(f'初始资金: {cerebro.broker.getvalue():.2f}')
    cerebro.run()
    print(f'期末资金: {cerebro.broker.getvalue():.2f}')

if __name__ == '__main__':
    run_backtest()
