something quick and usable to hookup a FT232 USB-to-UART board to a 4-channel relay board
********************************************************************************
Depends on ftd2xx and argparse. Install them using 'pip install ftd2xx argparse'
********************************************************************************
Watch it in action:
1) test-bat-run; https://youtu.be/0HMQPE-78PU
2) relay-powered-chan-1-test; https://youtu.be/q0dDHCDcen8
********************************************************************************
There is a initialization limitation hence have to run relay_brd_init.py atleast once after you plug the FT232 converter in.
********************************************************************************
<pre>
usage: relay_brd_init.py [-h] -d index

FTDI relay board init utility.

optional arguments:
  -h, --help            show this help message and exit
  -d index, --device index
                        Specify the FTDI device index.
 </pre>                   
********************************************************************************
<pre>
usage: relay_brd_ctl.py [-h] -d index -r {1,2,3,4} -s {0,1}

FTDI relay board control utility.

optional arguments:
  -h, --help            show this help message and exit
  -d index, --device index
                        Specify the FTDI device index.
  -r {1,2,3,4}, --relay {1,2,3,4}
                        Specify the relay ID.
  -s {0,1}, --state {0,1}
                        Specify the relay state.
</pre>
********************************************************************************
