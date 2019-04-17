import csv


class Node:

    def __init__(self, id, x, y, d, data=[]):
        self.id = id
        self.x = x
        self.y = y
        self.d = d
        self.data = []
        self.data.extend(data)
        self.connections = []

    def to_list(self):
        l = [self.id]
        l.extend([str(node) for node in self.connections])

        return l

    def __str__(self):
        return str(self.id)


class Map:

    def __init__(self, height, width, node_d):
        self.width = width
        self.height = height
        self.nodes = {}
        self.node_d = node_d

    def generate_nodes(self):
        # rows
        node_id = 0
        num_rows = self.height//self.node_d
        num_columns = self.width//self.node_d
        for i in range(num_rows):
            # columns
            for j in range(num_columns):
                self.nodes[node_id] = Node(node_id, i*self.node_d, j*self.node_d, self.node_d)
                node_id += 1

        # node_id is now one greater than the last node and can be used as a count
        node_count = node_id
        # create connections
        vertical_iter = [-1 * num_columns, 0, num_columns]
        horz_iter = [-1, 0, 1]
        for key in self.nodes.keys():
            for vert_d in vertical_iter:
                for horz_d in horz_iter:
                    connected_id = key + vert_d + horz_d
                    if horz_d == 0 and vert_d == 0:
                        continue
                    if connected_id < 0:
                        continue
                    if connected_id > node_count:
                        continue
                    if key % num_columns == 0 and horz_d < 0:
                        continue
                    if key % num_columns == num_columns - 1 and horz_d > 0:
                        continue
                    self.nodes[key].connections.append(connected_id)

    def write_to_csv(self):
        with open("nodes_connections.csv", "w+") as csv_file:
            writer = csv.writer(csv_file)
            for key in self.nodes:
                writer.writerow(self.nodes[key].to_list())


if __name__ == "__main__":
    map = Map(1500,750,50)
    map.generate_nodes()
    map.write_to_csv()
            









