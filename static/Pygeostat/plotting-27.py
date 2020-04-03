import pygeostat as gs
dat = gs.ExampleData('point3d_ind_mv')
data = dat.data[dat.data['HoleID'] == 3]
gs.drill_plot(data['Elevation'], data['Sw'], grid = True)