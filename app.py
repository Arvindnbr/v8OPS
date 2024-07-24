from v8OPS.logger import logging
from v8OPS.exception import AppException
import sys

try:
    print(12/"a")
except Exception as a:
    raise AppException(a, sys)