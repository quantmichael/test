#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 16:02:02 2024

@author: michaelis
"""

import sys
import os

# 클래스가 있는 디렉토리 경로 설정
directory = '/Users/michaelis/quant/comm'

# 디렉토리를 파이썬 경로에 추가
sys.path.append(directory)

# 이제 해당 디렉토리의 클래스를 임포트할 수 있습니다.
import common

# 클래스 사용
comm = common.Common();
start_date = "2018-01-01"
end_date = "2024-09-01"

dates = comm.date_range(start_date, end_date)
