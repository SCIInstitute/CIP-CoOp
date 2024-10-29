# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import shlex
# sys.path.insert(0, os.path.abspath('.'))

import recommonmark
#from recommonmark.transform import AutoStructify

# -- Project information -----------------------------------------------------

project = 'SCI CIP CoOp'
copyright = '2024, The Scientific Computing and Imaging Institute at the University of Utah'
author = 'CIP CoOp'

# The full version, including alpha/beta/rc tags
version = '0.0'
release = '0.0.1'

github_doc_root = 'https://github.com/SCIInstitute/CIP-CoOp/tree/main/docs'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.napoleon',
        'recommonmark',
        'sphinxcontrib.bibtex',
        'sphinx_markdown_tables',
        'nbsphinx'
]

# Path for bibtex files
bibtex_bibfiles = ['references.bib']
bibtex_default_style = 'unsrt'
bibtex_encoding = 'latin'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

suppress_warnings = [
    'nbsphinx',
]

pygments_style = 'sphinx'

# the master toctree doc
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

#if not on_rtd:
import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = ['css/main.css']

html_title = project

html_logo = '_static/sci24-white.png'

html_theme_options = {
    'logo_only': True
}

