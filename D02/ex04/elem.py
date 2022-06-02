#!/usr/bin/python3


class Text(str):
     def __str__(self):
        return super().__str__().replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace('\n', '\n<br />\n')

class Elem:
    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        self.tag = tag
        self.attr = attr
        self.content = content
        self.tag_type = tag_type

    def __str__(self):
        if self.tag_type == 'double':
            result = f"<{str(self.tag)}{self.__make_attr()}>{self.__make_content()}</{str(self.tag)}>"
        elif self.tag_type == 'simple':
            result = "<{0} {1}/>".format(str(self.tag), self.__make_attr())
       # print("-------" + result)
        return result

    def __make_attr(self):
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        if self.content is None:
            return ''
        if isinstance(self.content, Elem) == False and len(self.content) == 0:
            return ''
        if isinstance(self.content, Elem) or len(self.content) == 1:
            self.content = [self.content]

        result = '\n'
        #print(self.content)
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
        #print("========" + result)
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


if __name__ == '__main__':
    [...]
