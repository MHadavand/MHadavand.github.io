import pygeostat as gs
import pandas as pd

# Global setting using Parameters
gs.Parameters['data.griddef'] = gs.GridDef([10,1,0.5, 10,1,0.5, 2,1,0.5])
gs.Parameters['data.nreal'] = nreal = 100
size = gs.Parameters['data.griddef'].count();

reference_data = pd.DataFrame({'value':np.random.normal(0, 1, size = size)})

# Create example simulated data
simulated_data =pd.DataFrame(columns=['value'])
for i, offset in enumerate(np.random.rand(nreal)*0.04 - 0.02):
    simulated_data= simulated_data.append(pd.DataFrame({'value':np.random.normal(offset, 1, size = size)}))

gs.histogram_plot_simulation(simulated_data, reference_data, reference_variable='value',
                        title='Histogram Reproduction', grid=True)