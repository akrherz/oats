"""Some precip work with Dr Arritt

A file was provided on 3 March 2018, I appended the HUC12"""
from __future__ import print_function

from pyiem.util import get_dbconn


def main():
    """Go!"""
    pgconn = get_dbconn('idep')
    cursor = pgconn.cursor()
    for line in open('/tmp/5884_US_inv'):
        tokens = line.split()
        lon = float(tokens[1])
        lat = float(tokens[2])
        cursor.execute("""
        select huc12 from wbd_huc12 where
        st_contains(geom, 'SRID=4326;POINT(%s %s)')
        """, (lon, lat))
        row = cursor.fetchone()
        print("%s %s" % (line.strip(), row[0]))

if __name__ == '__main__':
    main()
