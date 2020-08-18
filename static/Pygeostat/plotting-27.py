import pygeostat as gs
dat = gs.ExampleData('point3d_ind_mv')
data = dat.data[dat.data['HoleID'] == 3]
cat_dict = {1: {'name': 'Sand', 'color': 'gold'},
        3: {'name': 'SHIS','color': 'orange'},
        4: {'name': 'MHIS','color': 'green'},
        5: {'name': 'MUD','color': 'gray'}}
gs.drill_plot(data['Elevation'], data['Lithofacies'], categorical_dictionary=cat_dict)