#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy
import sys
import matplotlib.pyplot as plt
import talib as ta
from datetime import datetime, timedelta
import warnings

import os
import configparser

# 공통 디렉토리를 설정합니다.
directory = '/Users/michaelis/quant/comm'
target_file = 'db.txt'
file_path = os.path.join(directory, target_file)

warnings.filterwarnings('ignore')

# Database Connection
cfg_db = configparser.ConfigParser()
cfg_db.read(file_path)
db_host = cfg_db.get('lg', 'db_host')
db_name = cfg_db.get('lg', 'db_name')
db_user = cfg_db.get('lg', 'db_user')
db_pwd = cfg_db.get('lg', 'db_pwd')
