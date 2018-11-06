import os as _os
import dash as _dash
import sys as _sys
from .version import __version__

_current_path = _os.path.dirname(_os.path.abspath(__file__))

_cdn = 'd360wc4uc6n3i9.cloudfront.net'
_namespace = 'dash_table_experiments'
_project = 'dash-table-experiments'

_components = _dash.development.component_loader.load_components(
    _os.path.join(_current_path, 'metadata.json'),
    _namespace
)

_this_module = _sys.modules[__name__]


_js_dist = [
    {
        'relative_package_path': 'bundle.js',
        'external_url': (
            'https://{}/{}/{}'
            '/bundle.js'
        ).format(_cdn, _project, __version__),
        'namespace': _namespace
    }
]

_css_dist = [
    {
        'relative_package_path': 'dash_table_experiments.css',
        'external_url': (
            'https://{}/{}/{}'
            '/dash_table_experiments.css'
        ).format(_cdn, _project, __version__),
        'namespace': _namespace
    }
]


for _component in _components:
    setattr(_this_module, _component.__name__, _component)
    setattr(_component, '_js_dist', _js_dist)
    setattr(_component, '_css_dist', _css_dist)
