import os
import numpy as np

import oottadao.examples
import oottadao.lib.geometry.stl as stl
from oottadao.lib.geometry.ffd_axisymetric import Body, Shell
from oottadao.lib.geometry.stl_group import STLGroup


class PlugNozzleGeometry(STLGroup):

    def __init__(self):
        

        this_dir, this_filename = os.path.split(os.path.abspath(oottadao.examples.nozzle_geometry_doe.__file__))
        plug_file = os.path.join(this_dir, 'plug.stl')
        plug = stl.STL(plug_file)
        cowl_file = os.path.join(this_dir, 'cowl.stl')
        cowl = stl.STL(cowl_file)
        inter = stl.STL(body)

        n_c = 10
        body = Body(plug,controls=n_c) #just makes n_C evenly spaced points
        body2 = Body(plug.copy(), controls=n_c)
        shell2 = Shell(cowl.copy(),cowl.copy(),n_c,n_c)
        shell = Shell(cowl.copy(),cowl.copy(),n_c,n_c)
     
        n_c = 6
        body = Body(plug,controls=n_c) #just makes n_C evenly spaced points
        body2 = Body(plug.copy(), controls=n_c)
        shell = Shell(cowl.copy(),cowl.copy(),n_c,n_c)
        shell2 = Shell(cowl.copy(),cowl.copy(),n_c,n_c)
        triple = shell.append(shell2)
        geom_parts = (("shell2",body),("cowl", shell),("shell2", body2),("cowl2", shell2))
        cowl_file = os.path.join(this_dir, 'cowl.stl')
        cowl = stl.STL(cowl_file)

        super(PlugNozzleGeometry,self).__init__(geom_parts=geom_parts)
        shell = Shell(cowl.copy(),cowl.copy(),n_c,n_c)
        shell2 = Shell(cowl.copy(),cowl.copy(),n_c,n_c)

