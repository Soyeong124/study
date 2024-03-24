# ---
# jupyter:
#   jupytext:
#     formats: py:percent,ipynb
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
pip install numpy

# %% [markdown]
# # 블랙숄즈머튼 옵션가격 모형
# 유러피안 콜 옵션 가격을 시뮬레이션을 통해 계산
# ![image.png](attachment:982c427a-c4b9-43b0-9a6e-5ab16fb413cd.png)
# ![image.png](attachment:d8fbb247-8090-490b-be7e-b5cb7d804d9c.png)

# %%
import math
import numpy as np

# %%
S0 = 100
K = 105
T = 1.0
r = 0.05
sigma = 0.2

# %%
I = 100000

# %%
np.random.seed(1000)

# %%
z = np.random.standard_normal(I)
# 표쥰정규분포 난수 뽑기

# %%
ST = S0 * np.exp((r - sigma ** 2 / 2) * T + sigma * math.sqrt(T) * z)

# %%
hT = np.maximum(ST - K, 0)

# %%
C0 = math.exp(-r * T) * np.mean(hT)

# %%
print("Value of the Eutopean call option: {:5.3f}.".format(C0))

# %%
print("git test")

# %%
