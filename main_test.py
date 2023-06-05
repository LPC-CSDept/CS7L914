import main
import io
import sys
import re
import math
import types


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = 'Kim \n 100 80 70 60\n Bill \n 100 90 80 60 \n Mary \n 90 80 70 100'
    # sys.stdin = io.StringIO(datastr)

    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    mylist = [5, 10, 15, 25, 20, 55, 40]
    ret = main.gtRight(mylist)
    print(f'Return value is {ret}')
    assert isinstance(ret, list)
    assert len(ret) == 2
    assert ret == [25, 55]

    # regex_string = r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*3'
    # regex_string += r'[\w,\W]*5'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != None
    # print(res.group())


def test_main_2():
    mylist = [1, 2, 3, 4, 5]
    ret = main.gtRight(mylist)
    print(f'Return value is {ret}')
    assert isinstance(ret, list)
    assert len(ret) == 0
    assert ret == []
