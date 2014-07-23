import os
from crate.testing.layer import CrateLayer

project_root = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))))


def crate_path(*parts):
    return os.path.join(project_root, 'parts', 'crate', *parts)

crate_layer = CrateLayer('crate',
                         crate_home=crate_path(),
                         port=44200)
