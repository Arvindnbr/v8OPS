import logging
import os
from datetime import datetime
from from_root import from_root

logfile = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logpath = os.path.join(from_root(),'log',logfile)
os.makedirs(logpath,exist_ok=True)

logfilepath = os.path.join(logpath,logfile)
logging.basicConfig(
    filename=logfilepath,
    format= "[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO
)