# Operator website

The screen the operator of عسّاس uses to set up and watch the drones.

- **Dashboard:** live map with the three drones, their paths, battery, flight time, speed and network delay, change alarms and lost-link warnings. **Run survey** starts a survey; **Cancel survey** sends all drones straight back to the tower.
- **Storage:** alarm history, LiDAR data history and image data history. Each entry can be downloaded: alarm report (.csv), scan report (.csv) and flight path (.geojson, opens in Google Earth or QGIS). **Export list** downloads the whole table. The LiDAR point cloud (.las) download becomes available when the website is connected to the drones.
- **Setup:** choose the scan area within the drones' range; the paths are created automatically. **Export mission files** saves one ArduPilot mission per drone (`drone1.waypoints`, `drone2.waypoints`, `drone3.waypoints`).

The website currently runs on simulated data, in real time or 4× faster. Each survey is different: it may find no change, one or two changes, and a drone may lose its link for a few seconds.

To open it, download `index.html` and open it in a browser. The map image is built into the file.

## Sending the missions to the drones

`upload_mission.py` sends the exported mission files to the three drones over MAVLink, the same way as to real drones. Put it in the same folder as the three `.waypoints` files, start the simulation, then run:

```bash
pip install pymavlink
python3 upload_mission.py
```

It connects to the drones on ports 5762, 5772 and 5782. The lanes use ArduPilot's terrain altitude (30 m above the ground), so terrain data must be available to the autopilot.
