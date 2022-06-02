#!/usr/bin/python3


from re import L


class Text(str):
     def __str__(self):
        if str == '"':
            return super().__str__().replace('"', "&quot;")
        return super().__str__().replace('<', '&lt;').replace('>', '&gt;').replace('\n', '\n<br />\n')

class Elem:
    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        if content != None and not Elem.check_type(content):
            raise Elem.ValidationError
        self.tag = tag
        self.attr = attr
        self.content = []
        if content:
            self.add_content(content)
        self.tag_type = tag_type

    def __str__(self):
        if self.tag_type == 'double':
            result = f"<{str(self.tag)}{self.__make_attr()}>{self.__make_content()}</{str(self.tag)}>"
        elif self.tag_type == 'simple':
            result = f"<{str(self.tag)}{self.__make_attr()} />"
        return result

    def __make_attr(self):
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        if self.content is None:
            return ''
        #if isinstance(self.content, Elem) == False and len(self.content) == 0:
            return ''
        #if isinstance(self.content, Elem) or len(self.content) == 1:
        #    self.content = [self.content]

        result = '\n'
        for elem in self.content:
            if elem is None:
                pass
            elif isinstance(elem, str) and len(elem) == 0:
                pass
            elif isinstance(elem, Elem):
                before = elem.__str__().split('\n')
                for line in before:
                    result += f"  {line}\n"
            else:
                result += f"  {elem}\n"
        if result == '\n':
            result = ""
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))

    class ValidationError(Exception):
        def __init__(self):
            super().__init__(self, "Validation error")

if __name__ == "__main__":
    print(Elem("html", {}, [Elem("head", {}, Elem("title", {}, Text('"Hello ground!"'), "double"), "double"), Elem("body", {}, [Elem("h1", {}, Text('"Oh no, not again!"'), "double"), Elem("img", {"src": "http://i.imgur.com/pfp37.jpg"}, None, "simple")], "double")], "double"))