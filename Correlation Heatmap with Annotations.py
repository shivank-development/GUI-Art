import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create random dataset
np.random.seed(2)
df = pd.DataFrame(np.random.rand(10, 6), columns=list('ABCDEF'))

# Compute correlation matrix
corr = df.corr()

# Create heatmap
sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5, square=True)

# Display the plot
plt.title("Correlation Heatmap", fontsize=14)
plt.show()
