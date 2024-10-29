import os
import time

import psutil


def measure_memory():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024  # Retorna o uso de memória em MB


def measure_performance(func, *args):
    start_time = time.time()
    memory_before = measure_memory()
    result = func(*args)
    memory_after = measure_memory()
    end_time = time.time()
    execution_time = end_time - start_time
    memory_used = memory_after - memory_before
    return execution_time, memory_used, result
