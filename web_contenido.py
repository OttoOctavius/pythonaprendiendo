from urllib import request
import html.parser
import re  # para expresiones regulares, texto

# create a subclass and override the handler methods
class MyHTMLParser(html.parser.HTMLParser):

    def __init__(self):
        super(MyHTMLParser,self).__init__()
        self.resetflag()

    def resetflag(self):
        self.flag = False

    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)
        if tag == 'p':
            print("Encontrado el texto")
            self.flag = True

    def handle_endtag(self, tag):
        self.resetflag()
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        # Si el flag de lo que me interesa esta, hacer algo
        if self.flag == True:
            m = re.search('.doc', data) #'(?<=abc)def'
            if not m is None:
                print("Encontre algo util senpai.............")
        else:
            print("Encountered some data  :", data)
#TODO: Mejorar el manejo de los eventos con otro objeto
#TODO: Usar doc de exp reg.

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()

response = request.urlopen('http://python.org/')
pagina = response.read()

parser.feed(pagina.decode('utf-8'))
#programita

parser.close()
