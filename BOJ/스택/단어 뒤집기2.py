import sys

s = sys.stdin.readline().rstrip()
tag = False
res = ''
stack = ''

for word in s:
    if tag == False:
        if word == '<':
            tag = True
            stack += word
        elif word == ' ':
            res += stack +' '
            stack = ''
        else:
            stack = word + stack
    else:
        if word == '>':
            tag = False
            stack += word
            res += stack
            stack = ''
        else:
            stack += word

print(res + stack)