import os

def get_theme_dir():
    """
    Returns path to directory containing this package's theme.
    
    This is designed to be used when setting the ``html_theme_path``
    option within Sphinx's ``conf.py`` file.
    """
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "theme"))

def get_templates_dir():
    """
    Returns path to directory containing this package's templates.
    
    This is designed to be used when setting the ``templates_path``
    option within Sphinx's ``conf.py`` file.
    """
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "templates"))

def default_sidebars():
    """
    Returns a dictionary mapping for the templates used to render the
    sidebar on the index page and sub-pages.
    """
    return {
        '**': ['localtoc.html', 'searchbox.html'],
        'index': [],
        'search': [],
    }
