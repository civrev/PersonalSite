'''
Coordinates logic for homepage
'''

from views.page import Page

class Index(Page):
    '''
    Homepage class
    '''
    def __init__(self):
        super().__init__()
        self.title = "Christian Watts"
        self.add_css('normalize.min', 'normalize')
        self.add_css('main')
        self.add_js('vendor/jquery-1.11.2.min', 'jquery')
        self.add_js('main')
        self.build_dict()

