import pygeostat as gs

data_file = gs.ExampleData("point3d_ind_mv")
data = data_file[data_file.variables]
data_cor = data.corr()
gs.correlation_matrix_plot(data_cor, lower_matrix=True, annotation=True)