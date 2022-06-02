from elem import Elem

class Html(Elem):
	def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        self.tag = tag
        self.attr = attr
        self.content = content
        self.tag_type = tag_type

class Head(Elem):
	pass

class Body(Elem):
	pass

class Meta(Elem):
	pass

class Img(Elem):
	pass

class Table(Elem):
	pass

class Th(Elem):
	pass

class Tr(Elem):
	pass

class Td(Elem):
	pass

class Ul(Elem):
	pass

class Ol(Elem):
	pass

class Li(Elem):
	pass

class H1(Elem):
	pass

class H2(Elem):
	pass

class P(Elem):
	pass

class Div(Elem):
	pass

class Span(Elem):
	pass

class Hr(Elem):
	pass

class Br(Elem):
	pass