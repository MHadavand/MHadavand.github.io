import pygeostat as gs

# Load the data, which registers the variables attribute
data_file = gs.ExampleData('point3d_ind_mv')

# Plot with the default KDE coloring
fig = gs.scatter_plots(data_file, nmax=1000, stat_xy=(0.95, 0.95), pad=(-1, -1), s=10,
                  figsize=(10, 10))