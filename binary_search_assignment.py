test0 = {
    'input': {
        'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
    },
    'output': 3
}
# A list of size 8 rotated 5 times.
test1 = {
    'input': {
        'nums': [4,5,6,7,8,1,2,3]
    },
    'output': 5
}
# A list that wasn't rotated at all.
test2 = {
    'input': {
        'nums': [1,2,3,4,5,6,7,8]
    },
    'output': 0
}
# A list that was rotated just once.
test3 = {
    'input': {
        'nums': [8,1,2,3,4,5,6,7]
    },
    'output': 1
}
# A list that was rotated n-1 times, where n is the size of the list.
test4 = {
    'input': {
        'nums': [2,3,4,5,6,7,8,1]
    },
    'output': 7
}
# A list that was rotated n times, where n is the size of the list
test5 = {
    'input': {
        'nums': [1,2,3,4,5,6,7,8]
    },
    'output': 0
}
# An empty list.
test6 = {
    'input': {
        'nums': []
    },
    'output': 0
}
# A list containing just one element.
test7 = {
    'input': {
        'nums': [1]
    },
    'output': 0
}
tests = [test0, test1, test2, test3, test3, test5, test6, test7]


def count_rotations_linear(nums):
    position = 0                 # What is the intial value of position?
    
    while position < len(nums):                     # When should the loop be terminated?
        
        # Success criteria: check whether the number at the current position is smaller than the one before it
        if position > 0 and nums[position-1] > nums[position]:   # How to perform the check?
            return position
        
        # Move to the next position
        position += 1
    
    return 0                     # What if none of the positions passed the check               

from jovian.pythondsa import evaluate_test_cases
evaluate_test_cases(count_rotations_linear, tests)

def count_rotations_binary(nums):
    lo = 0
    hi = len(nums) - 1
    
    while hi >= lo:
        mid = (lo + hi) // 2
        mid_number = nums[mid]
        
        # Uncomment the next line for logging the values and fixing errors.
        print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)
        
        if mid > 0 and nums[mid - 1] > mid_number:
            # The middle position is the answer
            return mid
        
        elif mid_number < nums[hi]:
            # Answer lies in the left half
            hi = mid - 1  
        
        else:
            # Answer lies in the right half
            lo = mid + 1
    
    return 0


binary_search_results = evaluate_test_cases(count_rotations_binary, tests)