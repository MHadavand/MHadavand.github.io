import pygeostat as gs
# load some data
dfl = gs.ExampleData("point3d_ind_mv")
cats = [1, 2, 3, 4, 5]
colors = gs.catcmapfromcontinuous("Spectral", 5).colors
# build the required cat dictionaries
dfl.catdict = {c: "RT {:02d}".format(c) for c in cats}
colordict =  {c: colors[i] for i, c in enumerate(cats)}
# plot the histogram_plot
f, axs = plt.subplots(2, 2, figsize=(12, 9))
axs=axs.flatten()
for var, ax in zip(dfl.variables, axs):
    gs.histogram_plot(dfl, var=var, icdf=True, cat=True, color=colordict, ax=ax)