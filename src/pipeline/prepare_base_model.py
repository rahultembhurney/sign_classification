from src.entity.entity_config import PrepareBaseModelConfig
from src.components.prepare_base_model import PrepareBaseModel
from src.config.configuration import ConfigurationManager


class PrepareModelPipeline():
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        base_model_config = config.get_base_model_config()
        base_model = PrepareBaseModel(config=base_model_config)
        base_model.get_base_model()
        base_model.get_updated_model()




if __name__ == "__main__":
    obj = PrepareModelPipeline()
    obj.main()
    