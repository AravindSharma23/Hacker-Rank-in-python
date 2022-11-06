"""
Hurdle race

"""




def hurdleRace(k, height):
    # Write your code here
    height.sort()
    high=height[-1]
    doses = high-k
    if high > k:
        return doses
    else:
        return 0
