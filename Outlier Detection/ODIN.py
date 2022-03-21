# ODIN
import package_outlier as po
data = [[1, 1], [2, 2.1], [1, 2], [2, 1], [50, 35], [2, 1.5], [10, 1], [20, 2.1], [10, 20], [35, 50]]
result = po.LocalOutlierFactorOutlier(data)
print(result)
