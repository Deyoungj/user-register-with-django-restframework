# from datetime import datetime
# from dateutil.relativedelta import relativedelta


# t = datetime.now() + relativedelta(months=6)

# print(t)


class Test:
    def __init__(self, name) -> None:
        self.name = name

    def g(self):
        print(self)

# t = Test('chidi')
# t.g()