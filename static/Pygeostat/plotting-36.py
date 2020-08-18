import pygeostat as gs
data_file = gs.ExampleData('3d_correlation')
loadmat = data_file.data.corr().iloc[3:6,6:9]
gs.loadings_plot(loadmat.values, figsize=(5,5), xticklabels=['PC1', 'PC2', 'PC3'], yticklabels=['InputVariable1', 'InputVariable2', 'InputVariable3'])