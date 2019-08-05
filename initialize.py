#! /usr/bin/env python

import xfftspy

# initialize XFFTS boards
>>> cmd = xfftspy.udp_client(host='localhost')
>>> cmd.stop()
>>> cmd.set_synctime(100000)          # synctime : 100 ms
>>> cmd.set_usedsections([1])         # use board : 1
>>> cmd.set_board_bandwidth(1, 200)  # bandwidth : 200 MHz
>>> cmd.configure()                   # apply settings
>>> cmd.caladc()                      # calibrate ADCs
>>> cmd.start()                       # start measurement
