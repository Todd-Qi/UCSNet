import os

data_folder = "/mnt/A/qiyh/2021/Github/UCSNet/results/eth3d/"

scenes = ["courtyard", "delivery_area", "electro", "facade", "kicker", "meadow", "office",
          "pipes", "playground", "relief", "relief_2", "terrace", "terrains"]


if __name__ == "__main__":

    point_folder = os.path.join(data_folder, "point_clouds")
    if not os.path.exists(point_folder):
        os.mkdir(point_folder)

    for scene in scenes:
        scene_point_folder = os.path.join(data_folder, scene, "points_ucsnet")
        consis_folders = [f for f in os.listdir(scene_point_folder) if f.startswith('consistencyCheck-')]
        consis_folders.sort()
        consis_folder = consis_folders[-1]

        source_ply = os.path.join(data_folder, scene, "points_ucsnet", consis_folder, "final3d_model.ply")
        target_ply = os.path.join(point_folder, "{}.ply".format(scene))

        cmd = "mv " + source_ply + " " + target_ply
        print(cmd)
        os.system(cmd)



        