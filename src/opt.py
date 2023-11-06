import numpy as np


def calculate_full_gradient(
    params: np.ndarray,
    loss_function,
    gradient_function=None,
    stochastic: bool = False,
    finite_difference: bool = False,
    eps: float = 1e-8,
):
    params = np.array(params)
    #

    if gradient_function is None or finite_difference == True:
        gradient_function = lambda p, d: numerical_gradient(
            p, d, loss_function=loss_function, eps=eps
        )

    grad = np.zeros_like(params)
    if stochastic:
        direction = np.random.choice([-1.0, 1.0], size=params.shape)
        grad_value = gradient_function(params, direction)
        grad += grad_value * direction
    else:
        for i in range(len(params)):
            direction = np.zeros_like(params)
            direction[i] = 1.0
            grad_value = gradient_function(params, direction)
            grad += grad_value * direction
    return grad


def numerical_gradient(
    params: np.ndarray,
    direction: np.ndarray,
    loss_function,
    eps: float = 1e-3,
):
    params_plus = params.copy()
    params_plus += eps * direction
    params_minus = params.copy()
    params_minus -= eps * direction
    grad_value = (loss_function(params_plus) - loss_function(params_minus)) / 2 / eps
    return grad_value
