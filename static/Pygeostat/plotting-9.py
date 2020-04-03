import pygeostat as gs
# load some data
dfl = gs.ExampleData("point3d_ind_mv")
cats = [1, 2, 3, 4, 5]
colors = gs.catcmapfromcontinuous("Spectral", 5).colors
# build the required cat dictionaries
dfl.catdict = {c: "RT {:02d}".format(c) for c in cats}
colordict =  {c: colors[i] for i, c in enumerate(cats)}
# plot the histogram_plot
f, axs = plt.subplots(2, 1, figsize=(8, 6))
for var, ax in zip(["Phi", "Sw"], axs):
    gs.histogram_plot(dfl, var=var, cat=True, color=colordict, bins=40, figsize=(8, 4), ax=ax,
               xlabel=False, title=var)