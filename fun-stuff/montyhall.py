from random import randint

N = 1000000

def simulate(N):
    K = 0
    # Determine which one has the car
    truth = randint(1,3)
    # Iterate 1000 times
    for i in range(N):
        # Determine first guess
        guess1 = randint(1,3)
        # If guess is correct, monte can be any
        if truth == guess1:
            monte = randint(1,3)
            # Make sure monte doesn't match the true value
            # (monte doesn't want to reveal it yet)
            while monte == truth:
                monte = randint(1,3)
        else:
            # monte is the one not correct and not guess1
            # logic: if truth = 1, guess1 = 2, monte = 3
            # logic2: if truth = 2, guess1 = 3, monte = 1,
            # therefore the function should always be correct!!
            monte = 6 - truth - guess1
        # Always make guess2 the value that is not guess1
        guess2 = 6 - guess1 - monte
        if guess2 == truth:
            K = K + 1
    return float(K) / float(N)
# Should be close to 0.66
print simulate(N)
