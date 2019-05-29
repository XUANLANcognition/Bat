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

    def replace(self):
        self.content = self.content.replace('\n', '<br>')
        self.content = self.content.replace('###', '')
        self.content = self.content.replace('[', '<h3>')
        self.content = self.content.replace(']', '</h3>')

    def create(self):
        self.replace()
        self.content = '<h1>' + self.headtitle + ' Report</h1>' + self.content
        with open('./' + self.headtitle + '.html', 'w') as f:
            f.write(self.content)
