# test file
import heapq

def getMaximumThroughput(throughput, scaling_cost, budget):
    ##### Non optimal solution
    tc = throughput.copy()


    cost = 0

    while cost < budget:

        # O(N) - this is the biggest inefficiency
        i = tc.index(min(tc))

        c = scaling_cost[i]

        if c + cost <= budget:
            tc[i] += throughput[i]
            cost += c
        else:
            break

    # O(N)
    return min(tc)

########## OPTIMAL SOLUTION ##########
def getMaximumThroughput(throughput, scaling_cost, budget):
    # tc = throughput.copy()

    # O(N)
    tc = [(throughput[i], throughput[i], scaling_cost[i]) for i in range(len(throughput))]

    # O(N)
    heapq.heapify(tc)

    cost = 0

    # worst case O(budget/scaling[i]) where scaling cost is smallest and repeatedly triggered 
    while cost < budget:
        # print(l)

        # O(logN)
        i = heapq.heappop(tc)

        c = i[2]

        if c + cost <= budget:
            nt = i[0] + i[1]
            # O(logN)
            heapq.heappush(tc, (nt, i[1], i[2]))
            cost += c
        else:
            break

            # O(logN)
    ans = heapq.heappop(tc)
    return ans[0]

# Test cases

# Test case 1: Expected output 10
throughput = [4, 2, 7]
scaling_cost = [3, 5, 6]
budget = 32
output1 = getMaximumThroughput(throughput, scaling_cost, budget)
print(f"Test case 1 output: {output1}")
