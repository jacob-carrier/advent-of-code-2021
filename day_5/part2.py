
from collections import Counter

def generate_points(f):
    points = []
    for line in f.readlines():
        line = line.rstrip('\n').split(' ')
        coordinate1 = line[0].split(',')
        x1 = int(coordinate1[0])
        y1 = int(coordinate1[1])
        
        coordinate2 = line[-1].split(',')
        x2 = int(coordinate2[0])
        y2 = int(coordinate2[1])

        if x1 != x2 and y1 != y2:
            while x1 != x2 and y1 != y2:
                points.append((x1, y1))
                if x1 > x2:
                    x1 -= 1
                else:
                    x1 += 1
                if y1 > y2:
                    y1 -= 1
                else:
                    y1 += 1
            points.append((x1, y1))
            continue

        if x1 > x2:
            tempx = x1
            x1 = x2
            x2 = tempx
        
        if y1 > y2:
            tempy = y1
            y1 = y2
            y2 = tempy
        # Some of the values are in the reverse direction as well, going both
        # left to right, as well as up and down, so we need to factor that in
        # when calling range() if we want positive numbers or for range not to stop
        # of it's own accord
        if x1 == x2:
            points = points + [(x1, y) for y in range(y1, y2+1)]

        if y1 == y2:
            points = points + [(x, y1) for x in range(x1, x2+1)]
            
    return points

if __name__ == '__main__':
    with open('./sample.txt') as f:
        points = generate_points(f)
        counted_list = Counter(points).most_common()
        high_intersection_points = sum([1 for item in counted_list if item[1] > 1])
        print(f"Number of highest intersected points: {high_intersection_points}")