import pygeostat as gs
data = gs.ExampleData('3d_estimate')
gs.validation_plot(data.data['Estimate'], data.data['True'], stat_blk='minimal')