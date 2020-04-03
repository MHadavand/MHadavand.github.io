import pygeostat as gs
# load some data
dfl = gs.ExampleData("point3d_ind_mv")
# plot the histogram_plot
gs.histogram_plot(dfl, var="Phi", icdf=True, stat_blk='all', stat_xy=(1, 0.75))
# Change the CDF line colour by grabbing the 3rd colour from the color pallet
# ``cat_vibrant`` and increase its width by passing a keyword argument to matplotlib's
# plot function. Also define a custom statistics block:
gs.histogram_plot(dfl, var="Phi", icdf=True, color=3, lw=3.5, stat_blk=['count','upquart'])