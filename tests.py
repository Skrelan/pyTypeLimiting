import type_check as tc


class dummy:
    def __init__(self):
        self.name = "dummy"


def test_type_int():
    try:
        tc.type_int(1)
        tc.type_int(10, 11, 23)
        tc.type_int("1")
    except Exception as e:
        print e


def test_type_class():
    try:
        r = dummy()
        s = dummy()
        t = dummy()
        tc.type_class(dummy, r)
        tc.type_class(dummy, r, s, t)
        tc.type_class(dummy, r, 1, 2)

    except Exception as e:
        print e


def run_tests():
    tests = [test_type_int, test_type_class]
    for test in tests:
        print "\nRunning test {}()\n".format(test.__name__)
        test()


run_tests()
