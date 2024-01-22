import time
import matplotlib.pyplot as plt
import pandas as pd
from collections import deque
from heapq import heappop, heappush
from UserNode import UserNode
from Server import Server

from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)


defaultData = {
    "input":"",
    "source":""
}

serverMap = {}
maxRows = 35
maxCols = 25
serverlocations = {}
INF = 999
G = [[0, INF, INF, INF, INF, INF, INF, INF, 8],
     [INF, 0, 13, INF, INF, INF, 14, INF, 11],
     [INF, 13, 0, INF, INF, INF, INF, INF, INF],
     [INF, INF, INF, 0, 4, INF, INF, INF, INF],
     [INF, INF, INF, 4, 0, 7, INF, INF, INF],
     [INF, INF, INF, INF, 7, 0, 5, INF, INF],
     [INF, 14, INF, INF, INF, 5, 0, 8, 6],
     [INF, INF, INF, INF, INF, INF, 8, 0, INF],
     [8, 11, INF, INF, INF, INF, 6, INF, 0]]
adjList = {}

distance = list(map(lambda i: list(map(lambda j: j, i)), G))

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    start()
    if request.method == 'POST':
        defaultData['input'] = request.form["input"]
        defaultData['source'] = request.form["source"]
        return redirect(url_for('path'))    
    return render_template('index.html', defaultData=defaultData, serverMap = serverMap)

@app.route('/findPath', methods=['GET', 'POST'])
def path():
    if request.method == 'POST':
        defaultData['input'] = request.form["input"]
        defaultData['source'] = request.form["source"]
    print(defaultData)
    # print(serverMap[0].cache)
    data = defaultData["source"].split("-")
    x = int(data[2])
    y = int(data[1])
    user = UserNode(x,y)
    output = navigateFromUserToData(user, defaultData['input'])
    print(output)
    x = defaultData["source"].split("-")
    y = int(x[1])
    x = int(x[2])
    source = []
    source.append([y,x])
    
    
    return render_template('index.html', defaultData=defaultData, output=output, source=source, 
                           cells_to_color=output, serverMap = serverMap, bfs=bfs)

data = [["AB001", "AB123", "CB234"], ["BC120", "CB345", "DH190"], ["EH098", "AN390", "FH347"], 
            ["AX099", "AB001", "DX340"], ["FH347", "CP120", "XN490"], ["DH190", "CC909", "AN390"], 
            ["DP090", "IO901", "KK120"], ["DS209", "PO109", "EH098"], ["CS190", "CI222", "AN390"]]

def start():
    createServer(4, 6, data[0], 0)
    createServer(13, 4, data[1], 1)
    createServer(27, 6, data[2], 2)
    createServer(23, 16, data[3], 3)
    createServer(28, 20, data[4], 4)
    createServer(20, 23, data[5], 5)
    createServer(14, 19, data[6], 6)
    createServer(5, 23, data[7], 7)
    createServer(7, 15, data[8], 8)

    for row in range(len(G)):
        for col in range(len(G)):
            if G[row][col] != INF and G[row][col] != 0:
                serverMap[row].addNeighbor(serverMap[col], G[row][col])
                serverMap[col].addNeighbor(serverMap[row], G[row][col])

    
    getServerLocations()
    floyd_warshall()
    calculate_data_adjList(distance)
    update_lookups(adjList)


bfs = []
def findNearestServer(user):
    q = deque([[user.x, user.y]])
    print("x,y:",[user.x,user.y])
    directions = [ [-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
    visited = []
    visited.append([user.x, user.y])
    while q:
        for i in range(len(q)):
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr<=0 or nc<=0 or nr>maxRows or nc>maxCols or (nr,nc) in visited:
                    continue

                if (nr, nc) in serverlocations:
                    return [serverlocations[(nr, nc)], visited]
                
                visited.append([nr, nc])
                q.append([nr, nc])
    return None

def navigateFromUserToData(user, data):
    global bfs
    src, bfs = findNearestServer(user)
    print(src.number)
    path = navigateToData(src, data)
    result = []
    for serverNo in path:
        s = serverMap[serverNo]
        result.append([s.y, s.x])
    return result


def createServer(x, y, data, number):
    if x not in range(maxRows) or y not in range(maxCols):
        return
    server = Server(x, y, data, number)
    serverMap[number] = server




def getServerLocations():
    for serverNumber, server in serverMap.items():
        serverlocations[(server.x, server.y)] = serverMap[serverNumber]



def floyd_warshall():
    for k in range(len(G)):
        for i in range(len(G)):
            for j in range(len(G)):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])


def calculate_data_adjList(distance):
    for node in range(len(G)):
        for i, dist in enumerate(distance[node]):
            for data in serverMap[i].storage:
                if (node, data) not in adjList:
                    adjList[(node, data)] = (i, dist)
                else:
                    adjList[(node, data)] = (i, dist) if dist < adjList[(node, data)][1] else \
                        adjList[(node, data)]

def update_lookups(adjList):
    for node, data in adjList:
        serverMap[node].addLookup(data, adjList[(node, data)][0])

def navigateToData(src, data):
    if src.cache.get(data) != -1:
        return [src.number]
    if data not in src.lookup:
        return []
    dest = src.lookup[data]
    minHeap = [(0, src.number, src, [])]
    visited = set()
    while minHeap:
        distance, number, node, path = heappop(minHeap)
        if node in visited:
            continue
        visited.add(node)
        path.append(node.number)
        if node.number == dest:
            src.updateCache(data)
            serverMap[dest].updateCache(data)
            return path
        for nei, dist in node.neighbor:
            if nei not in visited:
                heappush(minHeap, (distance + dist, nei.number,  nei, path[:]))
    return []



if __name__ == '__main__':
    app.run(debug=True)
    



