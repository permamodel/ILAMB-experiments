"""A custom ILAMB confrontation for net ecosystem productivity (nep)."""
import os
import numpy as np
from ILAMB.Confrontation import Confrontation
from ILAMB.Variable import Variable
import ilamblib as il


class ConfNEP(Confrontation):
    """Confront ``nep`` model outputs with ``nee`` observations.

    Net ecosystem productivity (``nep``) is a CMIP5 standard output
    provided by the MsTMIP models, and is the inverse of net ecosystem
    exchange (``nee``), for which benchmark datasets are provided in
    ILAMB.

    """

    def __init__(self, **keywords):
        super(ConfNEP, self).__init__(**keywords)

    def stageData(self, m):
        obs = Variable(filename=self.source,
                       variable_name=self.variable)
        self._checkRegions(obs)
        obs.data *= -1.0  # Reverse sign of benchmark data.

        mod = m.extractTimeSeries(self.variable,
                                  alt_vars=self.alternate_vars)
        mod.data *= -1.0  # Reverse sign of modified model outputs.

        obs, mod = il.MakeComparable(obs, mod, clip_ref=True,
                                     logstring="[%s][%s]" %
                                     (self.longname, m.name))

        return obs, mod
