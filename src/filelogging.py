import logging
import logging.config
import os

global logger

LOG_PATH = "../log"

def makeLog():
    if not os.path.isdir(LOG_PATH):
        os.mkdir(LOG_PATH)
    logger = logging.getLogger("socket-logger")
    logging.basicConfig(LOG_PATH, encoding="utf-8", level=logging.DEBUG)
    logging
    

def startLog():
    
    
    
    

def gracefulShutdown(logFileToClose):
    print("Closing Gracefully...")
    logFileToClose.write("\nClosing Gracefully\n")
    logFileToClose.flush()
    logFileToClose.close()
    exit(0)
