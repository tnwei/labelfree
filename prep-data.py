# TODO: Needs to be updated!

import os
import pickle

import numpy as np
import pandas as pd
from scipy.io import loadmat

if __name__ == "__main__":
    wd = "data/raw/NASA Deliverables/"
    savedir = "data/processed/"

    trajectories = {}
    image_frames = {}
    change_frames = {}

    for i in os.listdir(wd):
        if i.split(".")[-1] != "mat":
            continue
        print(wd + i)

        # Load data
        one_file_data = loadmat(wd + i)

        # Load trajectory data
        meas_x = one_file_data["trajectory"]["measured"][0, 0]["x"][0, 0].ravel()
        meas_y = one_file_data["trajectory"]["measured"][0, 0]["y"][0, 0].ravel()
        opt_x = one_file_data["trajectory"]["optimal"][0, 0]["x"][0, 0].ravel()
        opt_y = one_file_data["trajectory"]["optimal"][0, 0]["y"][0, 0].ravel()

        # Find non-valid data points
        nan_pad_count = meas_x.shape[0] - opt_x.shape[0]

        # Store trajectory data
        trajectories[i] = pd.DataFrame(
            index=one_file_data["trajectory"]["time"][0, 0].ravel(),
            data={
                "meas_x": meas_x,
                "meas_y": meas_y,
                "opt_x": np.concatenate(
                    [opt_x, np.array(nan_pad_count * [np.nan])], axis=0
                ),
                "opt_y": np.concatenate(
                    [opt_y, np.array(nan_pad_count * [np.nan])], axis=0
                ),
            },
        )

        # Store image frames
        image_frames[i] = one_file_data["images"][0, 0]["actual"]

        # Store change frames
        # Prolly won't use this though
        change_frames[i] = one_file_data["images"][0, 0]["detection"]

    # Save processed data
    with open(savedir + "trajectories.pkl", "wb") as f:
        pickle.dump(trajectories, f)

    with open(savedir + "image_frames.pkl", "wb") as f:
        pickle.dump(image_frames, f)

    with open(savedir + "change_frames.pkl", "wb") as f:
        pickle.dump(change_frames, f)
