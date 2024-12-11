import io
import socket
import threading
import os
import time
from datetime import date
import atexit


def __main__(): #The initializer
    print("Splitting off, you got 10 seconds to stop me before we start the process...\nDont worry, if something goes wrong, the part i used to be will be gone too...")
    time.sleep(10)
    print("Executing...")

    logFile = startLog()
    atexit.register(gracefulShutdown(logFile))
    print("Log File Established...")
    logFile.close()

    # netThread = threading.Thread()
    # __listener(netThread.start(), 65534)

def gracefulShutdown(logFileToClose):
    print("Closing Gracefully...")
    logFileToClose.write("\nClosing Gracefully\n")
    logFileToClose.flush()
    logFileToClose.close()
    exit(0)


def startLog():
    plog = open(f"../log/{time.strftime(f"[%M-%d-%Y-%I-%M]")}.txt", "a")
    plog.write(f"{time.strftime(f"[%M/%d/%Y, %I:%M, %A] Logging Startup!\n")}")
    plog.flush()
    return plog

def network():
    netsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 65445)
    netsock.setblocking(True)
    netsock.setsockopt()
    
__main__()
#TODO: make sure to add __main__

    