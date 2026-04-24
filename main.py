# Pinball Simulation
# Goal: Simulate the logic of the Pinball mini-game to determine the expected value of playing the game
#  and to practice coding with AI assistance.
# These "casual games" are usually designed so that you cannot win and this one is relatively simple.
# From basic testing, it appears that although you can alter the number of balls per round, they do not collide.
# I will infer this to mean that the number of balls played does not affect the outcome.
# You can also change the bet per ball but this also does not affect the outcome.
# The game board is setup in a triangular pattern 8 layers deep and in each layer the ball 
# can fall to the left or right. The bucket that the ball falls into determines the payout.
# This leaves us with a simple binomial distribution problem where we can calculate the expected value
#  of playing the game by summing the products of the probabilities of landing in each bucket and their corresponding payouts.
#
#                               o 
#                             o   o
#                           o   o   o
#                         o   o   o   o
#                       o   o   o   o   o
#                     o   o   o   o   o   o
#                   o   o   o   o   o   o   o
#                 o   o   o   o   o   o   o   o
#           11x|3.5x|1.5x|0.6x|0.2x|0.6x|1.5x|3.5x|11x

import math

def binomial_coefficient(n, k):
    return math.comb(n, k)

def expected_value():
    n = 8
    total_paths = 2 ** n
    payouts = [11, 3.5, 1.5, 0.6, 0.2, 0.6, 1.5, 3.5, 11]
    ev = 0
    for k in range(n + 1):
        prob = binomial_coefficient(n, k) / total_paths
        ev += prob * payouts[k]
    return ev

print(f"Expected value per ball: {expected_value():.4f}")

# The expected value per ball is 0.95 in the structure of this game.
#
# In the future, I might explore this game at scale with very large binomial 
# coefficients and create a more complex simulation to determine what payouts
# would be necessary to operate a game at such a scale profitably.