# Definition of a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Main class containing the burning logic
class Solution:
    # Function to calculate minimum time to burn the entire tree from the target node
    def minTime(self, root, target):
        # Dictionary to build the graph as adjacency list
        graph = {}

        # Build the graph from the binary tree
        self.buildGraph(root, None, graph)

        # Set to keep track of visited (burned) nodes
        visited = set()

        # Queue for BFS starting from target node
        queue = [target]
        visited.add(target)

        # Variable to store total burn time
        time = 0

        # Perform BFS level by level
        while queue:
            size = len(queue)
            burned = False

            # Process all nodes at current BFS level
            for _ in range(size):
                node = queue.pop(0)
                for neighbor in graph.get(node, []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                        burned = True

            # Increment time if any new nodes burned in this level
            if burned:
                time += 1

        return time

    # Helper to convert binary tree to undirected graph
    def buildGraph(self, node, parent, graph):
        if not node:
            return

        # If parent exists, make bidirectional connection
        if parent:
            graph.setdefault(node.val, []).append(parent.val)
            graph.setdefault(parent.val, []).append(node.val)

        # Recurse to left and right children
        self.buildGraph(node.left, node, graph)
        self.buildGraph(node.right, node, graph)

# Driver code 
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.left.left.right = TreeNode(7)

    target = 1
    sol = Solution()
    print("Minimum time to burn the tree:", sol.minTime(root, target))

# Time complexity - 0(N)