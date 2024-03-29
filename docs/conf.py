"""
Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html

Path Setup
"""
import os
import sys

sys.path.insert(0, os.path.abspath("../src"))

import rosetta_lang

# General configuration
# ---------------------

project = rosetta_lang.__package__

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.doctest",
    "sphinx_autodoc_typehints",
    "sphinx_rtd_theme",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

"""
Project Information

# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
"""
locale_dirs = ["locale/"]
gettext_compact = False

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["output", "_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

"""
List of patterns, relative to source directory, that match files and
directories to ignore when looking for source files. This pattern also affects
html_static_path and html_extra_path.
"""

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.doctest",
    "sphinx_autodoc_typehints",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "lark-parser": ("https://lark-parser.readthedocs.io/en/latest/", None),
}

html_theme = "sphinx_rtd_theme"
