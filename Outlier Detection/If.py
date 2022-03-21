# Isolation Forest
from sklearn.ensemble import IsolationForest
data = [[1, 1], [2, 2.1], [1, 2], [2, 1], [50, 35], [2, 1.5], [10, 1], [20, 2.1], [10, 20], [35, 50]]
iforest = IsolationForest(n_estimators=5)
iforest.fit(data)
prediction = iforest.predict(data)
print("IF: ",prediction)
print("IF Outliers:-:")
for i in range(0,len(prediction)):
    if prediction[i] == -1:
        print(data[i])
