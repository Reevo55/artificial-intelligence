def connectStartEnd(start, end):
    print(f'Connection {start} and {end}')
    connectionArr = []

    x = start.x
    y = start.y

    while True:
        if(x > end.x):
            x = x - 1
        elif(x < end.x):
            x = x + 1
        else:
            break

        point = Point(x, y)
        connectionArr.append(point)

        print(point)

    while True:
        if(y > end.y):
            y = y - 1
        elif(y < end.y):
            y = y + 1
        else:
            break

        point = Point(x, y)
        connectionArr.append(point)

    return connectionArr


def fillConnections(plate):
    for connection in plate.connections:
        points = connectStartEnd(connection.start, connection.end)
        connection.setPath(points)
        print('Connection path:')
        print(connection.getPath())

def connectPlatesConnections(plates):
    for plate in plates:
        fillConnections(plate)
