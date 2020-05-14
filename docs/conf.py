# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath("../"))
sys.setrecursionlimit(1500)


# -- Project information -----------------------------------------------------

project = "pycmc"
copyright = "2020, Musicfox, Inc. | musicfox.io"
author = "Jason R. Stevens, CFA"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "recommonmark",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.todo",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_logo = "_static/logo-dark-text.png"
html_favicon = "_static/favicon.ico"
html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "external_links": [{"name": "Musicfox", "url": "https://musicfox.io"},],
    "github_url": "https://github.com/musicfox/pycmc",
    "twitter_url": "https://twitter.com/musicfoxinc",
    "search_bar_text": "Search pycmc docs ...",
}
html_sidebars = {
    "**": [
        "util/searchbox.html",
        "util/sidetoc.html",
        "sourcelink.html",
        "relations.html",
    ]
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Add basic extension to take python docstrings
# autodoc

# -- Options for Syntax Highlighting -----------------------------------------
pygments_style = "colorful"

# -- Markdown support --------------------------------------------------------
# https://stackoverflow.com/a/56428123/5369706
import commonmark


def docstring(app, what, name, obj, options, lines):
    md = "\n".join(lines)
    ast = commonmark.Parser().parse(md)
    rst = commonmark.ReStructuredTextRenderer().render(ast)
    lines.clear()
    lines += rst.splitlines()


def setup(app):
    app.connect("autodoc-process-docstring", docstring)
