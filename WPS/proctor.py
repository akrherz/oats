"""Deliver it to her

call me with the year, duh

    python proctor.py 1979

"""
from __future__ import print_function
import sys
import os
import subprocess

NAMELIST_TEMPLATE = """
&share
 wrf_core = 'ARW',
 max_dom = 2,
 start_date = '%(year)s-01-01_00:00:00','%(year)s-01-01_00:00:00',
 end_date   = '%(year)s-12-31_18:00:00','%(year)s-12-31_18:00:00',
 interval_seconds = 21600
 io_form_geogrid = 2,
/

&geogrid
 parent_id         =   1,   1,
 parent_grid_ratio =   1,   3,
 i_parent_start    =   1,  25,
 j_parent_start    =   1,  17,
 e_we              =  89, 139,
 e_sn              =  58, 118,
 geog_data_res     = 'modis_lakes','modis_lakes',
 dx = 75000,
 dy = 75000,
 map_proj = 'lambert',
 ref_lat   =  36.00,
 ref_lon   = -95.00,
 truelat1  =  36.00,
 truelat2  =  36.00,
 stand_lon = -96.00,
 geog_data_path = '/ptmp/acaruthe/BUILD_WRF/WPS_GEOG'
/

&ungrib
 out_format = 'WPS',
 prefix = 'FILE',
/

&metgrid
 fg_name = 'FILE',
 io_form_metgrid = 2,
/
"""

def main(argv):
    """go main"""
    year = int(argv[1])
    print("We are running for the year of %s" % (year, ))
    # Run link_grib.csh
    print("   calling link_grib")
    cmd = "./link_grib.csh /mnt/nrel/akrherz/ERA_T255/*.%s0101??" % (year,)
    subprocess.call(cmd, shell=True)
    # Edit namelist
    fp = open("namelist.wps", 'w')
    fp.write(NAMELIST_TEMPLATE % dict(year=year))
    fp.close()
    # Run ungrib
    print("   calling ungrib")
    subprocess.call("./ungrib.exe >& ungrib_%s.log" % (year,), shell=True)
    # Run metgrid
    print("   calling metgrid")
    subprocess.call("./metgrid.exe >& metgrid_%s.log" % (year,), shell=True)
    # Run geogrid, no
    # Move files to larger storage, please
    print("   moving files to /mnt/nrel...")
    os.makedirs("/mnt/nrel/acaruthe/wrf_runs/input_files/%s" % (year, ))
    subprocess.call("mv met_em*nc /mnt/nrel/acaruthe/wrf_runs/input_files/%s" % (year, ), shell=True)
    print("We are done with year %s" %  (year, ))


if __name__ == '__main__':
    main(sys.argv)

