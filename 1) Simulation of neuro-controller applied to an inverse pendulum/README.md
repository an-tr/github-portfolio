# Simulation of neuro-controller applied to an inverse pendulum

## The inverse pendulum problem
The inverted pendulum represents a classic example of a system 
inherently unstable system. Its dynamics are fundamental to tasks 
involving the maintenance of equilibrium. 
Many control design techniques have been studied using the 
pendulum.
The successful application of these techniques requires considerable 
knowledge of the system and an expression of the desired behaviour, usually in the form of an objective function. 
usually, in the form of an objective function.
The pendulum control problem, presented below, is dealt with in the 
case in which the dynamics of the system is not known a priori and the objective function 
is not given. All that is known are the values and ranges of the 
state variables of the pendulum and a failure signal, which must be 
minimised over time.
The balancing problem that is presented has been addressed through 
the use of multilayer neural networks.
 ![pendolo inverso](https://github.com/an-tr/github-portfolio/assets/140265380/9d9b2576-2d30-496d-8821-373278adf1a4)

## Solution to the inverse pendulum problem
The solution to the problem of 
pendulum balance was applied via a neural network 
multilayer neural network. 
Without an objective function, necessary to evaluate states and actions, changes 
to the controller can only be based on the failure signal. 
In the time interval between one failure and another, however, a
long sequence of actions resulting in difficulty in assigning a 
'judgement' necessary to describe which actions in the sequence have 
contributed to the failure.
Two functions are developed to solve this problem: the 
action, designed to map the current state into control actions, and the 
evaluation function, used to assign credit to individual actions. 
These two functions are learnt from the action network and 
by the evaluation network.
The overall architecture (image below) of the network is thus given by the two networks, 
action and evaluation, which constitute the output layer, and a second 
layer, hidden layer, to which the two networks are connected.
![architettura reti multistrato](https://github.com/an-tr/github-portfolio/assets/140265380/4edf514a-aeae-4491-a1b0-b1b9ebf494d6)
