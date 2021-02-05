import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import json


# load mapping data
with open("test_mapping_data.json", "r") as read_file:
    mapping_data = json.load(read_file)
    odometry_data = mapping_data["odometry_vertices"]
    tag_data = mapping_data["tag_vertices"]

# print(mapping_data)
# print(odometry_data)
    

def parse_odometry():
    '''
    Parses odometry data and returns numpy translation arrays
    '''
    trans_x, trans_y, trans_z = [], [], []
    for pt in odometry_data:
        trans_x.append(pt["translation"]["x"])
        trans_y.append(pt["translation"]["y"])
        trans_z.append(pt["translation"]["z"])
    return np.array(trans_x), np.array(trans_y), np.array(trans_z)


def parse_tag():
    '''
    Parses tag data and returns numpy translation arrays
    '''
    trans_x, trans_y, trans_z = [], [], []
    for pt in tag_data:
        trans_x.append(pt["translation"]["x"])
        trans_y.append(pt["translation"]["y"])
        trans_z.append(pt["translation"]["z"])
    return np.array(trans_x), np.array(trans_y), np.array(trans_z)


def plot_translation_3D(x, y, z):
    # plot 3d plot
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.scatter(x, z, y)

    ax.set_title("Test Translation Mapping Data 3D Plot")
    ax.set_xlabel("x")
    ax.set_ylabel("z")
    ax.set_zlabel("y")

    plt.show()

def plot_translation_2D(x, z):
    fig, ax = plt.subplots()
    ax.scatter(x, z)
    ax.set(xlabel='x', ylabel='z',
        title='Test Translation Mapping Data 2D Plot')
    plt.show()


if __name__ == "__main__":
    x, y, z = parse_odometry()

    plot_translation_3D(x, y, z)
    plot_translation_2D(x, z)
    