
import sphinx_rtd_theme

extensions = [
	'myst_parser',
	'sphinx_rtd_theme',
	]

source_suffix = [
	'.rst', 
	'.md'
]

project = u'NSDF Documents'
html_theme = "sphinx_rtd_theme"
master_doc = 'index'

html_static_path = ['_static']
html_logo = 'images/NSDF.png'
html_theme_options = {
	'logo_only': False,
	'display_version': False,
}