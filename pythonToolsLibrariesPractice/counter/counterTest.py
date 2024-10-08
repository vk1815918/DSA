# from collections import Counter

# list = ["a", "b", "c", "a", "b", "a", "a", "b"]

# c = Counter(list)
# print(c)
# for k, v in c.items():
#     print(k, " ", v)
    

from collections import Counter


# Problem Description:
# You are given two arrays of integers `a` and `b`, and an array `queries`.
# Each element in the `queries` array represents a query that can be one of the following two types:
# 
# 1. [0, i, x]: This query means you need to update `a[i]` to the value `x`.
# 2. [1, x]: This query asks to find the total number of pairs (i, j) such that a[i] + b[j] = x, where
#             `i` is an index from array `a` and `j` is an index from array `b`.
# 
# The task is to perform each query in order and return an array containing the results of queries
# of the type [1, x], which count the valid pairs.
#
# Example:
# a = [3, 4]
# b = [1, 2, 3]
# queries = [
#     [1, 5],  # Count pairs where a[i] + b[j] = 5
#     [0, 0, 1],  # Update a[0] to 1
#     [1, 5]  # Count pairs where a[i] + b[j] = 5 after the update
# ]
# Output: [2, 1]
#
# Explanation:
# Initially, for the query [1, 5], there are 2 pairs where a[i] + b[j] = 5: 
# (a[0] + b[1] = 3 + 2 = 5) and (a[1] + b[0] = 4 + 1 = 5).
# After updating a[0] to 1, for the query [1, 5], there is only 1 pair: (a[1] + b[0] = 4 + 1 = 5).



def solution(a, b, queries):
    af = Counter(a)
    bf = Counter(b)

    ans = []

    for query in queries:

        if query[0] == 0:
            af[a[query[1]]]-=1
            if af[a[query[1]]] == 0:
                del af[a[query[1]]]
                
            a[query[1]] = query[2]
            af[a[query[1]]]+=1
        else:
            count = 0

            for i in af:
                if query[1] - i in bf:
                    count+=af[i]*bf[query[1] - i]
            
            ans.append(count)

    return ans







# def solution(a, b, queries):
#     # Create frequency maps for array a and b
#     a_freq = Counter(a)
#     b_freq = Counter(b)

#     print(a_freq)
#     print(b_freq)
    
#     results = []
    
#     for query in queries:
#         if query[0] == 0:
#             # Update query: set a[i] = x
#             _, i, x = query
#             old_value = a[i]
#             a_freq[old_value] -= 1
#             if a_freq[old_value] == 0:
#                 del a_freq[old_value]
#             a[i] = x
#             a_freq[x] += 1
#         elif query[0] == 1:
#             # Count query: count pairs such that a[i] + b[j] = x
#             _, x = query
#             pair_count = 0
#             for bj in b_freq:
#                 # We are looking for a[i] such that a[i] + bj = x, hence a[i] = x - bj
#                 pair_count += a_freq[x - bj] * b_freq[bj]
#             results.append(pair_count)
    
#     return results

# Example usage:
a = [3, 4]
b = [1, 2, 3]
queries = [
    [1, 5],  # Count pairs such that a[i] + b[j] = 5
    [0, 0, 1],  # Update a[0] = 1
    [1, 5]  # Count pairs such that a[i] + b[j] = 5
]

result = solution(a, b, queries)
print(result)  # Output should be [2, 1]
