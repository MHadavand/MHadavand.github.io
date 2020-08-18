import pygeostat as gs
import numpy as np
mean = [0, 0]
cov = [[1, 0.8], [0.8, 1]]  # diagonal covariance
x, y = np.random.multivariate_normal(mean, cov, 5000).T
gs.validation_plot(x,y,vlim=(-3.5, 3.5) ,grid=True, stat_xy=(1, 0.68))