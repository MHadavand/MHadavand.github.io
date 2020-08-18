import pygeostat as gs

varcalcdat = gs.ExampleData('experimental_variogram')
varmodeldat = gs.ExampleData('variogram_model')

colors = gs.get_palette('cat_dark', 2, cmap=False)
ax = gs.variogram_plot(varcalcdat.data, index=1, color=colors[0], minpairs=False, label=False)
gs.variogram_plot(varmodeldat.data, index=1, experimental=False, ax=ax, color=colors[0], label='Minor')
gs.variogram_plot(varcalcdat.data, index=2, ax=ax, color=colors[1], label=False)
gs.variogram_plot(varmodeldat.data, index=2, experimental=False, ax=ax, color=colors[1], label='Major')

plt.legend(loc=4)