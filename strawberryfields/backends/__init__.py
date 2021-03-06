# Copyright 2019 Xanadu Quantum Technologies Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""This package contains the modules that make up the
Strawberry Fields backends. This includes photonic simulators,
shared numerical operations, and states objects returned by
statevector simulators.

Local statevector simulators
----------------------------

Below are all available local statevector backends currently
provided by Strawberry Fields. These simulators all run locally,
provide access to the state after simulation, and the state is
preserved between engine runs.

.. currentmodule:: strawberryfields.backends
.. autosummary::
    :toctree: api

    FockBackend
    GaussianBackend
    ~tfbackend.TFBackend

.. raw:: html

    <div style="display: none;">

.. currentmodule:: strawberryfields.backends
.. autosummary::
    :toctree: api

    BaseFockState
    ~gaussianbackend.states.GaussianState
    ~tfbackend.states.FockStateTF

.. raw:: html

    </div>

Backend API
-----------

A list of the abstract base classes that define the
statevector backend API

.. currentmodule:: strawberryfields.backends
.. autosummary::
    :toctree: api

    BaseState
    BaseGaussianState
    BaseBackend
    BaseFock
    BaseGaussian

Utility modules
---------------

The following utility modules are provided for
backend development.

.. currentmodule:: strawberryfields.backends
.. autosummary::
    :toctree: api

    shared_ops
"""

from .base import BaseBackend, BaseFock, BaseGaussian, ModeMap
from .gaussianbackend import GaussianBackend
from .fockbackend import FockBackend
from .states import BaseState, BaseGaussianState, BaseFockState

__all__ = [
    "BaseBackend",
    "BaseFock",
    "BaseGaussian",
    "FockBackend",
    "GaussianBackend",
    "TFBackend",
    "BaseState",
    "BaseFockState",
    "BaseGaussianState"
]

supported_backends = {b.short_name: b for b in (BaseBackend, GaussianBackend, FockBackend)}


def load_backend(name):
    """Loads the specified backend by mapping a string
    to the backend type, via the ``supported_backends``
    dictionary. Note that this function is used by the
    frontend only, and should not be user-facing.
    """
    if name == "tf":
        # treat the tensorflow backend differently, to
        # isolate the import of tensorflow
        from .tfbackend import TFBackend

        return TFBackend()

    if name in supported_backends:
        backend = supported_backends[name]()
        return backend

    raise ValueError("Backend '{}' is not supported.".format(name))
