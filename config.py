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
    rho = 1.225  # Air density (kg/m3)
    theta_max = math.pi / 4  # Maximal azimuth angle (rad)
    kappa = 1e-26  # Effective capacitance coefficient
    sigma_square = 1e-6  # Background noise power (W)
    x_max, y_max = 400, 400  # Maximum side lengths of rectangular area (m)
    tau = 1  # Time slot (s)
    T = 300  # Number of time slots
    alpha = 5  # Input data size of a computation task (MB)
    beta = 1e9  # Number of CPU cycles required to execute the task
    zetas_candidate = [0.3, 0.5, 0.7]  # candidate parameters of Bernoulli random variables

    # Path loss parameters
    A0 = 3.04
    B9 = -23.29
    theta0 = -3.61
    C0 = 4.14
    eta0 = 20.7

    K = 60  # Number of SDs
    H = 30  # Number of flying altitude (m)


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
    n = 15

    learning_rate = 0.0001
