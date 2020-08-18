import pygeostat as gs
data_file = gs.ExampleData('accuracy_plot')
reals = data_file[list(data_file.columns[1:])].values
truth = data_file[list(data_file.columns)[0]].values
gs.accuracy_plot(truth=truth, reals=reals)