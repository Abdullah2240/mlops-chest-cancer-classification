from chestCancerClassifier import logger
from chestCancerClassifier.components.model_evaluation_mlflow import Evaluation
from chestCancerClassifier.config.configuration import ConfigurationManager

STAGE_NAME = "Evaluation"

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        evaluation_config = config.getEvaluationConfig()
        evaluation = Evaluation(config=evaluation_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()
        

if __name__ == "__main__":
    try:        
        logger.info("**************************")
        logger.info(f">>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<\n\nx======================x\n")
    except Exception as e:
        raise e
    
        