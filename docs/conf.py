# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SWAN'
copyright = '2011-2026, TU Delft'
author = 'Marcel Zijlema'
version = 'v41.51'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.githubpages',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'

# includes SWAN logo
html_logo = html_favicon = '_images/swanlogo.png'

# edit on GitHub
html_context = dict()
html_context['display_github'] = True
html_context['github_user'] = 'delftwaves'
html_context['github_repo'] = 'swan-docs'
html_context['github_version'] = 'main/docs/'
