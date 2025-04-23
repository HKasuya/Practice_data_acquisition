import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams["font.family"] = "sans-serif"
rcParams["font.sans-serif"] = [
    "Hiragino Maru Gothic Pro",
    "Hiragino sans",
    "BIZ UDGothic",
    "MS Gothic",
]

# 過去１０年の月の日経平均株価csvファイルを読み込む
df = pd.read_csv("日経平均株価のcsvファイル名を記載.csv", encoding="shift-jis")

# print(df.columns.values)
# print(df.index.values)

# 最後の行を削除
# df = df.drop(124, axis=0)


# 過去3年分のデータにする(残したい行)
start_index = 86
end_index = 123

df_remaining = df[start_index : end_index + 1]

# 最初の列（年）をインデックスに使用する
df_index = df_remaining.set_index(df.columns[0])
print(df_index)

# 高値と安値の差の列を作る
df_index["高値と安値の差"] = df_index["高値"] - df_index["安値"]
print(df_index)

plt.clf()
df_index["終値"].plot.bar(figsize=(10, 6))
plt.legend(loc="lower right")
plt.show()

plt.clf()
df_index["始値"].plot.bar(figsize=(10, 6))
plt.legend(loc="lower right")
plt.show()

plt.clf()
df_index["高値"].plot.bar(figsize=(10, 6))
plt.legend(loc="lower right")
plt.show()

plt.clf()
df_index["安値"].plot.bar(figsize=(10, 6))
plt.legend(loc="lower right")
plt.show()

plt.clf()
df_index["高値と安値の差"].plot.bar(figsize=(10, 6))
plt.legend(loc="upper right")
plt.ylim(0, 40000)
plt.show()
