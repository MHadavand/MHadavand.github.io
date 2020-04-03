import pygeostat as gs
data = gs.ExampleData('oilsands')
gs.probability_plot(data.data['Fines'], logscale=False)