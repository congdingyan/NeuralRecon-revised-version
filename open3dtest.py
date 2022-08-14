import open3d as o3d
import numpy as np

pcd=o3d.io.read_point_cloud(r"./results/scene_scannet_checkpoints_fusion_eval_29/scene0001_01.ply")
print(pcd)
#无序点云，打印所有点
print(np.asarray(pcd.points).shape)
#第一个参数是要可视化的点云列表，
o3d.visualization.draw_geometries([pcd],window_name="椅子",mesh_show_wireframe=True,mesh_show_back_face=True,
                                  zoom=0.3412,
                                  front=[0.4257, -0.2125, -0.8795],
                                  lookat=[2.6172, 2.0475, 1.532],
                                  up=[-0.0694, -0.9768, 0.2024])
