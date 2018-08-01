'''
Basis for all site pages
'''

from views.file_ops import get_static_path

class Page:
    '''
    Page class is parent of all views and holds functions common to all of them
    '''
    def __init__(self):
        self.title = ""
        self.css = {}
        self.js = {}
        self.txt = {}
        self.meta = {}
        self.dict = {}

    def build_dict(self):
        '''
        Updates the dictionary with current instance variables
        '''
        vars = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]
        self.dict = dict(zip(vars, [getattr(self, var) for var in vars]))

    def add_css(self, file_name, alias=""):
        '''
        builds the path to a css file, and adds it to the dictionary

        optional alias is what this value will be called by in Jinja
        by default it is set to same as file_name
        '''
        alias = file_name if len(alias) == 0 else alias
        path = get_static_path('css', file_name)
        self.css[alias]=path        

    def add_js(self, file_name, alias=""):
        '''
        builds the path to a javascript file, and adds it to the dictionary

        optional alias is what this value will be called by in Jinja
        by default it is set to same as file_name
        '''

        alias = file_name if len(alias) == 0 else alias
        path = get_static_path('js', file_name)
        self.js[alias]=path

    def add_meta(self, file_name, alias=""):
        '''
        adds values to meta dictionary, for reference in Jinja
        '''

        alias = file_name if len(alias) == 0 else alias
        path = get_static_path('js', file_name)
        self.meta[alias]=path
