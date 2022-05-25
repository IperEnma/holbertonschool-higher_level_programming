#!/usr/bin/python3
"""module matrix multi"""


def matrix_mul(m_a, m_b):
    """matrix multiply"""

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for x in m_a:
        if type(x) is not list:
            raise TypeError("m_a must be a list of lists")
    for x in m_b:
        if type(x) is not list:
            raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for x in m_a:
        for y in x:
            if type(y) is not float and type(y) is not int:
                raise TypeError("m_a should contain only integers or floats")

    for x in m_b:
        for y in x:
            if type(x) is not float and type(y) is not int:
                raise TypeError("m_b should contain only integers or floats")

    for x in m_a:
        savelen_a = len(m_a[0])
        if savelen_a != len(x):
            raise TypeError("each row of m_a must be of the same size")

    for x in m_b:
        savelen_b = len(m_b[0])
        if savelen_b != len(x):
            raise TypeError("each row of m_b must be of the same size")

    if savelen_a != savelen_b:
        raise ValueError("m_a and m_b can't be multiplied")

    new = [[i for i in x]for x in m_a]
    for x in range(len(new)):
        for y in range(len(new[x])):
            new[x][y] = 0

    for x in range(len(m_a)):
        for y in range(len(m_b[0])):
            for k in range(len(m_b)):
                new[x][y] += m_a[x][k] * m_b[k][y]
    return new
