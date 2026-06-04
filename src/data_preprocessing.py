import numpy as np
import pandas as pd

import numpy as np
import pandas as pd

TARGET_STATIONS = {
    "捷運市政府站(3號出口)": (121.56785, 25.04105),
    "松山高中": (121.56380, 25.04355),
    "基隆路一段101巷口": (121.56705, 25.04537),
    "富台公園": (121.57200, 25.04204),
    "興雅國中": (121.56989, 25.03633)
}

def build_station_graph_dataset(total_files=41594):
station_data = []

for idx in range(total_files):
    file_path = f"all_metadata/data{idx}.csv"
    df = pd.read_csv(file_path)

    filtered_df = df[df["站點名稱"].isin(TARGET_STATIONS.keys())]
    station_data.append(filtered_df)

all_df = pd.concat(station_data, ignore_index=True)

# Encode station names as graph node indices
station_mapping = {
    station: idx
    for idx, station in enumerate(TARGET_STATIONS.keys())
}

all_df["station_id"] = all_df["站點名稱"].map(station_mapping)

# Add spatial coordinates
all_df["longitude"] = all_df["站點名稱"].map(
    lambda x: TARGET_STATIONS[x][0]
)

all_df["latitude"] = all_df["站點名稱"].map(
    lambda x: TARGET_STATIONS[x][1]
)

# Sort temporal sequence
all_df = all_df.sort_values("時間")

return all_df
