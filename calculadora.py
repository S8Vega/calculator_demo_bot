st = []

def delim(c):
    return c == ' '

def is_op(c):
    return c == '+' or c == '-' or c == '*' or c == '/'

def priority(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return -1

def process_op(op):
    r = st.pop()
    l = st.pop()
    if op == '+':
        st.append(l + r)
    elif op == '-':
        st.append(l - r)
    if op == '*':
        st.append(l * r)
    if op == '/':
        st.append(l // r)
    
def evaluate(s):
    st.clear()
    op = []
    i = 0
    while i < len(s):
        if delim(s[i]):
            i += 1
            continue
        if s[i] == '(':
            op.append(s[i])
        elif s[i] == ')':
            while op[-1] != '(':
                process_op(op.pop())
            op.pop()
        elif is_op(s[i]):
            cur_op = s[i]
            while len(op) > 0 and priority(op[-1]) >= priority(cur_op):
                process_op(op.pop())
            op.append(cur_op)
        else:
            number = 0
            while i < len(s) and s[i].isnumeric():
                number = number * 10 + int(s[i])
                i += 1
            i -= 1
            st.append(number)
        i += 1
    while len(op) > 0:
        process_op(op.pop())
    return st[-1]