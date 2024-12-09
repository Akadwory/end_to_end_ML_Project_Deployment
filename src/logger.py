import logging 
import os 
from datetime import datetime

#Define the log file file and name 
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_dir = os.path.join(os.getcwd(),"logs") #Directory
os.makedirs(log_dir,exist_ok=True)

LOG_FILE_PATH = os.path.join(log_dir,LOG_FILE) #Full log file path 

#Configure logging 
logging.basicConfig(
    filename= LOG_FILE_PATH,
    format= "[%(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)
