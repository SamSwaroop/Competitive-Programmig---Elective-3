import os,sys
sys.path.append(os.getcwd())
from nthpronicnumber import nthpronicnumber
import pytest


@pytest.mark.parametrize('x, result',[
(0, 0), 
(1, 2), 
(2, 6), 
(3, 12), 
(4, 20), 
(5, 30), 
(6, 42), 
# (7, 56), 
# (8, 72), 
# (9, 90), 
# (10, 110), 
# (11, 132), 
# (12, 156), 
# (13, 182), 
# (14, 210), 
# (15, 240), 
# (16, 272), 
# (17, 306), 
# (18, 342), 
# (19, 380), 
# (20, 420), 
# (21, 462), 
# (22, 506), 
# (23, 552), 
# (24, 600), 
# (25, 650), 
# (26, 702), 
# (27, 756), 
# (28, 812), 
# (29, 870), 
# (30, 930), 
# (31, 992), 
# (32, 1056), 
# (33, 1122), 
# (34, 1190), 
# (35, 1260), 
# (36, 1332), 
# (37, 1406), 
# (38, 1482), 
# (39, 1560), 
# (40, 1640), 
# (41, 1722), 
# (42, 1806), 
# (43, 1892), 
# (44, 1980), 
# (45, 2070), 
# (46, 2162), 
# (47, 2256), 
# (48, 2352), 
# (49, 2450), 
# (50, 2550), 
])

def test_nthpronicnumber(x, result):
    assert nthpronicnumber(x) == result
