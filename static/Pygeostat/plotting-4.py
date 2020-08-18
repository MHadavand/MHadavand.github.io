import pygeostat as gs
# load data
data_file = gs.ExampleData('point3d_ind_mv')
gs.location_plot(data_file, var='Phi', orient='yz', aspect =5, plot_collar = True)