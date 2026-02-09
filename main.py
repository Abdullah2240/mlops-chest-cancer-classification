import os
import shutil
from chestCancerClassifier import logger
from chestCancerClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from chestCancerClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from chestCancerClassifier.pipeline.stage_03_model_trainer import ModelTrainingPipeline
from chestCancerClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"\n\n>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<\n")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<\n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e 


STAGE_NAME = "Prepare Base Model"
try:
    logger.info("**************************")
    logger.info(f">>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
    obj = PrepareBaseModelPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<\n\nx======================x\n")
except Exception as e:
    raise e


STAGE_NAME = "Training"
try:    
    logger.info("**************************")
    logger.info(f"\n\n>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<\n")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<\n\nx================x")

except Exception as e:
    raise e




STAGE_NAME = "Evaluation"
try:
    logger.info("**************************")
    logger.info(f">>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<\n\nx======================x\n")
except Exception as e:
    raise e
