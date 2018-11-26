import plotly
import math
import plotly.plotly as py
import plotly.graph_objs as go
plotly.tools.set_credentials_file(username='Dantide', api_key='yxopUzjN78CLtRZ5Kl0i')

def parse_data(file_name: str):
    """Parse through a data file for section 1.1 of ECE 2100 lab 4."""
    assert(isinstance(file_name, str))
    file_path = open(file_name, 'r')
    file_path.readline()
    frequency = []
    voltage_in = []
    current_in = []
    impedance = []
    for line in file_path:
        data_list = line.split()
        if len(data_list) == 3:
            frequency.append(float(data_list[0]))
            voltage_in.append(float(data_list[1]))
            current_in.append(float(data_list[2]))
            impedance.append(float(data_list[3]))
    file_path.close()
    return [frequency, current_in, voltage_in, impedance]


single_box_lists = parse_data("singlebox.txt")
single