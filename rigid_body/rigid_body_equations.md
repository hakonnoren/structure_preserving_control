

## Kinematics on SO(3)

This introduction follows [3, Ch. 1.1] to a great extent.

Let $\{E_1,E_2,E_3 \}$ be an orthonormal basis attached to a  rotating body, called the *body frame* $\mathcal B$ and $\{e_1,e_2,e_3\}$ is the orthonormal fixed basis, called the *inertial reference frame*.

Any point $\tilde x \in \mathcal B$ can be related to a point in the inertial frame $x(t)$ by a (time dependent) rotation matrix $Q \in SO(3)$ by

$$
x = Q\tilde x
$$
Where 
$$
SO(3) := \{Q \in \R^{3 \times 3} \; | \; QQ^T = I, \; \text{det}(Q) = 1 \}.
$$

Since $Q = [q_1^T,q_2^T,q_3^T]^T$ is orthonormal, we find that for $i = 1,2,3$
$$
e_i = Qq_i
$$
meaning that $E_i = q_i$, i.e. the basis of $\mathcal B$ in the inertial reference frame is given by the rows of $Q$.

Consider now the time-derivative

$$
\begin{align}
\dot x &= \dot Q \tilde x\\
&= \dot QQ^T x\\
&= S(\omega) x
 \end{align}
$$
Where we introduced $\omega \in \R^{3}$ as the angular velocity (in the inertial frame) such that $S(\omega) = \dot QQ^T$, by
$$
S(\omega) = \begin{bmatrix}
0 &  \omega_3 & -\omega_2\\
-\omega_3 & 0 & \omega_1\\
\omega_2 & - \omega_1 & 0
\end{bmatrix}
$$.
This could be done, since it is seen that $\dot QQ^T$ is skew symmetric by considering $\frac{d}{dt}(QQ^T) = 0$.

Similarly, since $Q^T$ is a map from the inertial frame to the body frame

$$
\begin{align}
Q^T\dot x &= Q^T\dot Q \tilde x\\
&= Q^T\dot Q x\\
&=S(W) x
 \end{align}
$$
with $W \in \R^{3}$ such that $S(W) = Q^T\dot Q$. We denote $W$ as the body angular velocity.

It thus follows that the rotation of the rigid body $Q$ is given by
$$
\dot Q = S(\omega) Q = QS(W).
$$

## Dynamics on Lie groups

The differential equation for $Q \in SO(3)$ is an example of an ODE on a manifold. The tangent space of Lie groups could be parametrized (?) by their corresponding Lie algebra. For $SO(3)$ we have the tangent space at $Q\in SO(3)$ given by 

$$
\mathcal T_Q SO(3) := \{ Q\xi \in \R^{3 \times 3}\; |\; \xi \in \mathfrak{so}(3) \}
$$
where $\mathfrak{so}(3)$ is the space of skew-symmetric matrices
$$
\mathfrak{so}(3) := \{A \in \R^{3 \times 3} \; | \; A^T + A = 0  \;\}.
$$

Since any skew-symmetric $3 \times 3$ matrix has three degrees of freedom, we let the $S : \R^3 \rightarrow \mathfrak{so}(3)$ denote the isomorphism between these two spaces.

The exponential map, $\text{exp}( \cdot ) $, is a map from a Lie group $G$ and its Lie algebra $\mathfrak g$. In other words, for $Q \in SO(3)$, we can find a $q \in \mathfrak so(3)$ such that $Q = \text{exp}(q)$. 

# Rigid body system

The rigid body system describes a mass spinning around its center. The angular momentum is given by 

$$
L = \mathcal I\omega
$$

Where $\mathcal I = \text{diag}\{I_1,I_2,I_3\} \in \R^{3\times 3}$ is the principal moments of intertia and $\omega \in \R^{3}$ is the angular velocity. By Newtons second law, the time derivative of the momentum is equal to external forces $F$. This gives us

$$
\begin{align}
F &= \frac{d}{dt}L\\
 &= S(\omega) \mathcal I\omega + \mathcal I \dot \omega
 \end{align}
$$

We can understand (can we?) why we get this result, by considering the sub-section below. Alternatively, this could be derived by Hamiltons prinicple from a Lagrangian, as done in [2, Ch. 6.3].

## Time derivative of function along the body frame

A time dependent, vector-valued function rotating along the body frame, is, given from the intertial frame by 

$$
f_{in} = Qf
$$
Computing the time-derivative we get, by the product-rule, that
$$
\begin{align}
\frac{d}{dt}f_{in} &= \dot Qf + Q\dot f\\
&= \dot QQ^Tf_{in} + Q\dot f\\
&= S(\omega) f_{in} + Q\dot f
\end{align}
$$

Since, by the orthogonality of $Q$
$$\frac{d}{dt}(QQ^T) = \dot QQ^T + Q\dot Q^T = 0$$
we find that $\dot QQ^T$ is skew symmetrix, which we relate to the angular velocity $\omega$ by the $S$ operator 
$$
S(\omega) = \begin{bmatrix}
0 &  \omega_3 & -\omega_2\\
-\omega_3 & 0 & \omega_1\\
\omega_2 & - \omega_1 & 0
\end{bmatrix} = \dot QQ^T
$$.

## Hamiltonian system


# References

[1] HLW. Geometric Numerical Integration

[2] Global formulations of Lagrangian and Hamiltonian dynamics on 
manifolds.

[3] Modeling and simulation of rigid body and rod dynamics via geometric methods. Ph.D. thesis. Niklas Säfström. (2009)