from typing import List 


from minmaxstack import simpleAssert

def collidingAsteroids(asteroids : List[int]) ->List[int]:
    stack = []

    for asteroid in asteroids:
        if asteroid > 0:
            stack.append(asteroid)
            continue
        
        while True:
            if len(stack) == 0 or stack[-1] < 0:
                stack.append(asteroid)
                break
            
            asteroidSize = abs(asteroid)
            if stack[-1] > asteroidSize:
                break 

            if asteroidSize == stack[-1]:
                stack.pop()
                break
            
            stack.pop()

    return stack


simpleAssert(collidingAsteroids([5]), [5])
simpleAssert(collidingAsteroids([-5]), [-5])
simpleAssert(collidingAsteroids([5, -5]), [])
simpleAssert(collidingAsteroids([1, 2, 3, 4, 5]),[1, 2, 3, 4, 5])
simpleAssert(collidingAsteroids([-6, -2, -10, -100, -30]),[-6, -2, -10, -100, -30])
simpleAssert(collidingAsteroids([1, 2, 3, -4]),[-4])