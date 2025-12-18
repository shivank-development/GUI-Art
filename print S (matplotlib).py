import matplotlib.pyplot as plt

s_art = """ 
 *****
*     
*     
 *****
      *
*     *
 *****
"""

plt.figure(figsize=(4,6))
plt.text(0.5, 0.5, s_art, fontsize=20, fontfamily='monospace', ha='center', va='center')
plt.axis('off')
plt.show()
