# Graph Navigator

## Author

Arina Andreeva

---

## Description

Graph Navigator is a console application for working with graphs.

The project demonstrates:

- Object-Oriented Programming

- BFS and DFS algorithms

- Dijkstra shortest path algorithm

- Factory design pattern

- JSON serialization

- Input validation

- Git and GitHub workflow

---

## Supported Graph Types

- Directed Graph

- Undirected Graph

- Weighted Graph

---

## Features

- Add and remove nodes

- Add and remove edges

- Breadth-First Search (BFS)

- Depth-First Search (DFS)

- Shortest path search

- Save graph to JSON

- Load graph from JSON

- Validation of incorrect input

---

## Technologies

- Python 3

- JSON

- OOP

- GitHub

---

## Project Structure

graphs/

algorithms/

storage/

main.py

README.md


---

## How to Run

python main.py


---

## Example Output

GRAPH NAVIGATOR

Graph:

A -> {'B': 5, 'C': 2}

B -> {'D': 3}

C -> {'D': 1}

D -> {}

BFS traversal:

['A', 'B', 'C', 'D']

DFS traversal:

['A', 'B', 'D', 'C']

Shortest path BFS:

['A', 'C', 'D']

Dijkstra shortest paths:

{'A': 0, 'B': 5, 'C': 2, 'D': 3}


---

## Validation Tests

The application checks:

- duplicate nodes

- negative weights

- nonexistent nodes

---

## GitHub Repository

This project was uploaded to GitHub with .gitignore support and commit history.
