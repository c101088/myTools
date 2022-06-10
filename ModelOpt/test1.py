# encoding: utf-8
# Author    : clz
# Datetime  : 2022/5/31 16:44
# User      : clz
# Product   : PyCharm
# Project   : ModelOpt
# File      : test.py
# explain   : 文件说明

import geatpy as ea  # Import geatpy
import numpy as np
import urllib.request
import urllib.parse


# def fitness_function(solution):
#     print("11")
#     # return np.sum(solution**2)
#     str1="http://192.168.53.5:8080/test/test/?x=" + str(solution[0]) + "," + str(solution[1]) + "," + str(solution[2]) + "," + str(solution[3])
#     resp = urllib.request.urlopen(str1)
#     result = float(resp.read().decode("UTF-8"))
#     return result

class MyProblem(ea.Problem):  # Inherited from Problem class.
    def __init__(self, M):  # M is the number of objects.
        name = 'DTLZ1'  # Problem's name.
        maxormins = [1] * M  # All objects are need to be minimized.
        Dim = 4  # Set the dimension of decision variables.
        varTypes = [0] * Dim  # Set the types of decision variables. 0 means continuous while 1 means discrete.

        lb = [0, 280, 0, 400]  # The lower bound of each decision variable.
        ub = [280, 1300, 400, 1500]  # The upper bound of each decision variable.
        lbin = [1] * Dim  # Whether the lower boundary is included.
        ubin = [1] * Dim  # Whether the upper boundary is included.
        # Call the superclass's constructor to complete the instantiation
        ea.Problem.__init__(self, name, M, maxormins, Dim, varTypes, lb, ub, lbin, ubin)

    def aimFunc(self, pop):  # Write the aim function here, pop is an object of Population class.
        x1=pop.Phen[:,0]
        x2=pop.Phen[:,1]
        x3=pop.Phen[:,2]
        x4=pop.Phen[:,3]
        # return np.sum(solution**2)
        arr = []
        index=0
        for solution in x1:
            str1 = "http://192.168.53.5:8080/test/test/?x=" + str(x1[index]) + "," + str(x2[index]) + "," + str(
                x3[index]) + "," + str(x4[index])
            resp = urllib.request.urlopen(str1)
            result = float(resp.read().decode("UTF-8"))
            arr.append(result)
            index=index+1
        cv=1
        return  np.array(arr).T,cv

    def calReferObjV(self):  # Calculate the theoretic global optimal solution here.
        realBestObjV = np.array([[0]])
        return realBestObjV


if __name__ == '__main__':
    M = 1  # Set the number of objects.
    problem = MyProblem(M)  # Instantiate MyProblem class
    # Instantiate a algorithm class.
    algorithm = ea.moea_NSGA2_templet(problem,
                                      ea.Population(Encoding='RI', NIND=50),
                                      MAXGEN=200,  # 最大进化代数
                                      logTras=0)  # 表示每隔多少代记录一次日志信息，0表示不记录。
    # 求解
    res = ea.optimize(algorithm, seed=1, verbose=False, drawing=1, outputMsg=True, drawLog=False, saveFlag=False,
                      dirName='result')
