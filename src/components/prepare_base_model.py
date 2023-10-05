from src.entity.entity_config import PrepareBaseModelConfig
from src.config.configuration import ConfigurationManager
import tensorflow as tf
from src.utils.commons import *


class PrepareBaseModel():
    def __init__(self, config: PrepareBaseModelConfig):
        self.config=config

    def get_base_model(self):
        self.model = tf.keras.applications.vgg16.VGG16(
            include_top=False,
            input_shape=[224,224,3],
            weights="imagenet"
        )

        save_model(filepath=self.config.base_model_path,
                   model=self.model)
        
    @staticmethod
    def _prepare_updated_model(model,
                               classes,
                               ):
        for layer in model.layers:
            layer.trainable=False

        flatten_in = tf.keras.layers.Flatten()(model.input)
        prediction = tf.keras.layers.Dense(units=classes,
                                           activation="softmax")(flatten_in)
        
        full_model = tf.keras.models.Model(
            inputs= model.input,
            outputs= prediction
        )

        full_model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
                           loss=tf.keras.losses.CategoricalCrossentropy(),
                           metrics=["accuracy"])
        
        full_model.summary()

        return full_model
    
    def get_updated_model(self):
        self.full_model = self._prepare_updated_model(model=self.model,
                                                 classes=5)
        
        save_model(model=self.full_model, filepath=self.config.updated_model_path)


