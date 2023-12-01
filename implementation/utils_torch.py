import torch
import torch.nn.functional as F
import numpy as np

def hat(x):
    A = torch.zeros((3, 3), dtype=x.dtype)
    A[0, 1:] = torch.tensor([-x[2], x[1]], dtype=x.dtype)
    A[1, ::2] = torch.tensor([x[2], -x[0]], dtype=x.dtype)
    A[2, :2] = torch.tensor([-x[1], x[0]], dtype=x.dtype)
    return A

def hat(x):
    A = torch.zeros((3, 3),dtype=x.dtype)
    z = torch.zeros(1)
    row1 = torch.cat([z,-x[2:3],x[1:2]])
    row2 = torch.cat([x[2:3],z,-x[0:1]])
    row3 = torch.cat([-x[1:2],x[0:1],z])
    res = torch.stack([row1,row2,row3])


    return res


def hat_inv(S):
    x = torch.zeros(S.shape[0], dtype=S.dtype)
    x[0] = S[2, 1]
    x[1] = S[0, 2]
    x[2] = S[1, 0]
    return x

def check_orth(A):
    return torch.norm(torch.eye(A.shape[0], dtype=A.dtype) - A @ A.t(), p="fro")

def get_orth(n, seed=1):
    torch.manual_seed(seed)
    Q, R = torch.linalg.qr(torch.rand(n, n, dtype=torch.float64))
    return Q

def cay(A):
    I = torch.eye(A.shape[0], dtype=A.dtype)
    return torch.inverse(I - 0.5 * A) @ (I + 0.5 * A)

def rodrigues(A):
    alpha = (1 / np.sqrt(2)) * torch.norm(A, p="fro")
    return torch.eye(A.shape[0], dtype=A.dtype) + \
           (torch.sin(alpha) / alpha) * A + \
           ((1 - torch.cos(alpha)) / alpha**2) * torch.matmul(A, A)

def frob_log(A):
    alpha = (1 / np.sqrt(2)) * torch.norm(A, p="fro")
    if alpha < 1e-14:
        return torch.tensor(0, dtype=A.dtype)
    elif torch.abs(alpha) < torch.tensor(np.pi, dtype=A.dtype):
        return torch.abs((alpha / (2 * torch.sin(alpha)))) * torch.norm((A - A.t()), p="fro")
    else:
        return np.sqrt(2) * torch.abs(alpha)

def dist_so3(R1, R2):
    return (1 / np.sqrt(2)) * frob_log(R1.t() @ R2)

def dist_trajectory(Rs):
    dist = torch.tensor(0, dtype=Rs[0].dtype)
    for R1, R2 in zip(Rs[:-1], Rs[1:]):
        dist += dist_so3(R1, R2)
    return dist