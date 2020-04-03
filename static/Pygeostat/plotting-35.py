import pygeostat as gs

varmodeldat = gs.ExampleData('variogram_model')
gs.variogram_plot(varmodeldat, index=1, experimental=False)