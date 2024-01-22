# Velocity Commerce

## Introduction
The topic is focused on the measures taken by a large e-commerce company, which has servers situated in different regions globally, to ensure that its website is accessible to users worldwide. The company has observed that certain users are encountering issues such as delayed page load times and prolonged wait times while attempting to finalize transactions on the website. To enhance user experience by optimizing data retrieval, the company decides to adopt a strategy that involves determining the most direct path among its servers. It utilizes network monitoring tools to gather information on the network's topology, which includes the servers' location and connectivity.

![Output Screenshot](https://github.com/karthikcd7/Velocity-Commerce/blob/main/Output.jpg)

## Defined Question
E-commerce has become an increasingly popular way for consumers to purchase goods and services, and as a result, e-commerce websites have become more complex, with more data to manage and retrieve. This has led to challenges in ensuring a smooth user experience, particularly for users who experience slow page load times and long wait times when completing transactions. A poor user experience can result in lost sales, reduced customer loyalty, and negative brand perception. As such, it's crucial for large e-commerce companies to optimize their data retrieval methods and improve the user experience on their websites. To achieve this goal, e-commerce companies must consider a range of strategies to reduce page load times and wait times for transactions. These strategies can include implementing content delivery networks (CDNs), caching, image and media optimization, prioritizing above-the-fold content, lazy loading, and data compression. By leveraging these strategies and continuously monitoring and optimizing performance, e-commerce companies can ensure a faster, more seamless user experience, which can lead to increased customer satisfaction, loyalty, and sales. Furthermore, as online shopping continues to grow in popularity and competition among e- commerce companies intensifies, optimizing data retrieval and improving the user experience has become more critical than ever. Companies that fail to keep up with user demands for fast
and reliable websites risk losing customers to competitors who provide a smoother user experience. Therefore, it's important for large e-commerce companies to invest in ongoing optimization efforts to stay ahead of the curve and meet the evolving needs of their customers.
What strategies can a large e-commerce company implement to optimize data retrieval and improve the user experience on its website, especially for users experiencing slow page load times and long wait times when completing transactions?

## Analysis:

### Algorithms:

#### BFS is used to find the nearest server.
- BFS stands for Breadth-First Search, which is a graph traversal algorithm used to explore and visit all the nodes of a graph or tree in a breadth-first manner. It starts at a designated starting node and explores all its neighboring nodes before moving on to the next level of nodes.
- In other words, BFS explores all the nodes at the same depth or level before moving on to explore the nodes at the next level. This process continues until all the nodes in the graph or tree have been explored.
- We use BFS for a variety of applications, including finding the shortest path between two nodes in an unweighted graph, checking if a graph is connected, finding all connected components in an undirected graph, and constructing a level-by-level tree traversal.
- BFS is a very efficient algorithm and has a time complexity of O(V+E), where V is the number of vertices and E is the number of edges in the graph. It is widely used in various fields, including computer science, data science, and artificial intelligence, for various applications such as web crawlers, social network analysis, and game AI.

#### FLOYD WARSHALL is used to get the get the distance among nodes.
- Floyd-Warshall is an algorithm for finding the shortest path between all pairs of vertices in a weighted graph. It uses dynamic programming to compute the shortest distances between all pairs of vertices in the graph. The algorithm works by considering all possible intermediate vertices between two vertices and updating the shortest path distances accordingly.
- We use the Floyd-Warshall algorithm in situations where we need to find the shortest path between all pairs of vertices in a graph. This can be useful in various applications such as network routing, traffic flow analysis, and scheduling problems.
- The main advantage of the Floyd-Warshall algorithm is that it can handle graphs with negative edge weights, unlike other shortest path algorithms like Dijkstra's algorithm. However, the time complexity of the Floyd-Warshall algorithm is O(V^3), where V is the number of vertices in the graph. Therefore, it is not suitable for large graphs with many vertices.
- Overall, the Floyd-Warshall algorithm is a powerful tool for finding the shortest paths between all pairs of vertices in a graph, and its ability to handle negative edge weights makes it a useful algorithm in various applications.

#### DIJKSTRAS – for finding shortest path.
- Dijkstra's algorithm is a shortest-path algorithm that is used to find the shortest path between a starting node and all other nodes in a weighted graph. The algorithm works by iteratively selecting the node with the smallest distance from the starting node and updating the distances of its neighboring nodes.
- We use Dijkstra's algorithm in situations where we need to find the shortest path between a starting node and all other nodes in a graph, such as in network routing, GPS navigation, and resource allocation problems.
- The main advantage of Dijkstra's algorithm is that it can handle graphs with non-negative edge weights, which makes it a popular choice for solving various real-world problems. Additionally, it is relatively easy to understand and implement compared to other shortest-path algorithms.
- However, Dijkstra's algorithm may not work well on graphs with negative edge weights, as it can get stuck in a loop of updating the distances between nodes. In such cases, we may need to use other algorithms such as Bellman-Ford or Floyd-Warshall to find the shortest path.
- Overall, Dijkstra's algorithm is a powerful and widely-used algorithm for finding the shortest path between a starting node and all other nodes in a graph with non-negative edge weights. Its simplicity and efficiency make it a popular choice for a variety of applications.

