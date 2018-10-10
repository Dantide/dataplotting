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
    log_current = []
    for line in file_path:
        data_list = line.split()
        if len(data_list) == 5:
            voltage1.append(float(data_list[0]))
            current1.append(float(data_list[1]))
            voltage2.append(float(data_list[2]))
            current2.append(float(data_list[3]))
            # log_current.append(float(data_list[4]))
    file_path.close()
    return [voltage1, current1, voltage2, current2, log_current]


single_led_lists = parse_data("1.3c.txt")
single_led_voltage1 = single_led_lists[0]
single_led_current1 = single_led_lists[1]

model_led_current = list(map(lambda x: 6 * x, single_led_current1))
model_led_voltage = list(map(lambda x, y: 6 * y + 270 * x, single_led_current1, single_led_voltage1))
model_led_log_current = list(map(lambda x: math.log10(x), model_led_current))

led_ribbon_lists = parse_data("1.3d.txt")
led_ribbon_voltage1 = led_ribbon_lists[0]
led_ribbon_current1 = led_ribbon_lists[1]

led_ribbon_log_current1 = list(map(lambda x: math.log10(math.fabs(x)), led_ribbon_current1))


trace1 = go.Scatter(
    x=model_led_voltage,
    y=model_led_log_current,
    mode="lines",
    name="LED Single"
)

trace2 = go.Scatter(
    x=led_ribbon_voltage1,
    y=led_ribbon_log_current1,
    name="LED Ribbon",
    line=dict(
        width=4,
        dash='dash')
)

data = [trace1, trace2]
layout = dict(title="LED Ribbon and Single Diode Models",
              xaxis={'title': "Voltage (V)", 'gridcolor': '#bdbdbd'},
              yaxis={'title': "Log Current", 'gridcolor': '#bdbdbd'},
              font={'color': '#000', 'size': 16})
fig = dict(data=data, layout=layout)
py.plot(fig, filename="Lab 2.2.1: LED Ribbon and Cell Plots")

