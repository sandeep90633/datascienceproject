from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_ingestion import DataIngestion
from src.datascience import logger


STAGE_NAME="Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def data_ingestion(self):
        config=ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
        

if __name__ == "__main__":
    try:
        logger.info(f"Started {STAGE_NAME} ...........")
        obj = DataIngestionTrainingPipeline()
        obj.data_ingestion()
        logger.info(f"Completed {STAGE_NAME} ..........")
    except Exception as e:
        logger.exception(e)
        raise e
