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
    for tz in [TimeZone.LUNCH, TimeZone.DINNER, TimeZone.OTHER]:
        res = []
        for counter_count in range(1, 50):
            res.append(Problem2().work(counter_count, tz))
        print(res)
