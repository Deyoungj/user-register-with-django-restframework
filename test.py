from datetime import datetime
from dateutil.relativedelta import relativedelta


t = datetime.now() + relativedelta(months=6)

print(t)