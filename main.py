import logging
import datetime as dt
from configparser import ConfigParser

today = dt.datetime.today()
filename = f"{today.year:02d}" \
            f"-{today.month:02d}" \
            f"-{today.day:02d}.log"

config = ConfigParser()
config.read("config.conf")
LEVEL = config["logging"]["level"]
LOGFILE_NAME = config["logging"]["logfile_name"]


logging.basicConfig(level=logging.WARNING)

logger = logging.getLogger("MY_MODULE")


# file_handler = logging.FileHandler(filename)
file_handler = logging.FileHandler(LOGFILE_NAME)

file_handler.setLevel(logging.DEBUG)

# formatter = logging.Formatter("%(asctime)s: %(levelname)s - %(message)s")
# file_handler.setFormatter(formatter)


logger.addHandler(file_handler)

logger.debug("debug message")
logger.warning("warning message")
 