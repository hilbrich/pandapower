# -*- coding: utf-8 -*-

# Copyright (c) 2016-2025 by University of Kassel and Fraunhofer Institute for Energy Economics
# and Energy System Technology (IEE), Kassel. All rights reserved.

import uuid
from collections import defaultdict

import numpy as np
import pandas as pd
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import inv

#from pandapower.auxiliary import get_indices
#from pandapower.create import create_empty_network
#from pandapower.toolbox.comparison import compare_arrays
#from pandapower.toolbox.element_selection import element_bus_tuples, pp_elements

try:
    import pandaplan.core.pplog as logging
except ImportError:
    import logging

logger = logging.getLogger(__name__)

def calc_sens_matrix(net):
    #print("success!")
    J=net._ppc['internal']['J']
    sensitivity_matrix_ppc = inv(J)
    pandapower_bus_idx = net.bus.index
    ppc_index = net._pd2ppc_lookups["bus"][pandapower_bus_idx]
    int_idx = net._pd2ppc_lookups["bus"][ppc_index]
    #Ybus[int_idx, int_idx]
    #print(J.toarray())
    return ppc_index, sensitivity_matrix_ppc

    np.set_printoptions(precision=6, suppress=True)  # 2 Dezimalstellen und keine wissenschaftliche Notation
    print(sensitivity_matrix_ppc.toarray())