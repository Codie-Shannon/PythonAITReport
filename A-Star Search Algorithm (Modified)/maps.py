import abc
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from node import Node


class Map:

    def __init__(self, h, w):
        self.h = h
        self.w = w

        # Build empty map
        self.map = np.zeros((h, w))
        
        
        
        # Add at least 5 other objects to the room
        self._add_circular_table_(30, 15, 5)
        self._add_circular_table_(15, 7, 4)
        self._add_circular_table_(30, 34, 4)
        self._add_circular_table_(16, 34, 3)
        self._add_rectangular_table_(17, 26, 5, 2)
        
        
        
        # Insert a bespoke object or wall
        # Wall 1 (Top Right)
        self.map[28, 0] = 1
        self.map[29, 0] = 1        
        self.map[28, 1] = 1
        self.map[29, 1] = 1        
        self.map[28, 2] = 1
        self.map[29, 2] = 1
        self.map[30, 2] = 1
        self.map[31, 2] = 1
        self.map[32, 2] = 1
        self.map[33, 2] = 1
        self.map[34, 2] = 1
        self.map[35, 2] = 1
        self.map[36, 2] = 1
        self.map[37, 2] = 1        
        self.map[28, 3] = 1
        self.map[29, 3] = 1
        self.map[30, 3] = 1
        self.map[31, 3] = 1
        self.map[32, 3] = 1
        self.map[33, 3] = 1
        self.map[34, 3] = 1
        self.map[35, 3] = 1
        self.map[36, 3] = 1
        self.map[37, 3] = 1        
        self.map[36, 4] = 1
        self.map[37, 4] = 1
        self.map[36, 5] = 1
        self.map[37, 5] = 1
        self.map[36, 6] = 1
        self.map[37, 6] = 1
        
        
        
        # Wall 2 (Bottom Left)
        self.map[0, 28] = 1
        self.map[0, 29] = 1        
        self.map[1, 28] = 1
        self.map[1, 29] = 1        
        self.map[2, 28] = 1
        self.map[2, 29] = 1
        self.map[2, 30] = 1
        self.map[2, 31] = 1
        self.map[2, 32] = 1
        self.map[2, 33] = 1
        self.map[2, 34] = 1
        self.map[2, 35] = 1
        self.map[2, 36] = 1
        self.map[2, 37] = 1        
        self.map[3, 28] = 1
        self.map[3, 29] = 1
        self.map[3, 30] = 1
        self.map[3, 31] = 1
        self.map[3, 32] = 1
        self.map[3, 33] = 1
        self.map[3, 34] = 1
        self.map[3, 35] = 1
        self.map[3, 36] = 1
        self.map[3, 37] = 1        
        self.map[4, 36] = 1
        self.map[4, 37] = 1
        self.map[5, 36] = 1
        self.map[5, 37] = 1
        self.map[6, 36] = 1
        self.map[6, 37] = 1
        
        
        
        # Wall 3 (Top Left)
        self.map[0, 1] = 1
        self.map[0, 2] = 1
        self.map[0, 3] = 1
        self.map[0, 4] = 1
        self.map[0, 5] = 1
        self.map[0, 6] = 1
        self.map[0, 7] = 1
        self.map[0, 8] = 1
        self.map[0, 9] = 1
        self.map[0, 10] = 1
        self.map[0, 11] = 1
        self.map[0, 12] = 1
        self.map[0, 13] = 1
        self.map[0, 14] = 1
        self.map[0, 15] = 1
        self.map[0, 16] = 1
        self.map[0, 17] = 1
        self.map[0, 18] = 1
        self.map[0, 19] = 1        
        self.map[1, 2] = 1
        self.map[1, 3] = 1
        self.map[1, 4] = 1
        self.map[1, 5] = 1        
        self.map[1, 6] = 1
        self.map[1, 7] = 1
        self.map[1, 8] = 1
        self.map[1, 9] = 1
        self.map[1, 10] = 1
        self.map[1, 11] = 1
        self.map[1, 12] = 1
        self.map[1, 13] = 1
        self.map[1, 14] = 1
        self.map[1, 15] = 1        
        self.map[2, 6] = 1
        self.map[2, 7] = 1
        self.map[2, 8] = 1
        self.map[2, 9] = 1
        self.map[2, 10] = 1
        self.map[2, 11] = 1
        self.map[2, 12] = 1
        self.map[2, 13] = 1        
        self.map[2, 0] = 1
        self.map[3, 0] = 1
        self.map[3, 1] = 1
        self.map[3, 2] = 1
        self.map[3, 3] = 1
        self.map[3, 4] = 1
        self.map[4, 4] = 1
        self.map[4, 5] = 1
        self.map[4, 6] = 1
        self.map[4, 7] = 1
        self.map[4, 8] = 1
        self.map[4, 9] = 1
        self.map[4, 10] = 1
        self.map[4, 11] = 1
        self.map[4, 12] = 1
        self.map[4, 13] = 1
        self.map[4, 14] = 1
        self.map[4, 15] = 1
        self.map[3, 15] = 1
        self.map[3, 16] = 1
        self.map[3, 17] = 1
        self.map[2, 17] = 1
        self.map[2, 18] = 1
        self.map[2, 19] = 1
        self.map[2, 20] = 1
        self.map[2, 21] = 1
        self.map[1, 21] = 1
        self.map[0, 21] = 1
        
        
                
    def _add_circular_table_(self, xc, yc, radii):

        for i in range(xc - radii, xc + radii + 1):
            for j in range(yc - radii, yc + radii + 1):
                if (i - xc) ** 2 + (j - yc) ** 2 <= radii ** 2:
                    self.map[i, j] = 1

    def _add_rectangular_table_(self, xc, yc, w, h):
        for i in range(xc - w, xc + w + 1):
            for j in range(yc - h, yc + h + 1):
                self.map[i, j] = 1
    
    # Checks if node is in range of map
    def _in_bounds_(self, node):
        return (node.x >= 0) and (node.x < self.h) and (node.y >= 0) and (node.y < self.w)

    def show(self, show_grid=True, do_show=True):

        cmap = matplotlib.colors.ListedColormap(['white', 'gray'])
        plt.imshow(self.map.T, cmap=cmap)

        if show_grid:
            plt.gca().grid(which='major', axis='both', linestyle='-', color='k',
                           linewidth=2, alpha=.7)
            plt.gca().set_xticks(np.arange(0 - .5, self.h, 1))
            plt.gca().set_yticks(np.arange(0 - .5, self.w, 1))
        else:
            plt.gca().set_xticks([])
            plt.gca().set_yticks([])

        if do_show:
            plt.show()

    def plot_path(self, path, figsize=(6, 6)):

        plt.figure(figsize=figsize)
        for i in range(len(path) - 1):
            plt.plot([path[i].x, path[i + 1].x],
                     [path[i].y, path[i + 1].y], c='r')
            #plt.plot([path[i][0], path[i + 1][0]],
                     #[path[i][1], path[i + 1][1]], c='r')
        self.show()

    @abc.abstractmethod
    def get_adjacent_nodes(self, node):
        return NotImplemented


