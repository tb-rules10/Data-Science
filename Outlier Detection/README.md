## Outlier Detection

- [Zscore](https://github.com/tb-rules10/Data-Science/blob/main/Outlier%20Detection/Zscore.py) - The Z-score(also called the standard score) is an important concept in statistics that indicates how far away a certain point is from the mean. By applying Z-transformation we shift the distribution and make it 0 mean with unit standard deviation. For example — A Z-score of 2 would mean the data point is 2 standard deviation away from the mean.

`Z-score(i) = (x(i) -mean) / standard deviation`

- [LOF](https://github.com/tb-rules10/Data-Science/blob/main/Outlier%20Detection/LOF.py) - In Local Outlier Factor (LOF), the idea revolves around the concept of local regions. Here, we calculate and compare the local density of the focus point with the local density of its neighbours.

     `LOF ≈ 1 similar density as neighbors` <br>
     `LOF < 1 higher density than neighbors (normal point)` <br>
     `LOF > 1 lower density than neighbors (anomaly)` <br>

- [Isolation Forest](https://github.com/tb-rules10/Data-Science/blob/main/Outlier%20Detection/IF.py) - Isolation Forest is a tree-based algorithm that tries to find out outliers based on the concept of decision boundaries(just like we have for decision trees). The idea over here is to keep splitting the data at random thresholds and feature till every point gets isolated(it’s like overfitting a decision tree on a dataset).

- [ODIN](https://github.com/tb-rules10/Data-Science/blob/main/Outlier%20Detection/ODIN.py) - In Outlier Detection using In-degree Number (ODIN), we calculate the in-degree for each of the data points. Here, in-degree is defined as the number of nearest neighbour sets to this point belongs. Higher this value, the more the confidence of this point belonging to some dense region in the space. Whereas, on the other side, a lesser value of this would mean that it’s not part of many nearest neighbour sets and is kind of isolated in the space. You can think of this method to be the reverse of KNN.


- [Interquartile Range](https://github.com/tb-rules10/Data-Science/blob/main/Outlier%20Detection/IQR.py)
