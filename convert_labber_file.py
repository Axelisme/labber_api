import argparse
import sys

import h5py
import Labber
import numpy as np


def hdf5_to_labber(hdf5_file_path: str) -> bool:
    # print python version
    print("hdf5_to_labber")
    print(f"Python version: {sys.version}")
    print(f"Running on file: {hdf5_file_path}")

    with h5py.File(hdf5_file_path, "r") as f:
        x_info = f["x_info"]
        y_info = f["y_info"]
        z_info = f["z_info"]

        z_info.update({"complex": True, "vector": False})

        log_channels = [z_info]
        step_channels = list(filter(None, [x_info, y_info]))

        Labber.createLogFile_ForData(hdf5_file_path, log_channels, step_channels)

    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=str)
    args = parser.parse_args()

    if args.file:
        hdf5_to_labber(args.file)
