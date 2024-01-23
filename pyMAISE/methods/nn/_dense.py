from keras.layers import Dense

from pyMAISE.methods.nn._layer import Layer


class DenseLayer(Layer):
    def __init__(self, layer_name, parameters: dict):
        # Initialize layer data
        self.reset()
        super().__init__(layer_name, parameters)

        # Build layer data
        self._data = super().build_data(self._data, parameters)

        # Assert keras non-default variables are defined
        assert self._data["units"] != None

    # ==========================================================================
    # Methods
    def build(self, hp):
        # Set pyMAISE hyperparameter to keras-tuner hyperparameter
        return Dense(**super().sample_parameters(self._data, hp))

    def reset(self):
        self._data = {
            "units": None,
            "activation": None,
            "use_bias": True,
            "kernel_initializer": "glorot_uniform",
            "bias_initializer": "zeros",
            "kernel_regularizer": None,
            "bias_regularizer": None,
            "activity_regularizer": None,
            "kernel_constraint": None,
            "bias_constraint": None,
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
