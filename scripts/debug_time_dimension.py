"""Figure out what our time dimension looks like"""
from __future__ import print_function
import sys
import datetime

import netCDF4


def main(argv):
    """Do Work"""
    nc = netCDF4.Dataset(argv[1])
    nctime = nc.variables['time']
    basetime = datetime.datetime.strptime(nctime.units.replace("hours since ",
                                                               ""),
                                          "%Y-%m-%d_%H:%M:%S")
    offsets = nctime[:] * 3600.
    olddelta = None
    olddt = basetime
    counts = {}
    for i, offset in enumerate(offsets):
        dt = basetime + datetime.timedelta(seconds=int(offset))
        if dt.second == 59:
            dt += datetime.timedelta(seconds=1)
        delta = dt - olddt
        counts.setdefault(delta, 0)
        counts[delta] += 1
        if dt < olddt:
            print("Time goes backwards by %s at %s" % (delta, dt))
            delta = olddelta
        elif delta != olddelta:
            print("New Time Delta of %s seconds at %s" % (delta, dt))
        olddelta = delta
        olddt = dt

    keys = counts.keys()
    keys.sort()
    for delta in keys:
        print("%s -> %s entries" % (delta, counts[delta]))


if __name__ == '__main__':
    main(sys.argv)
