import sys
from pymavlink import mavutil, mavwp

PORTS = {1: 5762, 2: 5772, 3: 5782}
host = sys.argv[1] if len(sys.argv) > 1 else '127.0.0.1'

for n, port in PORTS.items():
    m = mavutil.mavlink_connection(f'tcp:{host}:{port}')
    m.wait_heartbeat(timeout=15)
    w = mavwp.MAVWPLoader(target_system=m.target_system, target_component=m.target_component)
    w.load(f'drone{n}.waypoints')
    m.waypoint_clear_all_send()
    m.waypoint_count_send(w.count())
    ok = True
    for _ in range(w.count()):
        req = m.recv_match(type=['MISSION_REQUEST', 'MISSION_REQUEST_INT'], blocking=True, timeout=10)
        if req is None:
            ok = False
            break
        m.mav.send(w.wp(req.seq))
    ack = m.recv_match(type='MISSION_ACK', blocking=True, timeout=10)
    print(f'drone{n}: ' + ('mission uploaded' if ok and ack and ack.type == 0 else 'upload failed'))
    m.close()
