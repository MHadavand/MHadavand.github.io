import pygeostat as gs
data_file = gs.ExampleData('point3d_ind_mv')
gs.location_plot(data_file, var = 'Phi')