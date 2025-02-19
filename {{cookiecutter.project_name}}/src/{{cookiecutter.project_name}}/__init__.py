from __future__ import annotations

{% if cookiecutter.project_type == "setuptools" or cookiecutter.project_type == "pybind11" -%}
from ._version import version as __version__
{%- else -%}
__version__ = "0.1.0"
{%- endif %}

__all__ = ("__version__",)
