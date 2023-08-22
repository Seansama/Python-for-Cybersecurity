import xml.dom.minidom

domtree = xml.dom.minidom.parse('data.xml')
group = domtree.documentElement

books = group.getElementsByTagName('book')

for book in books:
    print('----BOOK----')
    if book.hasAttribute('id'):
        print('ID: {}'.format(book.getAttribute('id')))

    print("Title: {}".format(book.getElementsByTagName('title')[0].childNodes[0].data))
    print("Author: {}".format(book.getElementsByTagName('author')[0].childNodes[0].data))
    print("Genre: {}".format(book.getElementsByTagName('genre')[0].childNodes[0].data))
    print("Publication Year: {}".format(book.getElementsByTagName('publication_year')[0].childNodes[0].data))
    print("Price: {}".format(book.getElementsByTagName('price')[0].childNodes[0].data))

books[1].getElementsByTagName('title')[0].childNodes[0].nodeValue = 'New title'
domtree.writexml(open('data2.xml', 'w'))

newbook = domtree.createElement('book')
newbook.setAttribute('id', '4')

title = domtree.createElement('title')
title.appendChild(domtree.createTextNode('The 48 laws of power'))

author = domtree.createElement('author')
author.appendChild(domtree.createTextNode('Michael scott'))

genre = domtree.createElement('genre')
genre.appendChild(domtree.createTextNode('Self Help'))

publication_year = domtree.createElement('publication_year')
publication_year.appendChild(domtree.createTextNode('1996'))

price = domtree.createElement('price')
price.appendChild(domtree.createTextNode('25.60'))

newbook.appendChild(title)
newbook.appendChild(author)
newbook.appendChild(genre)
newbook.appendChild(publication_year)
newbook.appendChild(price)

group.appendChild(newbook)
domtree.writexml(open('data3.xml', 'w'))


