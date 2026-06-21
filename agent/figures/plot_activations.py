# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "matplotlib",
#     "numpy",
# ]
# ///
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-6, 6, 300)

# Sigmoid
sigmoid = 1 / (1 + np.exp(-x))

# ReLU
relu = np.maximum(0, x)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3.5))

# --- Sigmoid ---
ax1.plot(x, sigmoid, color='#2563eb', linewidth=2)
ax1.axhline(0, color='gray', linewidth=0.5)
ax1.axvline(0, color='gray', linewidth=0.5)
ax1.set_title(r'$\sigma(x) = \frac{1}{1+e^{-x}}$', fontsize=14)
ax1.set_ylim(-0.1, 1.1)
ax1.set_xlim(-6, 6)
ax1.grid(True, linewidth=0.3)

# --- ReLU ---
ax2.plot(x, relu, color='#dc2626', linewidth=2)
ax2.axhline(0, color='gray', linewidth=0.5)
ax2.axvline(0, color='gray', linewidth=0.5)
ax2.set_title(r'$\mathrm{ReLU}(x) = \max(0, x)$', fontsize=14)
ax2.set_ylim(-0.5, 6.5)
ax2.set_xlim(-6, 6)
ax2.grid(True, linewidth=0.3)

plt.tight_layout()
plt.savefig('2-2.pdf', bbox_inches='tight')
print('Saved 2-2.pdf')
