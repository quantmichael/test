import multiprocessing
import time
import math
from concurrent.futures import ProcessPoolExecutor
from joblib import Parallel, delayed
import dask
import dask.bag as db
import ray
import pymysql
import configparser

# Database Connection
pymysql.install_as_MySQLdb()
cfg_db = configparser.ConfigParser()
cfg_db.read('db.txt')
db_host = cfg_db.get('lg', 'db_host')
db_name = cfg_db.get('lg', 'db_name')
db_user = cfg_db.get('lg', 'db_user')
db_pwd = cfg_db.get('lg', 'db_pwd')
conn = pymysql.connect(host=db_host, user=db_user, password=db_pwd, db=db_name, charset='utf8')
cursor = conn.cursor()

# CPU 바운드 작업: 팩토리얼 계산 함수
def calculate_factorial(number):
    return math.factorial(number)

# 1. multiprocessing 라이브러리 사용
def test_multiprocessing(numbers):
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(calculate_factorial, numbers)
    return results

# 2. concurrent.futures 라이브러리 사용
def test_concurrent_futures(numbers):
    with ProcessPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
        results = list(executor.map(calculate_factorial, numbers))
    return results

# 3. joblib 라이브러리 사용
def test_joblib(numbers):
    results = Parallel(n_jobs=multiprocessing.cpu_count())(delayed(calculate_factorial)(i) for i in numbers)
    return results

# 4. dask 라이브러리 사용
def test_dask(numbers):
    bag = db.from_sequence(numbers, npartitions=multiprocessing.cpu_count())
    results = bag.map(calculate_factorial).compute()
    return results

# 5. ray 라이브러리 사용
@ray.remote
def calculate_factorial_ray(number):
    return math.factorial(number)

def test_ray(numbers):
    ray.init(ignore_reinit_error=True)
    results = ray.get([calculate_factorial_ray.remote(i) for i in numbers])
    ray.shutdown()
    return results

if __name__ == "__main__":
    numbers = list(range(10000, 20000))

    # 1. multiprocessing 테스트
    start_time = time.time()
    test_multiprocessing(numbers)
    mp_time = time.time() - start_time
    print(f"multiprocessing 라이브러리 시간: {mp_time:.2f}초")

    # 2. concurrent.futures 테스트
    start_time = time.time()
    test_concurrent_futures(numbers)
    cf_time = time.time() - start_time
    print(f"concurrent.futures 라이브러리 시간: {cf_time:.2f}초")

    # 3. joblib 테스트
    start_time = time.time()
    test_joblib(numbers)
    joblib_time = time.time() - start_time
    print(f"joblib 라이브러리 시간: {joblib_time:.2f}초")

    # 4. dask 테스트
    start_time = time.time()
    test_dask(numbers)
    dask_time = time.time() - start_time
    print(f"dask 라이브러리 시간: {dask_time:.2f}초")

    # 5. ray 테스트
    start_time = time.time()
    test_ray(numbers)
    ray_time = time.time() - start_time
    print(f"ray 라이브러리 시간: {ray_time:.2f}초")
