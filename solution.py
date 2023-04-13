import pandas as pd
import numpy as np


chat_id = 2090817777

def solution(...) -> bool: 
    alpha = 0.08
    threshold = 300
    mean = sum(data) / len(data)
    std = stats.tstd(data)
    n = len(data)
    t_stat = (mean - threshold) / (std / (n**0.5))
    crit_val = stats.t.ppf(alpha, df=n-1)
    return t_stat < alpha
