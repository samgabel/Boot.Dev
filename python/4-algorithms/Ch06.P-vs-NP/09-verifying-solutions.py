# This example is meant to reaffirm the idea of "slow to solve, fast to verify"

# Calculate the number of combinations (only using lowercase english letters) are in and up to a password length.
# We want to calculate for length(1) + length(2) ... + length(n) amount of password combinations.



def get_num_guesses(length):
    total = 0
    for i in range(1, length + 1):
        total += 26 ** i
    return total



# --------------------------------------------



password = "password"
print(get_num_guesses(len(password)))
# 217180147158
