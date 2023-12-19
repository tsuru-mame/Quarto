import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot


class Visualization:
    def __init__(self) -> None:
        self.board = np.array([[np.nan]*4]*4)
        self.board_path = 'stl/quarto_board.stl'
        self.block_paths = {
            0 : 'stl/big_cube_hole.stl',
            1 : 'stl/big_cube_nohole.stl',
            2 : 'stl/big_round_hole.stl',
            3 : 'stl/big_round_nohole.stl',
            4 : 'stl/small_cube_hole.stl',
            5 : 'stl/small_cube_nohole.stl',
            6 : 'stl/small_round_hole.stl',
            7 : 'stl/small_round_nohole.stl',
            8 : 'stl/big_cube_hole.stl',
            9 : 'stl/big_cube_nohole.stl',
            10: 'stl/big_round_hole.stl',
            11: 'stl/big_round_nohole.stl',
            12: 'stl/small_cube_hole.stl',
            13: 'stl/small_cube_nohole.stl',
            14: 'stl/small_round_hole.stl',
            15: 'stl/small_round_nohole.stl'
            }
        
        self.block_centers = {
            0 : [6.61294688, -39.2428062],
            1 : [-14.29293533, -39.34175769],
            2 : [-14.16196591, -60.08903798],
            3 : [6.64124933, -60.08900727],
            4 : [27.41527733, -39.04504417],
            5 : [48.26776087, -39.44082099],
            6 : [27.41838273, -60.02330608],
            7 : [47.95682291, -59.69336399],
            8 : [6.61294688, -39.2428062],
            9 : [-14.29293533, -39.34175769],
            10: [-14.16196591, -60.08903798],
            11: [6.64124933, -60.08900727],
            12: [27.41527733, -39.04504417],
            13: [48.26776087, -39.44082099],
            14: [27.41838273, -60.02330608],
            15: [47.95682291, -59.69336399]
            }
        
        self.block_colors = {
            0 : 'saddlebrown',
            1 : 'saddlebrown',
            2 : 'saddlebrown',
            3 : 'saddlebrown',
            4 : 'saddlebrown',
            5 : 'saddlebrown',
            6 : 'saddlebrown',
            7 : 'saddlebrown',
            8 : 'navajowhite',
            9 : 'navajowhite',
            10: 'navajowhite',
            11: 'navajowhite',
            12: 'navajowhite',
            13: 'navajowhite',
            14: 'navajowhite',
            15: 'navajowhite'
            }

    def visualization(self, blocks):
        figure = pyplot.figure()
        axes = figure.add_subplot(projection='3d', computed_zorder=False)

        board_mesh = mesh.Mesh.from_file(self.board_path)
        board_mesh.translate(np.array([30, 30, -25]))
        collection = mplot3d.art3d.Poly3DCollection(board_mesh.vectors, color="black", alpha=0.5)
        axes.add_collection3d(collection)
        scale = board_mesh.points.flatten()
        axes.auto_scale_xyz(scale, scale, scale)
        for i in range(blocks.shape[0]):
            for j in range(blocks.shape[1]):
                if ~np.isnan(blocks[i,j]):
                    block_path = self.block_paths[blocks[i,j]]
                    block_center = self.block_centers[blocks[i,j]]
                    new_block_mesh = mesh.Mesh.from_file(block_path)
                    new_block_mesh.rotate([0.0, 1.0, 0.0], np.radians(180))
                    new_block_mesh.translate(np.array([i*20-block_center[0], j*20-block_center[1],0]))
                    new_block_mesh = self.mesh_update(new_block_mesh)
                    block_color = self.block_colors[blocks[i,j]]
                    collection = mplot3d.art3d.Poly3DCollection(new_block_mesh.vectors, color=block_color, alpha=0.5)
                    axes.add_collection3d(collection)

        scale = new_block_mesh.points.flatten()
        axes.auto_scale_xyz(scale, scale, scale)

        pyplot.show()


    def mesh_location_zero(self, my_mesh):
        midPosRel = (my_mesh.max_ - my_mesh.min_)/2
        my_mesh.x = my_mesh.x - (midPosRel[0] + my_mesh.min_[0])
        my_mesh.y = my_mesh.y - (midPosRel[1] + my_mesh.min_[1])
        my_mesh.z = my_mesh.z - (midPosRel[2] + my_mesh.min_[2])
        return my_mesh


    def mesh_update(self, my_mesh):
        my_mesh.update_areas()
        my_mesh.update_max()
        my_mesh.update_min()
        my_mesh.update_units()
        return my_mesh


    def mesh_scale(self, my_mesh, scale_x, scale_y, scale_z):
        my_mesh.x = my_mesh.x * scale_x
        my_mesh.y = my_mesh.y * scale_y
        my_mesh.z = my_mesh.z * scale_z 
        return my_mesh


def main():
    vis = Visualization()
    # blocks = [[np.nan,np.nan,np.nan,np.nan],
    #           [np.nan,np.nan,np.nan,np.nan],
    #           [np.nan,np.nan,np.nan,np.nan],
    #           [np.nan,np.nan,np.nan,np.nan]]
    blocks = [[0,1,2,3],
              [4,5,6,7],
              [8,9,10,11],
              [12,13,14,15]]
    vis.visualization(np.array(blocks))




if __name__ == "__main__": 
    main()
