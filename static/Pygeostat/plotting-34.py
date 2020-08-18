import pygeostat as gs

varcalcdat = gs.ExampleData('experimental_variogram')
varmodeldat = gs.ExampleData('variogram_model')
ax = gs.variogram_plot(varcalcdat.data, index=1, sill=False)
gs.variogram_plot(varmodeldat.data, index=1, experimental=False, ax=ax)