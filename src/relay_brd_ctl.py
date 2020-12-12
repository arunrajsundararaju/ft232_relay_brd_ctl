# MIT License

# Copyright (c) 2020 'Arun Raj Sundararaju (arunraj03@gmail.com)'

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
import ftd2xx as ftd
import argparse

def setBit(int_type, offset):
    mask = 1 << offset
    return(int_type | mask)

def clearBit(int_type, offset):
    mask = ~(1 << offset)
    return(int_type & mask)

parser = argparse.ArgumentParser(description='FTDI relay board control utility.')
parser.add_argument('-d',
                    '--device',
                    required=True,
                    type=int,
                    help='Specify the FTDI device index.',
                    metavar='index')
parser.add_argument('-r',
                    '--relay',
                    required=True,
                    type=int,
                    help='Specify the relay ID.',
                    choices=[1, 2, 3, 4])
parser.add_argument('-s',
                    '--state',
                    required=True,
                    type=int,
                    help='Specify the relay state.',
                    choices=[0, 1])
args = parser.parse_args()

args.relay -= 1

try:
    dev = ftd.open(args.device)
except Exception as e:
    print(e)
    sys.exit(1)

dbus_val = dev.getBitMode()

if args.state == 1:
    dbus_val = clearBit(dbus_val, args.relay)
else:
    dbus_val = setBit(dbus_val, args.relay)

dev.write(chr(dbus_val))
dev.close()
