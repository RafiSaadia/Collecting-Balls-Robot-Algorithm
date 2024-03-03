clear;close all;clc;
%%
%-----------------%
%-----Params------%
%-----------------%
Kt  = 0.1868; % [kg·cm/A] % the torque constant derived from the stall ...
% torque and stall current.
K   = Kt;% []  % is the motor torque constant
J   = 1e-6;% [Kg*m^2]  % is the rotor's moment of inertia
B   = 1e-5;% [N*m*s]  % is the viscous damping coefficient.
L   = 1;% []  % is the armature inductance.
R   = 2.857;% [Hoam]  % is the armature resistance
Ke  = Kt;% []  % is the back electromotive force (EMF) constant...
% , often assumed to be equal to Kt in SI Units
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%           Tf =  K/((Js + B)*(Ls +R) + Ke*Kt)    %
%   Tf =  K/(J*L*s^2 + (J*R + B*L)s B*R + Ke*Kt)  %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
