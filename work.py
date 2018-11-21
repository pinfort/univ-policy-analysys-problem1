from timezone import TimeZone

class Work(object):
    # カウンタ数
    c = 3

    # １カウンタの五分当たり処理能力
    c_power = 1

    # 計算対象時間（分間）
    minute = 60 * 3

    # 計算時間単位（分間）
    minute_base = 5

    # 並んでいる顧客数
    remaining_customer = 0

    # 時間帯
    timezone = TimeZone.OTHER

    def work(self):
        for i in range(int(self.minute / self.minute_base)):
            # 新規顧客がやってくる
            new_customer = TimeZone.getRandomCustomerCount(self.timezone)
            # print(i * self.minute_base, 'remaining_customer is', self.remaining_customer, 'new_costomer is', new_customer)

            # 新規顧客が並ぶ
            self.remaining_customer = self.remaining_customer + new_customer

            # 処理を行う顧客数。残り顧客数は0より少なくならない。
            customer = min(self.remaining_customer, self.c_power * self.c) if min(self.remaining_customer, self.c_power * self.c) > 0 else 0

            # カウンターで処理を行う。
            self.remaining_customer = self.remaining_customer - customer

            yield [i * self.minute_base, customer, self.remaining_customer]
            # print(i * minute_base, customer, 'customer finished.', remaining_customer, 'customers remaining.' + "\n")
