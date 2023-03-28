import matplotlib.pyplot as plt
N = [10, 100, 1000, 10000, 100000, 1000000]
hash_table = [0, 0.00005, 0.00235, 0.3321, 1.19985, 4.0019]
binary_tree = [0, 0.0001, 0.0035, 0.5452, 1.8648, 10.4047]
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
ax1.plot(N[:3], hash_table[:3], marker='o', label='Hash Table')
ax1.plot(N[:3], binary_tree[:3], marker='o', label='Balanced Binary Tree')
ax1.set_xscale('log')
ax1.set_xlabel('N')
ax1.set_ylabel('Running Time(ms)')
ax1.set_title('N<=1000')
ax1.legend()
ax2.plot(N[3:], hash_table[3:], marker='o', label='Hash Table')
ax2.plot(N[3:], binary_tree[3:], marker='o', label='Balanced Binary Tree')
ax2.set_xscale('log')
ax2.set_xlabel('N')
ax2.set_ylabel('Running Time(Second)')
ax2.set_title('N>1000')
ax2.legend()
plt.savefig("Q3.pdf")
plt.show()
