
from datetime import datetime
from telnetlib import STATUS


class Payment:
    id              = int
    status          = str
    executed_date   = datetime