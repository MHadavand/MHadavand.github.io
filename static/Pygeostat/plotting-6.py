import pygeostat as gs
# load some data
dfl = gs.ExampleData("point3d_ind_mv")
# plot the histogram_plot
gs.histogram_plot(dfl, var="Phi", bins=30)