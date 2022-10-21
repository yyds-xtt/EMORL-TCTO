import math


class EnvConfig:
    A = 0.503  # Rotor disc area (m2)
    d0 = 0.6  # Fuselage drag ratio
    d_max = 30  # Maximal distance the UAV can move (m)
    f_U = 1  # Computing capability of the UAV (GHz)
    g = 0.05  # Rotor solidity
    N_max = 10  # Maximum number of tasks in the computing queue
    P1 = 79.86  # Blade profile power
    P2 = 88.63  # Induced power
    P_U = 1  # Transmission power of the UAV (W)
    U_tip = 120  # Tip speed of rotor blade (m/s)
    v0 = 4.03  # Mean rotor induced velocity in hover
    v_max = 30  # Maximum flying velocity of the UAV (m/s)
    W = 10  # Channel bandwidth (MHz)
    rho = 1.225  # Air density (km/m3)
    theta_max = math.pi / 4  # Maximal azimuth angle (rad)
    kappa = 1e-26  # Effective capacitance coefficient
    sigma_square = 1e-6  # Background noise power (W)

class RLConfig:
    G_max = 100  # Number of maximum evolution generations
    P_num = 200  # Number of the performance buffers
    P_size = 2  # Size of each performance buffer
    gamma = 0.995  # Discount factor
    epsilon = 0.2  # Clipping parameter
    lambda_ = 0.95  # Parameter of general advantage estimator
    n_warm = 60  # Number of warm-up iterations
    n_evo = 10  # Number of task iterations
    delta = 4  # Number of divisions of weight vectors
