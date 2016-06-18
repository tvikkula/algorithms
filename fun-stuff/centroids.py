from collections import namedtuple

Point = namedtuple("Point", ["x","y"])
centroids = [Point(44,105),Point(55,63)]
points = {Point(50,130):0,Point(65,140):0,Point(38,115):0,Point(55,118):0,Point(50,90):0,Point(63,88):0,Point(43,83):0,Point(50,60):0}

def euclidian(point1, point2):
    return sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

def kmeans(centroids, points):
    # End condition(s): If centroids don't change (converge)
    # calculate which centroid the points belong to. For each of these
    # new points calculate the centroid.
    # How to define the cluster for each point? Tuples are immutable so 
    # it is inefficient to create a new one each time --> use a map.
    for point, k in points.items():
        length = 9999 # positive infinity
        for k in centroids:
            # Calculate distance to centroid:
            newLength = euclidian(point, k)
            if (newLength < length):
                length = newLength
                point
    
