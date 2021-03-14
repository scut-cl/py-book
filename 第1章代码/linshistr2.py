def func(s):
    if len(s) < 1:
        return s
    return func(s[1:]) + s[0]


new_str = func("123456789")
print("new_str=", new_str)
