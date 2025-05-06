from src.datascience import logger
from src.datascience.pipeline.data_ingestion_stage import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_stage import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformation_stage import DataTransformationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"Started {STAGE_NAME} ...........")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.data_ingestion()
    logger.info(f"Completed {STAGE_NAME} ..........")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f"Started {STAGE_NAME} ...........")
    data_validation = DataValidationTrainingPipeline()
    data_validation.data_validation()
    logger.info(f"Completed {STAGE_NAME} ..........")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f"Started {STAGE_NAME} ...........")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.data_transformation()
    logger.info(f"Completed {STAGE_NAME} ..........")
except Exception as e:
    logger.exception(e)
    raise e