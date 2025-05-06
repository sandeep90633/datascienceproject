import pandas as pd
from src.datascience.config.configuration import DataValidationConfig
from src.datascience import logger

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config= config
    
    def validate_all_columns(self) -> bool:
        try:
            validation_status = None
            
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            
            all_schema = self.config.all_schema.keys()
            
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        logger.error("Validation status is False....")
                        f.write(f"validation_status: {validation_status}")
                        
                    
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        logger.info("Validation status is True.......")
                        f.write(f"validation_status: {validation_status}")
            
            return validation_status
        
        except Exception as e:
            raise e