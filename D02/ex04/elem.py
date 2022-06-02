#!/usr/bin/python3


class Text(str):
    def __init__(self, s = ''):
        super(s)

    def __str__(self):
        return super().__str__().replace('\n', '\n<br />\n')


class Elem:
    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        self.tag = tag
        self.attr = attr
        self.content = content
        self.tag_type = tag_type

    def __str__(self):

        content = "\n  {0}\n".format(self.content)

        #result += content




        if self.tag_type == 'double':
            result = "<{0}>{1}</{0}>".format(str(self.tag), content)

        elif self.tag_type == 'simple':
            result = "<{0} {1}/>".format(str(self.tag), )
        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """

        if len(self.content) == 0:
            return ''
        result = '\n'
        for elem in self.content:
            result += [...]
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
