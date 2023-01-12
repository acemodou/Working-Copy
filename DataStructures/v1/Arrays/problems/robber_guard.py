import math

# This is an infinite loop 

def computeChanges(guardX, guardY, speed, targetX, targetY):
    '''
    Calculate the angle of depressiion 
    Guard is moving towards the target
    Target is moving towards the door
    '''
    bigTriangewidth = guardX - targetX
    bigTriangeHeight = guardY - targetY
    bigTriangleRatio = bigTriangewidth / bigTriangeHeight
    angleOfDepression = math.atan(bigTriangleRatio)

    ratioX = math.sin(angleOfDepression)
    ratioY = math.cos(angleOfDepression)
    changeX = ratioX * speed
    changeY = ratioY * speed

    guardX += math.copysign(changeY, bigTriangewidth * -1)
    guardY += math.copysign(changeY, bigTriangeHeight * -1)

def abs_distance(X1, X2, Y1, Y2):
    '''
    Distance between pints in a cartesian plane
    '''
    P1 = X2- X1 
    P2 = Y2 - Y1
    PQ = math.sqrt(P1 * P1 + P2 * P2)
    return abs(PQ)

def normalizeSpeeds(speed1, speed2, maxSpeed):
    '''
    Normalize the two speeds not to be too far from each other
    '''
    largest_speed = speed1
    if speed2 > largest_speed:largest_speed = speed2
    speed1 = (speed1 / largest_speed) * maxSpeed
    speed2 = (speed2 / largest_speed) * maxSpeed


if __name__=="__main__":
    
    # Thief coordinates 
    robberX = -10.0
    robberY = 100.0
    robberSpeed = 13

    # Guard coordinates 
    guardX = -5.0
    guardY = 115.0
    guardSpeed = 11

    normalizeSpeeds(robberSpeed, guardSpeed, 0.1)

    doorX = 0.0
    doorY = 0.0 

    closeEnough = 0.2 


    while(abs_distance(robberX, robberY, guardX, guardY) > closeEnough \
          and abs_distance(robberX, robberY, doorX, doorY) > closeEnough):
          computeChanges(robberX, robberY, robberSpeed, doorX, doorY)
          computeChanges(guardX, guardY, guardSpeed, robberX, robberY)

          if abs_distance(robberX, robberY, doorX, doorY) <= closeEnough:
              print(f'Robber escapes.\n GuardX: {guardX} GuardY: {guardY} \n')
          if abs_distance(robberX, robberY, guardX, guardY) <= closeEnough:
              print(f'Guard reaches robber.\n RobberX: {robberX} RobberY: {RobberY} \n GuardX: {guardX} GuardY: {guardY} \n')



    
