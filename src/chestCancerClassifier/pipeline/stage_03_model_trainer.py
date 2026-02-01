from chestCancerClassifier.config.configuration import ConfigurationManager
from chestCancerClassifier.components.model_training import Training
from chestCancerClassifier import logger

STAGE_NAME = "Training"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()

if __name__ == "__main__":
    try:    
        logger.info("**************************")
        logger.info(f"\n\n>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<\n")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<\n\nx================x")
    except Exception as e:
        raise e

    