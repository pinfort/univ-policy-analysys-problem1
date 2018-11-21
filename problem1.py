import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from work import Work
from timezone import TimeZone

class Problem1(object):
    def __init__(self):
        super(Problem1, self).__init__()
        
        self.w = Work()

        # カウンタ数
        self.w.c = 1

        # 時間帯
        self.w.timezone = TimeZone.OTHER

        # 従業員時給
        self.c_cost = 966

        # 客一人当たり利益
        self.c_profit = 180

        # 処理した客数
        self.customer_finished = 0

    def main(self, counter_count, timezone):
        self.w.c = counter_count
        self.w.timezone = timezone

        for r in self.w.work():
            self.customer_finished = self.customer_finished + r[1]

        all_profit = self.c_profit * self.customer_finished
        cost = self.c_cost * int(self.w.minute / 60) * self.w.c
        # print('cost: ', cost)
        # print('all profit: ', all_profit)
        # print('result: ', all_profit - cost)
        return all_profit - cost

if __name__ == '__main__':
    x_label = 'how many counter'
    y_label = 'how much profit'

    for tz in [TimeZone.LUNCH, TimeZone.DINNER, TimeZone.OTHER]:
        graph_title = TimeZone.TIMEZONE_NAMES[tz]
        x_data = []
        y_data = []
        for counter_count in range(1, 10):
            x_data.append(counter_count)
            # print('timezone: ', TimeZone.TIMEZONE_NAMES[tz], 'counter: ', counter_count)
            y_data.append(Problem1().main(counter_count, tz))

        y_arr = np.array(y_data)
        x_arr = np.array(x_data)
        plt.plot(x_arr, y_arr)
        plt.title(graph_title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.grid(True)
        plt.savefig('figure/' + graph_title + '.png')
        plt.figure()
