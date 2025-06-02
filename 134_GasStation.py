class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        total_tank = 0
        curr_tank = 0
        start_station = 0
        
        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            if curr_tank < 0:
                start_station = i + 1
                curr_tank = 0

        return start_station if total_tank >= 0 else -1

if __name__ == "__main__":
    solver = Solution()

    gas1 = [1, 2, 3, 4, 5]
    cost1 = [3, 4, 5, 1, 2]
    resultado1 = solver.canCompleteCircuit(gas1, cost1)
    print(f"Exemplo 1:")
    print(f"Gas: {gas1}")
    print(f"Cost: {cost1}")
    print(f"Resultado: {resultado1}") 
    print("-" * 20)

    gas2 = [2, 3, 4]
    cost2 = [3, 4, 3]
    resultado2 = solver.canCompleteCircuit(gas2, cost2)
    print(f"Exemplo 2:")
    print(f"Gas: {gas2}")
    print(f"Cost: {cost2}")
    print(f"Resultado: {resultado2}") 
    print("-" * 20)

    gas3 = [5, 1, 2, 3, 4]
    cost3 = [4, 4, 1, 5, 1]
    resultado3 = solver.canCompleteCircuit(gas3, cost3)
    print(f"Exemplo 3:")
    print(f"Gas: {gas3}")
    print(f"Cost: {cost3}")
    print(f"Resultado: {resultado3}") 
    print("-" * 20)

    gas4 = [3,1,1]
    cost4 = [1,2,2]
    resultado4 = solver.canCompleteCircuit(gas4, cost4)
    print(f"Exemplo 4:")
    print(f"Gas: {gas4}")
    print(f"Cost: {cost4}")
    print(f"Resultado: {resultado4}") 
    print("-" * 20)
    
    gas5 = [7,1,0,11,4]
    cost5 = [5,9,1,2,5]
    resultado5 = solver.canCompleteCircuit(gas5, cost5)
    print(f"Exemplo 5:")
    print(f"Gas: {gas5}")
    print(f"Cost: {cost5}")
    print(f"Resultado: {resultado5}") 
    print("-" * 20)