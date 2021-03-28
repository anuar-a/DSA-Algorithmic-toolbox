# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    i = 0
    #write your code here
    for i in range(len(segments)-1):
        if len(points) == 0:
            points.append(segments[i].end)
        else:
            if points[len(points)-1] >= segments[i].start and points[len(points)-1] <= segments[i].end:
                continue
            else:
                points.append(segments[i].end)
    if points[len(points)-1] >= segments[len(segments)-1].start and points[len(points)-1] <= segments[len(segments)-1].end:
        return points
    else:
        points.append(segments[len(segments)-1].start)
        return points


    '''for i in range(len(segments)-1):

        if len(points) == 0:
            if segments[i].end < segments[i+1].start :
                points.append(segments[i].end)
            else:
                points.append(min(segments[i].end,segments[i+1].end))
        else:
            if points[len(points)-1] >= segments[i].start and points[len(points)-1] <= segments[i].end:
                continue
            else:
                if segments[i].end < segments[i+1].start :
                    points.append(segments[i].end)
                else:
                    if segments[i].start <= segments[i+1].start and segments[i].end >= segments[i+1].end:
                        continue
                    else:
                        points.append(min(segments[i].end,segments[i+1].end))
    if points[len(points)-1] >= segments[len(segments)-1].start and points[len(points)-1] <= segments[len(segments)-1].end:
        return points
    else:
        points.append(segments[len(segments)-1].start)
        return points'''

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(sorted(segments, key = lambda x: x.end))
    #print(sorted(segments, key = lambda x: x.end))
    print(len(points))
    for p in points:
        print(p, end=' ')
