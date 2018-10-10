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
    current2 = []
    log_current = []
    optical_power = []
    wall_plug = []
    for line in file_path:
        data_list = line.split()
        if len(data_list) == 6:
            voltage1.append(float(data_list[0]))
            current1.append(float(data_list[1]))
            current2.append(float(data_list[2]))
            log_current.append(float(data_list[3]))
            optical_power.append(float(data_list[4]))
            wall_plug.append(float(data_list[5]))
    file_path.close()
    return [voltage1, current1, current2, log_current, optical_power, wall_plug]


amber_lists = parse_data("1.2amb.txt")
amber_current1 = amber_lists[1]
amber_optical_power = amber_lists[4]
amber_wall_plug = amber_lists[5]

royal_blue_lists = parse_data("1.2roy.txt")
royal_blue_current1 = royal_blue_lists[1]
royal_blue_optical_power = royal_blue_lists[4]
royal_blue_wall_plug = royal_blue_lists[5]

# Plot Optical Power vs Drive Current
trace1 = go.Scatter(
    x=amber_current1,
    y=amber_optical_power,
    name='Amber LED',
    line=dict(
        color='rgb(255, 191, 0)',
        width=4,
        dash='dash')
)

trace2 = go.Scatter(
    x=royal_blue_current1,
    y=royal_blue_optical_power,
    name='Royal Blue LED',
    line=dict(
        color='rgb(65, 105, 255)',
        width=4,
        dash='dash')
)

data = [trace1, trace2]
layout = dict(title="Optical Power vs Drive Current LEDs",
              xaxis={'title': "Current (A)", 'gridcolor': '#bdbdbd'},
              yaxis={'title': "Optical Power (mW)", 'gridcolor': '#bdbdbd'},
              paper_bgcolor='rgba(255,255,255,1)',
              plot_bgcolor='rgba(255,255,255,1)',
              font={'color': "#000", 'size': 16}
)
fig = dict(data=data, layout=layout)
py.plot(fig, filename="Lab 2.1.2: Power vs Drive Current Plots")


# Plot Device Efficiency vs Drive Current
trace1 = go.Scatter(
    x=amber_current1,
    y=amber_wall_plug,
    name='Amber LED',
    line=dict(
        color='rgb(255, 191, 0)',
        width=4,
        dash='dash')
)

trace2 = go.Scatter(
    x=royal_blue_current1,
    y=royal_blue_wall_plug,
    name='Royal Blue LED',
    line=dict(
        color='rgb(65, 105, 255)',
        width=4,
        dash='dash')
)

data = [trace1, trace2]
layout = dict(title="Wall Plug Efficiency vs Drive Current LEDs",
              xaxis={'title': "Current (A)", 'gridcolor': '#bdbdbd'},
              yaxis={'title': "Wall Plug Efficiency (%)", 'gridcolor': '#bdbdbd'},
              paper_bgcolor='rgba(255,255,255,1)',
              plot_bgcolor='rgba(255,255,255,1)',
              font={'color': "#000", 'size': 16})
fig = dict(data=data, layout=layout)
py.plot(fig, filename="Lab 2.1.2: Efficiency vs Drive Current Plots")
