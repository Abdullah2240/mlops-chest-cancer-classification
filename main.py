from chestCancerClassifier import logger
from chestCancerClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"\n\n>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<\n")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<\n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e 