class DiscreteMap(Map):
    hitList = []
        
    def get_adjacent_nodes(self, node):
        adjacent_nodes = []
    
        for i in range(-1, 2):
            for j in range(-1, 2):
                
                # Make sure within range
                if not (i == j):
                    new_node = Node(node.x + i, node.y + j)
                    if self._in_bounds_(new_node):
                        if self.map[new_node.x, new_node.y] == 0:
                            adjacent_nodes.append(new_node)
                        elif self.map[new_node.x, new_node.y] == 1 and new_node not in self.hitList:
                            self.hitList.append(new_node)
                            print('Object Hit: [{x}, {y}]'.format(x=new_node.x, y=new_node.y))

        return adjacent_nodes


class ContinuousMap(Map):

    def __init__(self, h, w, nodes, adjacency_matrix):

        super().__init__(h, w)
        self.nodes = nodes
        self.adjacency_matrix = adjacency_matrix

    def get_adjacent_nodes(self, node):

        adjacent_nodes = []

        index = self.nodes.index(node)
        for i in range(self.adjacency_matrix.shape[1]):
            if self.adjacency_matrix[index, i] == 1:
                adjacent_nodes.append(self.nodes[i])

        return adjacent_nodes

    def show(self, show_grid=False, do_show=True):

        super().show(show_grid=show_grid, do_show=False)

        # Plot nodes
        for node in self.nodes:
            plt.scatter(node.x, node.y, marker='+', s=100, c='C0')

        # Plot connections between nodes
        for i in range(self.adjacency_matrix.shape[0]):
            for j in range(self.adjacency_matrix.shape[1]):
                if self.adjacency_matrix[i, j] == 1:
                    plt.plot([self.nodes[i].x, self.nodes[j].x],
                             [self.nodes[i].y, self.nodes[j].y], c='k', alpha=0.2)
        if do_show:
            plt.show()


