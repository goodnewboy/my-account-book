# 个人记账本 v0.1
def add_expense():
    name = input("花费名称：")
    amount = float(input("金额："))
    print(f"已记录：{name}，{amount}元1")

if __name__ == "__main__":
    add_expense()