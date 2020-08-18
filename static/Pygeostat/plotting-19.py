import pygeostat as gs

# Load the data
data_file = gs.ExampleData('point3d_ind_mv')

# Select a couple of variables
x, y = data_file[data_file.variables[0]], data_file[data_file.variables[1]]

# Scatter plot with default parameters
gs.scatter_plot(x, y, figsize=(5, 5), cmap='hot')

# Scatter plot without correlation and with a color bar:
gs.scatter_plot(x, y, nmax=2000, stat_blk=False, cbar=True, figsize=(5, 5))

# Scatter plot with the a constant color, transparency and all statistics
# Also locate the statistics where they are better seen
gs.scatter_plot(x, y, c='k', alpha=0.2, nmax=2000, stat_blk='all', stat_xy=(.95, .95),
           figsize=(5, 5))