import pygeostat as gs
# load some data
dfl = gs.ExampleData("point3d_ind_mv")
cats = [1, 2, 3, 4, 5]
colors = gs.catcmapfromcontinuous("Spectral", 5).colors
# build the required cat dictionaries
dfl.catdict = {c: "RT {:02d}".format(c) for c in cats}
colordict =  {c: colors[i] for i, c in enumerate(cats)}
# plot the histogram_plot
ax = gs.histogram_plot(dfl, cat=True, color=colordict, figsize=(7, 4), rotateticks=(45, 0),
                label_count=True)