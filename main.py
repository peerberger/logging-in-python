import logging
import datetime as dt
from configparser import ConfigParser

today = dt.datetime.today()
filename = f"{today.year:02d}" \
            f"-{today.month:02d}" \
            f"-{today.day:02d}.log"

config = ConfigParser()
config.read("config.ini")

LEVEL = config["logging"]["level"]

logging.basicConfig(level=LEVEL)

logger = logging.getLogger("MY_MODULE")

# formatter = logging.Formatter("%(asctime)s: %(levelname)s - %(message)s")
FORMATTER_STRING = config["logging"]["formatter_string"]
# print(FORMATTER_STRING)
formatter = logging.Formatter(FORMATTER_STRING)

file_handler = logging.FileHandler(filename)
file_handler.setLevel(logging.WARNING)
logger.addHandler(file_handler)

logger.debug("debug message")
logger.warning("warning message")
 