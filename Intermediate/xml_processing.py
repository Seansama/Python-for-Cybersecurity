# SAX
import xml.sax


class GroupHandler(xml.sax.ContentHandler):

    def startElement(self, title, attrs):
        self.current = title
        if self.current == 'book':
            print("-----BOOK-----")
            print('ID: {}'.format(attrs['id']))

    def characters(self, content):
        if self.current == 'title':
            self.title = content
        elif self.current == 'author':
            self.author = content
        elif self.current == 'genre':
            self.genre = content
        elif self.current == 'publication_year':
            self.publication_year = content
        elif self.current == 'price':
            self.price = content

    def endElement(self, name):
        if self.current == 'title':
            print("Title: {}".format(self.title))
        elif self.current == 'author':
            print("Author: {}".format(self.author))
        elif self.current == 'genre':
            print("Genre: {}".format(self.genre))
        elif self.current == 'publication_year':
            print("Publication Year: {}".format(self.publication_year))
        elif self.current == 'price':
            print("Price: {}".format(self.price))
        self.current = ''


handler = GroupHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('data.xml')
