import numpy as np
import matplotlib.pyplot as plt
import collections
import pandas as pd

# ポアソン分布の情報を返します
class Poisson(object):
    def __init__(self):
        super(Poisson, self).__init__()

        #設定
        #試行回数
        self.rand_exp_size = 100000000

    def __getPoissonRawData(self, lam):
        return np.random.poisson(lam=lam, size=self.rand_exp_size)

    def __collectData(self, ndarray):
        data = collections.Counter(ndarray)
        wariai = []

        for i in range(11):
            wariai.append(data[i] / self.rand_exp_size)

        return wariai

    def __collectDataAsAccumulation(self, ndarray):
        data = collections.Counter(ndarray)
        wariai = []
        before = 0

        for i in range(11):
            newNum = (data[i] / self.rand_exp_size) + before
            wariai.append(newNum)
            before = newNum
        return wariai

    def getPoisson(self, lam, accumulation=False):
        ndarray = self.__getPoissonRawData(lam)
        if accumulation:
            ret = self.__collectDataAsAccumulation(ndarray)
        else:
            ret = self.__collectData(ndarray)
        return ret

def main():
    # 一億回試行結果サンプル
    # --------------単純-------------------
    # [[0.36794134, 0.36777254, 0.18393338, 0.06135812, 0.015329, 0.00307398, 0.00050946], [0.13535494, 0.27065747, 0.27065742, 0.1804658, 0.09019598, 0.03610984, 0.01201569], [0.04983646, 0.14932302, 0.22403269, 0.22401309, 0.16805746, 0.10079521, 0.05041649]]
    # ----------------累積------------------
    # [[0.36787723, 0.73581517, 0.9197135599999999, 0.9810340099999999, 0.9963521299999999, 0.9994061499999999, 0.9999158099999998], [0.13533748, 0.40606087, 0.67668496, 0.8571052100000001, 0.9473208000000001, 0.98342485, 0.99546965], [0.04976937, 0.19917284000000002, 0.42318917, 0.64725109, 0.8153467400000001, 0.91615721, 0.96649918]]

    poisson = Poisson()
    wariai_list = []

    print('--------------単純-------------------')
    for i in range(1, 5):
        wariai_list.append(poisson.getPoisson(i))
    print(wariai_list)

    wariai_list = []
    print('----------------累積------------------')
    for i in range(1, 5):
        wariai_list.append(poisson.getPoisson(i, True))
    print(wariai_list)

if __name__ == "__main__":
    main()
