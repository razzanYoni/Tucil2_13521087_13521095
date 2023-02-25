from main import *

"""DEBUG MODE"""	
if __name__ == '__main__':

    fileName = './txt/tc3.txt'

    arrOfPoints = []
    dimension:int
    n:int

    with open(fileName, 'r') as f:
        for line in f:
            temp = line.split(', ')
            point = []
            dimension = len(temp)
            for num in temp :
                point = point + [float(num)]
            arrOfPoints = arrOfPoints + [point]
    
    f.close()
    
    n = len(arrOfPoints)

    timeBruteForce = currentTime()
    point1BF, point2BF, minDistanceBF = getClosestPairByBruteForce(arrOfPoints, n, dimension)
    timeBruteForce = currentTime() - timeBruteForce

    timeDivideNConquer = currentTime()
    point1DC, point2DC, minDistanceDC= getClosestPairByDivideNConquer(arrOfPoints, n, dimension)
    timeDivideNConquer = currentTime() - timeDivideNConquer

    print("Closest pair is Using Brute Force: ")
    print("Point A: ", point1BF)
    print("Point B: ", point2BF)
    print("Distance: ", minDistanceBF)
    print("Time: ", timeBruteForce)

    print()

    print("Closest pair is Using Divide and Conquer: ")
    print("Point A: ", point1DC)
    print("Point B: ", point2DC)
    print("Distance: ", minDistanceDC)
    print("Time: ", timeDivideNConquer)