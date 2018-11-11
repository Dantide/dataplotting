import math
import plotly.plotly as py
import plotly.graph_objs as go


def parse_data(file_name: str):
    """Parse through a data file for section 1.2 of ECE 2100 lab 2."""
    assert(isinstance(file_name, str))
    file_path = open(file_name, 'r')
    file_path.readline()
    file_path.readline()
    voltage1 = []
    current1 = []
    voltage2 = []
    current2 = []
    cell_power = []
    for line in file_path:
        data_list = line.split()
        if len(data_list) == 5:
            voltage1.append(float(data_list[0]))
            current1.append(float(data_list[1]))
            voltage2.append(float(data_list[2]))
            current2.append(float(data_list[3]))
            cell_power.append(float(data_list[4]))
    file_path.close()
    return [voltage1, current1, voltage2, current2, cell_power]


dark_cell_lists = parse_data("2.1c-dark.txt")
dark_cell_voltage1 = dark_cell_lists[0]
dark_cell_current1 = dark_cell_lists[1]
dark_cell_log_current1 = list(map(lambda x: math.log10(x), dark_cell_current1))
dark_cell_power = dark_cell_lists[4]

light_cell_lists = parse_data("2.1d.txt")
light_cell_voltage1 = light_cell_lists[0]
light_cell_current1 = light_cell_lists[1]
light_cell_power = list(map(lambda x: -x if x < 0 else None, light_cell_lists[4]))

quarter_cell_lists = parse_data("2.1fquartercell.txt")
quarter_cell_voltage1 = quarter_cell_lists[0]
quarter_cell_power = list(map(lambda x: -x if x < 0 else None, quarter_cell_lists[4]))

whole_cell_lists = parse_data("2.1fwholecell.txt")
whole_cell_voltage1 = whole_cell_lists[0]
whole_cell_power = list(map(lambda x: -x if x < 0 else None, whole_cell_lists[4]))


# Plot Solar Cell Dark IV Curve
trace1 = go.Scatter(
    x=dark_cell_voltage1,
    y=dark_cell_log_current1,
    mode="lines",
    name="Solar Cell"
)

data = [trace1]
layout = dict(title="Log Current vs Voltage Solar Cell",
              xaxis={'title': "Voltage (V)", 'gridcolor': '#bdbdbd'},
              yaxis={'title': "Log Current", 'gridcolor': '#bdbdbd'},
              font={'color': '#000', 'size': 16})
fig = dict(data=data, layout=layout)
py.plot(fig, filename="Lab 2.2.1: Solar Cell Dark IV Plot")


# Plot Solar Cell Power vs Voltage, Full and Partial Exposure
trace1 = go.Scatter(
    x=light_cell_voltage1,
    y=light_cell_power,
    name="Solar Cell Full Exposure",
    line=dict(
        color='rgb(0, 0, 0)',
        width=4)
)

trace2 = go.Scatter(
    x=quarter_cell_voltage1,
    y=quarter_cell_power,
    name="Solar Cell Each Quarter Coverage",
    line=dict(
        color='rgb(0, 0, 0)',
        width=4,
        dash='dash')
)

trace3 = go.Scatter(
    x=whole_cell_voltage1,
    y=whole_cell_power,
    name="Solar Cell One Full Coverage",
    line=dict(
        color='rgb(0, 0, 0)',
        width=4,
        dash='dot')
)

data = [trace1, trace2, trace3]
layout = dict(title="Solar Cell Power vs Voltage in Full and Partial Exposure",
              xaxis={'title': "Voltage (V)", 'gridcolor': '#bdbdbd'},
              yaxis={'title': "Cell Power (W)", 'gridcolor': '#bdbdbd'},
              font={'color': '#000', 'size': 16})
fig = dict(data=data, layout=layout)
py.plot(fig, filename="Lab 2.1.1: Solar Cell in Full and Partial Exposure")


# Plot Solar Cell IV Curve
trace1 = go.Scatter(
    x=light_cell_voltage1,
    y=light_cell_current1,
    name="Solar Cell Full Exposure",
    mode='lines'
)

data = [trace1]
layout = dict(title="Solar Cell Full Exposure IV Curve",
              xaxis={'title': "Voltage (V)", 'gridcolor': '#bdbdbd'},
              yaxis={'title': "Current (A)", 'gridcolor': '#bdbdbd'},
              font={'color': '#000', 'size': 16})
fig = dict(data=data, layout=layout)
py.plot(fig, filename="Lab 2.1.1: Solar Cell Full Exposure IV Curve")
