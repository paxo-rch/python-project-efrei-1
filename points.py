# TODO multiple players

global_points = {}

def register_points(name, points):
    if(name in global_points):
        if(points):
            global_points[name] = points
    else:
        global_points[name] = points