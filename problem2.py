import statistics
import numpy as np
import matplotlib.pyplot as plt
from work import Work
from timezone import TimeZone

class Problem2(object):
    def __init__(self):
        super(Problem2, self).__init__()

        self.w = Work()

        # カウンタ数
        self.w.c = 1

        # 時間帯
        self.w.timezone = TimeZone.OTHER

        # 計算対象期間(分)
        self.w.minute = 60 * 24 * 10

        # 要件待機客数(未満)
        self.c_limit = 5

        # 許容要件不満回数
        self.c_permit = 1

    def work(self, counter_count, timezone):
        self.w.timezone = timezone
        self.w.c = counter_count
        c_unsatisfied = 0

        # 並んでいる客数
        customer_remaining = 0

        for r in self.w.work():
            customer_remaining = customer_remaining + r[2]
            if customer_remaining > self.c_limit:
                c_unsatisfied = c_unsatisfied + 1
            if c_unsatisfied > self.c_permit:
                return False
        return True

if __name__ == '__main__':
    problem2 = Problem2()
    x_label = 'how many counter'
    y_label = 'is good'

    for tz in [TimeZone.LUNCH, TimeZone.DINNER, TimeZone.OTHER]:
        graph_title = TimeZone.TIMEZONE_NAMES[tz]
        res = [statistics.mode([problem2.work(counter_count, tz) for i in range(21)]) for counter_count in range(1, 16)]

        y_arr = np.array(list(map(lambda x: int(x), res)))
        x_arr = np.array(list(range(1, 16)))
        plt.plot(x_arr, y_arr)
        plt.title(graph_title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.xticks(list(range(1, 16)))
        plt.yticks([0, 1])
        plt.grid(True)
        plt.savefig('figure/problem2/' + graph_title + '.png')
        plt.figure()
