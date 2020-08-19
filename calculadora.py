class Calculadora:
    def __init__(self):
        self.st = []
    
    def delim(self, c):
        return c == ' '
    
    def is_op(self, c):
        return c == '+' or c == '-' or c == '*' or c == '/'
    
    def priority(self, op):
        if op == '+' or op == '-':
            return 1
        if op == '*' or op == '/':
            return 2
        return -1
    
    def process_op(self, op):
        r = self.st.pop()
        l = self.st.pop()
        if op == '+':
            self.st.append(l + r)
        elif op == '-':
            self.st.append(l - r)
        if op == '*':
            self.st.append(l * r)
        if op == '/':
            self.st.append(l // r)
        
    def evaluate(self, s):
        self.st.clear()
        op = []
        i = 0
        while i < len(s):
            if self.delim(s[i]):
                i += 1
                continue
            if s[i] == '(':
                op.append(s[i])
            elif s[i] == ')':
                while op[-1] != '(':
                    self.process_op(op.pop())
                op.pop()
            elif self.is_op(s[i]):
                cur_op = s[i]
                while len(op) > 0 and self.priority(op[-1]) >= self.priority(cur_op):
                    self.process_op(op.pop())
                op.append(cur_op)
            else:
                number = 0
                while i < len(s) and s[i].isnumeric():
                    number = number * 10 + int(s[i])
                    i += 1
                i -= 1
                self.st.append(number)
            i += 1
        while len(op) > 0:
            self.process_op(op.pop())
        return self.st[-1]