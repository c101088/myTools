# encoding: utf-8
# Author    : clz
# Datetime  : 2022/5/31 16:44
# User      : clz
# Product   : PyCharm
# Project   : ModelOpt
# File      : test.py
# explain   : 文件说明
import time

from mealpy.evolutionary_based import GA
from mealpy.bio_based import SMA
import numpy as np
import urllib.request
import urllib.parse
import requests
import datetime
def fitness_function(solution):
    print("11")
    # return np.sum(solution**2)
    str1="http://192.168.53.5:8080/test/test/?x=" + str(solution[0]) + "," + str(solution[1]) + "," + str(solution[2]) + "," + str(solution[3])
    resp = urllib.request.urlopen(str1)
    result = float(resp.read().decode("UTF-8"))
    return result



if __name__ == '__main__':
    # problem_dict1 = {
    #     "fit_func": fitness_function,
    #     "lb": [0, 280, 0, 400],
    #     "ub": [280, 1300, 400, 1500],
    #     "minmax": "min",
    #     "log_to": None,
    #     "save_population": False,
    # }
    #
    # ## Run the algorithm
    # model = SMA.BaseSMA(problem_dict1, epoch=100, pop_size=50, pr=0.03)
    # # model = GA.BaseGA(problem_dict1, epoch=100, pop_size=50, pr=0.03)
    # best_position, best_fitness = model.solve()
    # print(f"Best solution: {best_position}, Best fitness: {best_fitness}")
    start_time = time.time()
    fitness_function([10,1000,200,1200])
    seconds = time.time() - start_time
    print(seconds*1000)