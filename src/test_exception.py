# src/test_exception.py
from src.exception import CustomException
import sys

try:
    # Deliberate error to test logging
    a = 1 / 0
except Exception as e:
    raise CustomException(e, sys)

