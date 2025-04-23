import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib import rcParams
import pandas as pd
import numpy as np

rcParams["font.family"] = "sans-serif"
rcParams["font.sans-serif"] = [
    "Hiragino Maru Gothic Pro",
    "Hiragino sans",
    "BIZ UDGothic",
    "MS Gothic",
]


# 日経平均株価の株価の取得（７日間１日おき）
data = yf.download("^N225", period="7d", interval="1d")
# print(type(data))
print(data)

# NumPyを使って整数の連番の配列を作成する(x軸に使用するために生成（数字）)
# そのまま日付を使用できるが、日付で位置調整をするより数字にして調整した方が調整しやすい
index = np.arange(len(data.index))
# グラフの棒の幅を決める
bar_width = 0.15
# x軸のラベルの位置を設定
tick_locations = index + bar_width * 1.5
# x軸のラベルを取得したdataのindex(日時)にし、表示を一定にしたリストを作成する
tick_label = data.index.strftime("%Y-%m-%d").tolist()

plt.figure(figsize=(14, 6))

plt.bar(index, data["Close"].values.flatten(), bar_width, label="終値")
plt.bar(
    index + bar_width,
    data["High"].values.flatten(),
    bar_width,
    label="高値",
    align="center",
)
plt.bar(
    index + bar_width * 2,
    data["Low"].values.flatten(),
    bar_width,
    label="安値",
    align="center",
)
plt.bar(
    index + bar_width * 3,
    data["Open"].values.flatten(),
    bar_width,
    label="始値",
    align="center",
)

plt.legend(loc="upper right")
plt.xlabel("Date")
plt.ylabel("Price")
plt.title("日経平均株価（終値、高値、安値、始値）")
plt.xticks(tick_locations, tick_label)
plt.tight_layout()
plt.show()

plt.bar(
    index,
    data["Volume"].values.flatten(),
    bar_width,
    label="出来高",
    align="center",
)

plt.legend(loc="upper right")
plt.xlabel("Date")
plt.ylabel("Price")
plt.title("日経平均株価（出来高）")
plt.xticks(index, tick_label)
plt.tight_layout()
plt.show()
