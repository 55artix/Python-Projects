#==========================================
# Problem A
#
# Purpose: The function calculates the contracted distance between
#          the two objects in our reference frame in meters.
# Input Parameter(s):
# dist -- represents the original distance
#         between the two objects in meters
# speed -- represents the speed in meters/second at which we are
#          travelling relative to the two objects
# Return Value(s): the contracted distance between the two objects 
#                  from our reference frame in meters 
#==========================================
#
def length_contract(dist, speed):
    speed_light=3*10**8
    dist_contract=dist*(1-speed**2/speed_light**2)**0.5
    return dist_contract

#==========================================
# Problem B
#
# Purpose: The function calculates the time required to transverse
#          the segment from both a stationary observer's perspective and
#          Friedrich Bessel's perspective in years. 
# Input Parameter(s):
# speed -- represents Bessel's average speed in the run (meters/second)
# Return Value(s): the time required to transverse the segment as seen by Bessel in years.  
#==========================================
#
def bessel_run(speed):
    dist_stationary=12*3.086*10**16
    time_stationary=dist_stationary/speed/31557600.0
    print('The time required to travel ',dist_stationary,' meters, as seen by the stationary observer is ', time_stationary, ' years.')
    time_bessel= length_contract(dist_stationary,speed)/speed/31557600.0
    return time_bessel 
#==========================================
# Problem C
#
# Purpose: The function writes 'Who needs loops?' 100 times
#          without using any loops.
# Input Parameter(s): none
# Return Value(s):  none
#==========================================
#
def print_100():
    def print_10():
        print('Who needs loops?')
        print('Who needs loops?')
        print('Who needs loops?')
        print('Who needs loops?')
        print('Who needs loops?')
        print('Who needs loops?')
        print('Who needs loops?')
        print('Who needs loops?')
        print('Who needs loops?')
        print('Who needs loops?')
    def print_20():
        print_10()
        print_10()
    print_20()
    print_20()
    print_20()
    print_20()
    print_20()
