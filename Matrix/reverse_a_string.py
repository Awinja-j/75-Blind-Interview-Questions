def reverse_string(s):
    count = len(s) -1
    ns = ''
    while count >= 0:
        ns += s[count]
        count -= 1
    return ns

print(reverse_string('joan'))