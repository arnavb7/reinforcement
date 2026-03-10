# analysis.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2():
    answerDiscount = 0.9
    # changed answerNoise to 0 to make policy deterministic, no slipping off bridge
    answerNoise = 0
    return answerDiscount, answerNoise

def question3a():
    # low discount for close exit, no noise for cliff safety, no living reward to deincentivize living
    answerDiscount = 0.3
    answerNoise = 0.0
    answerLivingReward = 0.0
    return answerDiscount, answerNoise, answerLivingReward

def question3b():
    # low discount for close exit, noise for cliff avoidance, no living reward to deincentivize living
    answerDiscount = 0.3
    answerNoise = 0.1
    answerLivingReward = 0.0
    return answerDiscount, answerNoise, answerLivingReward

def question3c():
    # high discount for far exit, no noise for cliff safety, no living reward to deincentivize living
    answerDiscount = 0.9
    answerNoise = 0.0
    answerLivingReward = 0.0
    return answerDiscount, answerNoise, answerLivingReward

def question3d():
    # high discount for far exit, noise for cliff avoidance, no living reward to deincentivize living
    answerDiscount = 0.9
    answerNoise = 0.1
    answerLivingReward = 0.0
    return answerDiscount, answerNoise, answerLivingReward

def question3e():
    answerDiscount = 0.0
    answerNoise = 0.0
    answerLivingReward = 1
    return answerDiscount, answerNoise, answerLivingReward

def question8():
    answerEpsilon = None
    answerLearningRate = None
    return answerEpsilon, answerLearningRate
    # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
    print('Answers to analysis questions:')
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print('  Question %s:\t%s' % (q, str(response)))
