"""Parameter layer in TensorFlow."""

import tensorflow as tf
from tensorflow.python.ops.gen_array_ops import broadcast_to


def parameter(input_var,
              length,
              initializer=tf.zeros_initializer(),
              dtype=tf.float32,
              trainable=True,
              name='parameter'):
    """
    Parameter layer.

    Used as layer that could be broadcast to a certain shape to
    match with input variable during training.
    Example: A trainable parameter variable with shape (2,), it needs to be
    broadcasted to (32, 2) when applied to a batch with size 32.

    Args:
        input_var (tf.Tensor): Input tf.Tensor.
        length (int): Integer dimension of the variables.
        initializer (callable): Initializer of the variables. The function
            should return a tf.Tensor.
        dtype: Data type of the variables (default is tf.float32).
        trainable (bool): Whether these variables are trainable.
        name (str): Variable scope of the variables.

    Return:
        A tensor of the broadcasted variables.
    """
    with tf.variable_scope(name):
        p = tf.get_variable(
            'parameter',
            shape=(length, ),
            dtype=dtype,
            initializer=initializer,
            trainable=trainable)

        broadcast_shape = tf.concat(
            axis=0, values=[tf.shape(input_var)[:-1], [length]])
        p_broadcast = broadcast_to(p, shape=broadcast_shape)
        return p_broadcast
