import pygeostat as gs

#Load the data from output from varcal/varmodel file
varcalcdat = gs.ExampleData('experimental_variogram')
gs.variogram_plot(varcalcdat, index=1)