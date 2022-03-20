# LOF
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import LocalOutlierFactor
data1 = [[1, 1], [2, 2.1], [1, 2], [2, 1], [50, 35], [2, 1.5], [10, 1], [20, 2.1], [10, 20], [35 , 50]]
df = pd.DataFrame(np.array(data1), columns = ["x", "y"], index = [0,1,2,3,4,5,6,7,8,9])
plt.scatter(df["x"], df["y"], color = "r", s = 65)
plt.grid()
lof = LocalOutlierFactor(n_neighbors=2, metric='manhattan')
prediction = lof.fit_predict(data1)
print("LOF:",prediction)
print("Outliers:-:")
for i in range(0,len(prediction)):
    if prediction[i] == -1:
        print(data1[i])
plt.show()
