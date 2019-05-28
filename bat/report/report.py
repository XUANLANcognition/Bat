#!/usr/bin/env python
# -*- config : utf-8 -*-

'help'

class Report(object):
    """
    You can wirte the report has created into a html file.
    """
    
    def __init__(self, headtitle, content):
        self.headtitle = 'Bat''s' + headtitle
        self.content = content


    def create():
        with open('./' + self.headtitle + '.html', 'w') as f:
            f.write(self.content)
