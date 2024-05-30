# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- for custom bib style --
import pybtex.plugin
from pybtex.style.formatting.unsrt import BaseStyle, toplevel
from pybtex.style.template import field, sentence

class OnlyTitle(BaseStyle):
  def format_title(self, e, which_field):
    formatted_title = field(which_field)
    return formatted_title
  
  def get_article_template(self, e):
      template = toplevel [
        self.format_title(e, 'title'),
      ]
      return template
    
pybtex.plugin.register_plugin("pybtex.style.formatting", "onlytitle", OnlyTitle)
# --------

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '能源和人类未来'
copyright = '2024, Thomas W. Murphy, Jr.'
author = 'Thomas W. Murphy, Jr., Translator: Lin Lin'
release = ''

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# extensions = []
extensions = ['sphinx.ext.mathjax','sphinxcontrib.bibtex']

bibtex_bibfiles = ['refs.bib']
bibtex_default_style = "onlytitle"

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# autosectionlabel_prefix_document = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
# html_theme = 'classic'
# html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']
html_css_files = ["custom.css"]

html_theme = 'sphinx_book_theme'
html_theme_options = {
  "use_sidenotes": True,
}

# rst_prolog:
# A string of reStructuredText will be included at the beginning of every source file
# Support text color and size:
rst_prolog = """
 .. include:: <s5defs.txt>

 """

# Support color in Latex output:
latex_elements = {
    'passoptionstopackages': r'\PassOptionsToPackage{svgnames}{xcolor}',
    'preamble': r'''
\newcommand{\DUrolered}[1]{{\color{red} #1}}
''',
}