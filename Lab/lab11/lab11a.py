from abc import ABC, abstractmethod, abstractproperty
from typing import List, Dict

class Node(ABC):
    def __init__(self, content:str, attributes:Dict):
        self.__children = []
        self.__attributes = attributes
        self.__content = content

    @property
    def content(self):
        return self.__content

    @property
    def children(self):
        return self.__children

    @property
    def attributes(self):
        return self.__attributes

    @abstractmethod
    def html(self):
        pass

    def appendChild(self, child):
        self.__children.append(child)

    def __iter__(self):
        self.__index = -1  # initialize index for each iteration
        return self

    def __next__(self):
        if self.__index >= len(self.__children)-1:
            raise StopIteration()
        self.__index += 1
        child = self.__children[self.__index]
        return child

class Div(Node):
    def html(self):
        str = '<div'
        for k, v in self.attributes.items():
            str += ' ' + k + '="' + v + '"'
        str += '>'

        # children
        for child in self.children:
            str += child.html()

        str += self.content


        str += '</div>'
        return str
    
    def text(self):
        print(self.html())

class B(Node):
    def html(self):
        str = '<b>'
        str += self.content
        str += '</b>'
        return str
    
    def text(self):
        print(self.html())
    
class Body(Node):        
    def html(self):
        str = '<body>' 
        for child in self.children:
            str += child.html()

        str += '</body>'
        return str
    
    def text(self):
        print(self.html())


class Title(Node):
    def html(self):
        str = '<title>'
        str += self.content
        str += '</title>'
        return str
    
    def text(self):
        print(self.html())

class Head(Node):
    def html(self):
        str = '<head>'
        for child in self.children:
            str += child.html()

        str += '</head>'
        return str
    
    def text(self):
        print(self.html())

class Html(Node):
    def html(self):
        str = '<!DOCTYPE html>'
        str += '<html'
        for k, v in self.attributes.items():
            str += ' ' + k + '="' + v + '"'
        str += '>'

        # children
        for child in self.children:
            str += child.html()
            

        str += self.content


        str += '</html>'
        return str
    
    def text(self):
        print(self.html())


def main():
     divAtts = {}
     divAtts['id'] = 'first'
     divAtts['class'] = 'foo'
     divA = Div('This is a test A', divAtts)
     divAtts = {}
     divAtts['id'] = 'second'
     divAtts['class'] = 'bar'
     divB = Div('This is a test B', divAtts)

     divAtts = {}
     divAtts['id'] = 'third'
     divAtts['class'] = 'dump'
     divC = Div('This is a test C', divAtts)
     b = B('This is a simple HTML file', {})
     divC.appendChild(b)

     body = Body('', {})
     body.appendChild(divA)
     body.appendChild(divB)
     body.appendChild(divC)

     title = Title('Example', {})
     head = Head('', {})
     head.appendChild(title)

     htmlAtts = {}
     htmlAtts['lang'] = 'en'
     html = Html('', htmlAtts)
     html.appendChild(head)
     html.appendChild(body)
     print(html.html())

if __name__ == "__main__":
    main()
