import pygeostat as gs
import numpy as np

# Load the data, which registers the variables attribute
data_file1 = gs.ExampleData('point3d_ind_mv')
data_file2 = gs.ExampleData('point3d_ind_mv')
mask = np.random.rand(len(data_file2))<0.3
data_file2.data = data_file2.data[mask]

# Plot with the standard orientation
fig = gs.scatter_plots_lu(data_file1, data_file2, titles=('Data', 'Realization'), s=10, nmax=1000,
                     stat_xy=(0.95, 0.95), pad=(-1, -1), figsize=(10, 10))

# Plot with aligned orientation to ease comparison
fig = gs.scatter_plots_lu(data_file1, data_file2, titles=('Data', 'Realization'), s=10, nmax=1000,
                     stat_xy=(0.95, 0.95), pad=(-1, -1), figsize=(10, 10), cmap='jet',
                     align_orient=True)