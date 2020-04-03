import pygeostat as gs
# load some data
data = gs.ExampleData('3d_grid',griddef = gs.GridDef([40,1,2,40,1,2,40,0.5,1]))
# plot the grid slices
_ = gs.grid_slice_plot(data, nrow=2, ncol=5, start_slice=10, end_slice=25, n_slice=10, cmap='hot', vlim=(-3,3))