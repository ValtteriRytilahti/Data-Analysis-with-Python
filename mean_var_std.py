import numpy as np
import numpy as np

def calculate(input_list):
    # Check if the input list has exactly 9 numbers
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")

    # Convert the list to a 3x3 numpy array
    array = np.array(input_list).reshape(3, 3)

    mean_columns = array.mean(axis=0).tolist()
    mean_rows = array.mean(axis=1).tolist()
    mean_total = array.mean().item()

    var_columns = array.var(axis=0).tolist()
    var_rows = array.var(axis=1).tolist()
    var_total = array.var().item()

    std_columns = array.std(axis=0).tolist()
    std_rows = array.std(axis=1).tolist()
    std_total = array.std().item()

    max_columns = array.max(axis=0).tolist()
    max_rows = array.max(axis=1).tolist()
    max_total = array.max().item()

    min_columns = array.min(axis=0).tolist()
    min_rows = array.min(axis=1).tolist()
    min_total = array.min().item()

    sum_columns = array.sum(axis=0).tolist()
    sum_rows = array.sum(axis=1).tolist()
    sum_total = array.sum().item()

    calculations = {
        'mean': [mean_columns, mean_rows, mean_total],
        'variance': [var_columns, var_rows, var_total],
        'standard deviation': [std_columns, std_rows, std_total],
        'max': [max_columns, max_rows, max_total],
        'min': [min_columns, min_rows, min_total],
        'sum': [sum_columns, sum_rows, sum_total]
    }

    return calculations