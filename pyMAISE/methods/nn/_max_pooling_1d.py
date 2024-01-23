from keras.layers import MaxPooling1D

from pyMAISE.methods.nn._layer import Layer


class MaxPooling1DLayer(Layer):
    def __init__(self, layer_name, parameters):
        # Initialize layer data
        self.reset()
        super().__init__(layer_name, parameters)

        # Build layer data
        self._data = super().build_data(self._data, parameters)

    # ==========================================================================
    # Methods
    def build(self, hp):
        # Set pyMAISE hyperparameters to keras-tuner hyperparameters
        sampled_data = super().sample_parameters(self._data, hp)
        return MaxPooling1D(**sampled_data)

    def reset(self):
        self._data = {
            "pool_size": 2,
            "strides": None,
            "padding": "valid",
            "data_format": "channels_last",
        }
        super().reset()

    def increment_layer(self):
        return super().increment_layer()

    # ==========================================================================
    # Getters
    def num_layers(self, hp):
        return super().num_layers(hp)

    def sublayer(self, hp):
        return super().sublayer(hp)

    def wrapper(self):
        return super().wrapper()
