import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot([0, 1, 2, 3, 4])  #for older version use distplot and for latest use displot
plt.show()

# 
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot([0, 1, 2, 3, 4, 5], hist = False)  #hist is the histogram
plt.show()