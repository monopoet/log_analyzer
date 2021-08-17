
import pandas as pd
import numpy as np
import os
import sys
import folium
from tkinter import filedialog

filename = filedialog.askopenfilename(title="Select file",
                                      filetypes=(("csv files", "*.csv"),
                                      ("all files", "*.*")))

print(filename)

site_log = pd.read_csv(filename)
site_log[['위도','경도']] = site_log[['위도','경도']].apply(pd.to_numeric)
#site_log = site_log.dropna()

rsrp_map=folium.Map(location=[site_log['위도'][1], site_log['경도'][1]], zoom_start=17)
for a,b,rsrp in zip(site_log['위도'], site_log['경도'], site_log['RSRP']):
#    print(a,b)
    if rsrp > 30:
        folium.CircleMarker([a,b],
                            radius = 2,
                            color='green', fill_color='green').add_to(rsrp_map)
    elif rsrp > 15:
        folium.CircleMarker([a,b],
                    radius = 2,
                    color='greenyellow', fill_color='greenyellow').add_to(rsrp_map)
    elif rsrp > 2:
        folium.CircleMarker([a,b],
                    radius = 2,
                    color='yellow', fill_color='yellow').add_to(rsrp_map)
    elif rsrp > 0:
        folium.CircleMarker([a,b],
                    radius = 2,
                    color='orange', fill_color='orange').add_to(rsrp_map)
    else :
        folium.CircleMarker([a,b],
                    radius = 2,
                    color='red', fill_color='red').add_to(rsrp_map)

gps_map=folium.Map(location=[site_log['위도'][1], site_log['경도'][1]], zoom_start=17)
for a,b,hdop in zip(site_log['위도'], site_log['경도'], site_log['hdop']):
#    print(a,b)
    if hdop < 0.9:
        folium.CircleMarker([a,b],
                            radius = 2,
                            color='green', fill_color='green').add_to(gps_map)
    elif hdop < 1.0:
        folium.CircleMarker([a,b],
                    radius = 2,
                    color='greenyellow', fill_color='greenyellow').add_to(gps_map)
    elif rsrp < 1.1:
        folium.CircleMarker([a,b],
                    radius = 2,
                    color='orange', fill_color='orange').add_to(gps_map)
    else :
        folium.CircleMarker([a,b],
                    radius = 2,
                    color='red', fill_color='red').add_to(gps_map)

filename = filename.rstrip('.csv')
rsrp_map.save(filename+'_rsrp.html')
gps_map.save(filename+'_gps.html')