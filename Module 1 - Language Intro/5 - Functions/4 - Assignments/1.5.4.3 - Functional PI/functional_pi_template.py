import math


def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """

    ### YOUR CODE HERE ###
    a = 1
    b = 1 / math.sqrt(2)
    t = 1 / 4
    p = 1

    for i in range(1, 10):
        a_i = (a + b) / 2
        b_i = math.sqrt(a * b)
        t_i = t - (p * ((a - a_i) **2))
        p_i = 2 * p

        a = a_i
        b = b_i
        t = t_i
        p = p_i

    pi_estimate = ((a + b) ** 2) / (4 * t)

    # change this so an actual value is returned
    return pi_estimate


desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
