__author__ = 'WangZhe'


class Node:
    __slots__ = 'name', 'father', 'son', 'is_root'

    def __init__(self, name):
        self.name = name
        self.father = self
        self.son = {}
        self.is_root = False

    def __str__(self):
        return str(self.name)


class SimplifyPath:

    def drive(self, path):
        path_list = self.prepare(path)
        current_ptr = self.main(path_list)
        output = self.output(current_ptr)
        return output

    def prepare(self, path_string):
        no_repeated_slash = []
        for i in range(len(path_string)):
            if not(i == 0 and path_string[0] == '/') and not (path_string[i] == '/' and path_string[i-1] == '/'):
                no_repeated_slash.append(path_string[i])
        if len(no_repeated_slash) != 0 and no_repeated_slash[-1] == '/':
            del no_repeated_slash[-1]
        no_repeated_slash = ''.join(no_repeated_slash)
        path_list = no_repeated_slash.split('/')
        return path_list

    def main(self, path_list):
        current_ptr = Node('root')
        current_ptr.is_root = True

        for i in path_list:
            if i == '..':
                current_ptr = current_ptr.father
            elif i == '.':
                current_ptr = current_ptr
            else:
                if current_ptr.son.get(i) is None:
                    tmp = Node(i)
                    tmp.father = current_ptr
                    current_ptr.son[i] = tmp
                    current_ptr = tmp
                else:
                    current_ptr = current_ptr.son[i]
        return current_ptr

    def output(self, current_ptr):
        stack = []
        while not current_ptr.is_root:
            stack.append(current_ptr.name)
            current_ptr = current_ptr.father
        output = []
        while len(stack) != 0:
            output.append(stack.pop())
        output = '/'.join(output)
        return '/' + output


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        return SimplifyPath().drive(path)

if __name__ == '__main__':
    print(SimplifyPath().drive('/'))

