# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = 'Average of Squares'
copyright = '2025, Jingwen'
author = 'Jingwen'
release = '1.0'

# -- Path setup --------------------------------------------------------------
# ✨ 新增部分 ✨
# 告诉 Sphinx 去上一级目录（也就是 squares.py 所在处）找 Python 模块
import os
import sys
sys.path.insert(0, os.path.abspath('..'))


# -- General configuration ---------------------------------------------------

# ✨ 修改这里 ✨
# 启用自动文档生成扩展（autodoc），如果将来想支持 NumPy 风格可加 napoleon
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # 可选：支持 Google/NumPy 风格 docstring
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'
html_static_path = ['_static']