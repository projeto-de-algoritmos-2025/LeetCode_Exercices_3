class Solution(object):
    def candy(self, ratings):
        n = len(ratings)
        candies = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
                print(f"Updated candies after checking right neighbor at index {i}: {candies}")

        return sum(candies)

if __name__ == "__main__":
    solver = Solution()

    ratings1 = [1, 0, 2]
    result1 = solver.candy(ratings1)
    print(f"Ratings: {ratings1}, Candies: {result1}")

    ratings2 = [1, 2, 2]
    result2 = solver.candy(ratings2)
    print(f"Ratings: {ratings2}, Candies: {result2}")

    ratings3 = [1, 3, 2, 2, 1]
    result3 = solver.candy(ratings3)
    print(f"Ratings: {ratings3}, Candies: {result3}")

    ratings4 = [1, 2, 87, 87, 87, 2, 1]
    result4 = solver.candy(ratings4)
    print(f"Ratings: {ratings4}, Candies: {result4}")

    ratings5 = [1, 6, 10, 8, 7, 3, 2]
    result5 = solver.candy(ratings5)
    print(f"Ratings: {ratings5}, Candies: {result5}")