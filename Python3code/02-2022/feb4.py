def bracket(s):

    spec = ['()', '{}', '[]']
    while any(x in s for x in spec):
        for br in spec:
            s = s.replace(br, '')
    return not s

if __name__ == "__main__":
    test_s1 = "()[]{}"
    test_s2 = "(]"
    test_s3 = "()"
    test_s4 = "{[]}"
    test_s5 = "([)]"
    print(bracket(test_s1))
    print(bracket(test_s2))
    print(bracket(test_s3))
    print(bracket(test_s4))
    print(bracket(test_s5))
    #returns true
