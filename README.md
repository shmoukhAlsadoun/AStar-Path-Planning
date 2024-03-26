<body>
  <h1>A* Path Finding Algorithm Game</h1>
  
  <h2>Overview</h2>
  <p>
    This repository contains a Python implementation of the A* search algorithm for path finding in a grid-based environment. The A* algorithm is a popular path finding algorithm that guarantees finding the shortest path from a start point to an end point in a graph or grid.
  </p>

  <h2>How it Works</h2>
  <p>
    The program uses the Pygame library to create a graphical interface where you can set the start point, end point, and obstacles on a grid. The A* algorithm then finds the shortest path from the start point to the end point, avoiding the obstacles.
  </p>
  <p>
    The A* algorithm works by exploring the neighboring nodes of the current node and calculating a heuristic score for each neighbor. The heuristic score is a combination of the cost to reach the neighbor from the start point (known as the "g" score) and an estimate of the remaining cost to reach the end point (known as the "h" score). The algorithm selects the neighbor with the lowest heuristic score and continues the search until the end point is reached.
  </p>

  <h2>Prerequisites</h2>
  <p>
    To run this program, you need to have Python 3 installed on your computer. Additionally, you need to install the Pygame library, which can be done using the following command:
  </p>
  <pre><code>pip install pygame</code></pre>

  <h2>Usage</h2>
  <ol>
    <li>Run the program by executing the <code>main.py</code> file.</li>
    <pre><code>python main.py</code></pre>
    <li>Once the graphical interface appears, you can set the start point by left-clicking on a spot on the grid.</li>
    <li>Set the end point by left-clicking on another spot on the grid.</li>
    <li>Set obstacles by left-clicking on the desired spots. To remove obstacles, right-click on them.</li>
    <li>Press the <strong>Space</strong> key to start the A* algorithm and find the shortest path.</li>
    <li>Press the <strong>C</strong> key to clear the grid and reset the start and end points.</li>
  </ol>

  <h2>Credits</h2>
  <p>
    This program is based on the A* search algorithm and uses the Pygame library for visualization.
  </p>

  <h2>License</h2>
  <p>
    This project is licensed under the <a href="https://opensource.org/licenses/MIT">MIT License</a>.
  </p>
</body>
</html>
