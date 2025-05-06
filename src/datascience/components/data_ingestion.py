import os
import urllib.request as request
from src.datascience import logger
import zipfile
from src.datascience.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    #Downloading the Zip file 
    def download_file(self):
        if not os.path.exists(self.config.local_dir_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename= self.config.local_dir_file
            )
            logger.info(f"{filename} downloaded! with following info: \n{headers}")
        else:
            logger.info("File already exists.")
            
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        
        with zipfile.ZipFile(self.config.local_dir_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)