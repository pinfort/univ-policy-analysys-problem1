from timezone import TimeZone

# カウンタ数
c = 3

# １カウンタの五分当たり処理能力
c_power = 1

# 1カウンタの一時間当たりコスト（従業員時給）
c_cost = 950

# 1会計当たり利益
c_profit = 200

# 計算対象時間（分間）
minute = 60 * 3

# 計算時間単位（分間）
minute_base = 5

# 並んでいる顧客数
remaining_customer = 0

for i in range(int(minute / minute_base)):
    # 新規顧客がやってくる
    new_customer = TimeZone.getRandomCustomerCount(TimeZone.OTHER)
    print(i * minute_base, 'remaining_customer is', remaining_customer, 'new_costomer is', new_customer)

    # 新規顧客が並ぶ
    remaining_customer = remaining_customer + new_customer

    # 処理を行う顧客数。残り顧客数は0より少なくならない。
    customer = min(remaining_customer, c_power * c) if min(remaining_customer, c_power * c) > 0 else 0

    # カウンターで処理を行う。
    remaining_customer = remaining_customer - customer

    print(i * minute_base, customer, 'customer finished.', remaining_customer, 'customers remaining.' + "\n")

