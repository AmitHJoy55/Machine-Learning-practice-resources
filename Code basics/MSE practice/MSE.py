import numpy as np

def gradient_descent(x,y):
    m_curr = b_curr = 0
    itr = 10000
    n = len(x)
    learning_rate = 0.01
    for i in range(itr):
        y_predicted = m_curr * x + b_curr
        cost = -(1/n) * sum ([val ** 2 for val in (y- y_predicted)])
        md = - (2/n) * sum (x * (y - y_predicted))
        bd = - (2/n) * sum  (y - y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print("m {}, b {}, iteration {}, cost {}".format(m_curr, b_curr, itr, cost))

x = np.array([1,2,3,4,5])
y = np.array([7,9,11,13,15])

gradient_descent(x,y)
