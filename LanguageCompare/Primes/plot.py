import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


sns.set_theme(style="darkgrid")
plt.style.use("dark_background")

data = {
    "C": 7.4500,
    "C++": 7.3343,
    "C#": 8.2900,
    "Cython": 146.4989,
    "Java": 8.8000,
    "Python": 259.6320,
    "TS/JS": 9.2438,
    "Rust": 7.6278,
    "Zig": 9.0616,
}

data = dict(sorted(data.items(), key=lambda item: item[1]))

k_ = np.array(list(data.keys()))
v_ = np.array(list(data.values()))

plt.figure(figsize=(12, 6))
ax = sns.barplot(x=k_, y=v_)
ax.set(yscale="log")
plt.xlabel("Language")
plt.ylabel("Time (ms)")
plt.savefig("times.png")
# plt.show()

data = dict(sorted(data.items(), key=lambda item: item[1]))
data.pop("Python")
data.pop("Cython")

k_ = np.array(list(data.keys()))
v_ = np.array(list(data.values()))

plt.figure(figsize=(12, 6))
ax = sns.barplot(x=k_, y=v_)
plt.xlabel("Language")
plt.ylabel("Time (ms)")
plt.savefig("times2.png")
# plt.show()
