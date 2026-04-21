# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'user_manual'
copyright = '2024, i-soft'
author = 'i-soft'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []



templates_path = ['_templates']
exclude_patterns = []
suppress_warnings = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

extensions.append("sphinx_wagtail_theme")
html_theme = 'sphinx_wagtail_theme'
html_static_path = ['_static']
# 让每个页面都加载你的切换器脚本/样式
html_js_files = [
    'version-switcher-static.js',
]
html_css_files = [
    'version-switcher.css',
]
# Theme options
html_theme_options = {
    'logo': 'img/xmen_logo.png',
    'logo_alt': 'EasyXMen',
    'logo_height': 59,
    'logo_width': 45,
    'logo_url': '',
    'project_name': '开源小满EasyXMen',
}