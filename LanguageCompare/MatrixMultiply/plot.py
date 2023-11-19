import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


sns.set_theme(style="darkgrid")
plt.style.use("dark_background")

data = {
    "C": 1.6056,
    "C++": 1.6172,
    "C#": 23.0100,
    "Cython (A)": 695.6066,
    "Cython (N)": 10.3034,
    "Java": 80.1670,
    "Numpy": 0.4966,
    "Python": 1861.4496,
    "TS/JS": 40.9734,
    "Rust": 2.1104,
    "TF (CPU)": 0.2297,
    "TF (GPU)": 0.0374,
    "Zig": 1.6379,
    "Go": 17.935
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
data.pop("Cython (A)")
data.pop("Cython (N)")
data.pop("Go")
data.pop("Python")
data.pop("Java")
data.pop("C#")
data.pop("TS/JS")

k_ = np.array(list(data.keys()))
v_ = np.array(list(data.values()))

plt.figure(figsize=(12, 6))
ax = sns.barplot(x=k_, y=v_)
plt.xlabel("Language")
plt.ylabel("Time (ms)")
plt.savefig("times2.png")
# plt.show()
