import  logging
import os
from datetime import datetime


# i will create my log file from this how my log file is get created
Log_file=f" {datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #the file name is getting created based on whatever the current datetime (datetime.now())strftime this will convert actual datetime to string this will be the text file
Logs_path=os.path.join(os.getcwd(),"Logs",Log_file) #this will creates the folder to store our created files
os.makedirs(Logs_path,exist_ok=True) #the created files will append in this folder.

LOG_FILE_PATH=os.path.join(Logs_path,Log_file)


# when we want to overwrite the logging functionality of the  login we have to probably set this up in basic congig
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] (%(lineno)d %(name)s - %(levelname)s -%(message)s ",
    level=logging.INFO # in the place of INFO only i will print specific message 


)

# wherever i use logging.info i will import logging.info and i will write any print message on that time i will going to use this kind of format only 
# it will create the file path,and gives the particular format and with respect to the message  and all 




    