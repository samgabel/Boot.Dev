# Given the initial followers count n, growth factor factor, and number of days days,
# return a list containing the exponential growth of followers for each day.

def exponential_growth(n, factor, days):
    followers = []
    for i in range(days + 1):
        followers.append(n * (factor ** i))
    return followers

# I guess that the exponent operation is an expensive computing process so finding a way to solve this without using
# exponent operations is more optimal...

def exponential_growth2(n, factor, days):
    followers = [n]
    for _ in range(days):
        followers.append(followers[-1] * factor)
    return followers


print(exponential_growth2(10, 2, 4))
# [10, 20, 40, 80, 160]
