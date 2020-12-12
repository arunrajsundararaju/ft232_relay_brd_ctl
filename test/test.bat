setlocal
SET PATH=%PATH%;..\src

relay_brd_init.py -d4

relay_brd_ctl.py -d4 -r1 -s1
relay_brd_ctl.py -d4 -r2 -s1
relay_brd_ctl.py -d4 -r3 -s1
relay_brd_ctl.py -d4 -r4 -s1
relay_brd_ctl.py -d4 -r1 -s0
relay_brd_ctl.py -d4 -r2 -s0
relay_brd_ctl.py -d4 -r3 -s0
relay_brd_ctl.py -d4 -r4 -s0
