import pygeostat as gs
griddef = gs.GridDef([40,0.5,1,40,0.5,1,40,0.5,1])
data_file = gs.ExampleData('3d_grid', griddef)
gs.slice_plot(data_file, orient='xy', cmap='viridis')