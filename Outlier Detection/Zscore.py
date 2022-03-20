# Z score
import numpy as np
data = [1,2,3,2,1,100,1,2,3,2,1,50,3,4,5,10,7,2,5,80]
threshold = 3
mean = np.mean(data)
std = np.std(data)
z_score_outlier = [i for i in data if (i-mean)/std > threshold]
print("Z score:",z_score_outlier)
