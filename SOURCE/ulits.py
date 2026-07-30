import os
import sys
import pandas as pd
import numpy as np
from SOURCE.exception import Custom_Exception
import dill


def saved_objects(file_path,obj):

    try:
        dir_path_name=os.path.dirname(file_path)

        os.makedirs(dir_path_name,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise Custom_Exception(e,sys)
