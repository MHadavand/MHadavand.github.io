import pygeostat as gs
grid_str = '''120 5.00  10.00 -nx, xmn, xsiz
            110 1205.00  10.00 -ny, ymn, ysiz
            1 0.5 1.0  -nz, zmn, zsiz'''

griddef = gs.GridDef(grid_str=grid_str)

data_fl = gs.ExampleData("grid2d_surf", griddef=griddef)
ax = gs.slice_plot(data_fl, var="Thickness")
_ = gs.contour_plot(data_fl, var="Thickness", ax = ax, clabel=True)