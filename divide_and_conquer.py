test0 = {
    'input': {
        'poly1': [2, 0, 5, 7],
        'poly2': [3, 4, 2]
    },
    'output': [6, 8, 19, 41, 38, 14]
}
test1 = {
    'input': {
        'poly1': [2, 0, 5, 7],
        'poly2': [1]
    },
    'output': [2, 0, 5, 7]
}
test2 = {
    'input': {
        'poly1': [4],
        'poly2': [6]
    },
    'output': [24]
}
test3 = {
    'input': {
        'poly1': [2, 0, 5, 7],
        'poly2': [0]
    },
    'output': [0]
}
test4 = {
    'input': {
        'poly1': [0],
        'poly2': [0]
    },
    'output': [0]
}
test5 = {
    'input': {
        'poly1': [2, 0, 5, 7],
        'poly2': []
    },
    'output': []
} 
tests = [test0, test1, test2, test3, test4, test5]

def multiply_basic(poly1, poly2):
    if len(poly1) == 0 and len(poly2) != 0:
        return []
    elif len(poly2) == 0 and len(poly1) != 0:
        return []
    elif poly1 == [0] or poly2 == [0]:
        return [0]

    m = len(poly1) 
    n = len(poly2)
  
    result = [0] * (m + n - 1)
      
    # Multiply two polynomials term by term
      
    # Take ever term of first polynomial
    for i in range(m):
          
        # Multiply the current term of first 
        # polynomial with every term of 
        # second polynomial.
        for j in range(n):
            result[i + j] += poly1[i] * poly2[j];
  
    return result

# multiply([2, 0, 5, 7], [3, 4, 2])

from jovian.pythondsa import evaluate_test_cases

# evaluate_test_cases(multiply_basic, tests)

def add(poly1, poly2):
    """Add two polynomials"""
    result = [0] * max(len(poly1), len(poly2))
    for i in range(len(result)):
        if i < len(poly1):
            result[i] += poly1[i]
        if i < len(poly2):
            result[i] += poly2[i]
    return result

def split(poly1, poly2):
    """Split each polynomial into two smaller polynomials"""
    mid = max(len(poly1), len(poly2)) // 2
    return  (poly1[:mid], poly1[mid:]), (poly2[:mid], poly2[mid:])

def increase_exponent(poly, n):
    """Multiply poly1 by x^n"""
    return [0] * n + poly


def multiply_optimized_function(poly1, poly2):
    n = max(len(poly1), len(poly2))

    if n == 1 or len(poly2) == 1 or n == 0 or len(poly2) == 0:
        return multiply_basic(poly1, poly2)
    
    (A0, A1), (B0, B1) = split(poly1, poly2)

    y = multiply_optimized(add(A0, A1), add(B0,B1))
    u = multiply_optimized(A0, B0)
    z = multiply_optimized(A1, B1)

    z_exp = increase_exponent(z, 2*(n//2))
    y_exp = increase_exponent(add(y, [-x for x in add(u,z)]), n//2)
    result = add(add(u, y_exp), z_exp)

    return result 

def multiply_optimized(poly1, poly2):
    if len(poly1) == 0 and len(poly2) != 0:
        return []
    elif len(poly2) == 0 and len(poly1) != 0:
        return []
    else:
        return multiply_optimized_function(poly1, poly2)

evaluate_test_cases(multiply_optimized, tests)
