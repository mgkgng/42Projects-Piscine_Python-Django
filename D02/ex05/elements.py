from elem import Text, Elem

class Html(Elem):
	def __init__(self, content=None):
		super().__init__("html", {}, content, "double")

class Head(Elem):
	def __init__(self, content=None):
		super().__init__("head", {}, content, "double")

class Body(Elem):
	def __init__(self, content=None):
		super().__init__("body", {}, content, "double")

class Title(Elem):
	def __init__(self, content=None):
		super().__init__("title", {}, content, "double")

class Meta(Elem):
	def __init__(self, content=None):
		super().__init__("meta", content, None, "simple")

class Img(Elem):
	def __init__(self, content=None):
		super().__init__("img", content, None, "simple")

class Table(Elem):
	def __init__(self, content=None):
		super().__init__("table", {}, content, "double")

class Th(Elem):
	def __init__(self, content=None):
		super().__init__("th", {}, content, "double")

class Tr(Elem):
	def __init__(self, content=None):
		super().__init__("tr", {}, content, "double")

class Td(Elem):
	def __init__(self, content=None):
		super().__init__("td", {}, content, "double")

class Ul(Elem):
	def __init__(self, content=None):
		super().__init__("ul", {}, content, "double")

class Ol(Elem):
	def __init__(self, content=None):
		super().__init__("ol", {}, content, "double")

class Li(Elem):
	def __init__(self, content=None):
		super().__init__("li", {}, content, "double")

class H1(Elem):
	def __init__(self, content=None):
		super().__init__("h1", {}, content, "double")

class H2(Elem):
	def __init__(self, content=None):
		super().__init__("h2", {}, content, "double")

class P(Elem):
	def __init__(self, content=None):
		super().__init__("p", {}, content, "double")

class Div(Elem):
	def __init__(self, content=None):
		super().__init__("div", {}, content, "double")

class Span(Elem):
	def __init__(self, content=None):
		super().__init__("span", {}, content, "double")

class Hr(Elem):
	def __init__(self, content=None):
		super().__init__("hr", content, None, "simple")

class Br(Elem):
	def __init__(self, content=None):
		super().__init__("br", content, None, "simple")

if __name__ == "__main__":
	print(Html([Head(Title(Text('\\"Hello ground!\\"'))), Body([H1(Text('\\"Oh no, not again!\\"')), Img({Text("src"): Text("http://i.imgur.com/pfp3T.jpg")})])]))