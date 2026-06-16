import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
trials = 10000

samplesize = [1, 5, 10, 20, 50, 100, 500, 1000]

plt.figure(figsize=(12, 6)
plt.suptitle("Central Limit Theorem", fontsize=16) 
for i, n in enumerate(samplesize, 1):
    plt.subplot(2, 4, i)
    sample = np.random.binomial(n, 0.5, trials)
    mean = sample / n
    
    sns.histplot(mean, kde=True, bins=20, color='blue', edgecolor='black', stat='density')
    plt.title(f"Sample size={n}")
plt.tight_layout() 
plt.show()