class ContinuousMap1:

    @classmethod
    def get_nodes(cls):
        return [Node(0, 0),
                Node(0.24, 1.36),
                Node(2.80, 0.83),
                Node(0.74, 4.45),
                Node(3.07, 3.11),
                Node(5, 5),
                Node(10, 0),
                Node(7, 0.9),
                Node(9.33, 4),
                Node(15, 6),
                Node(13, 1),
                Node(15.5, 2.8),
                Node(18, 0.4),
                Node(5, 13),
                Node(5.8, 15),
                Node(8, 12),
                Node(2, 7),
                Node(1.3, 9),
                Node(3.8, 10),
                Node(2.12, 11.47),
                Node(.66, 13.07),
                Node(.01, 15.8),
                Node(.5, 18.5),
                Node(2.88, 18.97),
                Node(7.86, 16.59),
                Node(5.91, 17.94),
                Node(11.32, 18.00),
                Node(12.35, 15.02),
                Node(11.81, 12.26),
                Node(16.14, 12.85),
                Node(18.5, 18.5),
                Node(18.3, 5.07),
                Node(18.65, 6.96),
                Node(16.46, 9.89),
                Node(18.25, 12.24),
                Node(17.76, 15.46)]

    @classmethod
    def get_adjacency_matrix(cls):

        adjacency_matrix = np.zeros((len(cls.get_nodes()), len(cls.get_nodes())))
        adjacency_matrix[0, 1] = 1
        adjacency_matrix[0, 2] = 1
        adjacency_matrix[1, 2] = 1
        adjacency_matrix[1, 3] = 1
        adjacency_matrix[1, 4] = 1
        adjacency_matrix[2, 4] = 1
        adjacency_matrix[2, 7] = 1
        adjacency_matrix[7, 6] = 1
        adjacency_matrix[6, 10] = 1
        adjacency_matrix[3, 4] = 1
        adjacency_matrix[4, 7] = 1
        adjacency_matrix[10, 12] = 1
        adjacency_matrix[12, 11] = 1
        adjacency_matrix[7, 8] = 1
        adjacency_matrix[8, 10] = 1
        adjacency_matrix[8, 9] = 1
        adjacency_matrix[9, 31] = 1
        adjacency_matrix[9, 32] = 1
        adjacency_matrix[31, 32] = 1
        adjacency_matrix[3, 5] = 1
        adjacency_matrix[4, 5] = 1
        adjacency_matrix[7, 5] = 1
        adjacency_matrix[8, 5] = 1
        adjacency_matrix[3, 16] = 1
        adjacency_matrix[5, 16] = 1
        adjacency_matrix[16, 17] = 1
        adjacency_matrix[16, 18] = 1
        adjacency_matrix[32, 33] = 1
        adjacency_matrix[33, 34] = 1
        adjacency_matrix[29, 33] = 1
        adjacency_matrix[29, 34] = 1
        adjacency_matrix[29, 35] = 1
        adjacency_matrix[34, 35] = 1
        adjacency_matrix[35, 30] = 1
        adjacency_matrix[17, 19] = 1
        adjacency_matrix[18, 19] = 1
        adjacency_matrix[19, 20] = 1
        adjacency_matrix[19, 13] = 1
        adjacency_matrix[20, 21] = 1
        adjacency_matrix[21, 22] = 1
        adjacency_matrix[22, 23] = 1
        adjacency_matrix[23, 25] = 1
        adjacency_matrix[13, 14] = 1
        adjacency_matrix[14, 25] = 1
        adjacency_matrix[13, 15] = 1
        adjacency_matrix[15, 28] = 1
        adjacency_matrix[28, 29] = 1
        adjacency_matrix[28, 27] = 1
        adjacency_matrix[27, 26] = 1
        adjacency_matrix[26, 24] = 1
        adjacency_matrix[14, 24] = 1
        adjacency_matrix[25, 24] = 1

        # Make adjacency matrix symmetric
        for i in range(adjacency_matrix.shape[0]):
            for j in range(adjacency_matrix.shape[1]):
                if adjacency_matrix[i, j] == 1:
                    adjacency_matrix[j, i] = 1

        return adjacency_matrix