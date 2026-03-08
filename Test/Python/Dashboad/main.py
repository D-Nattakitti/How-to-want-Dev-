import dash
from dash import dcc, html # แนะนำให้ใช้ import แบบใหม่นี้สำหรับ Dash 2.0+

# 1. แก้ไข __name__ ให้มี underline 2 ตัว
app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1('My Dashboard'), # 2. เติมคอมม่าตรงนี้
        dcc.Graph(
            id='My-Graph', 
            figure={
                'data': [ # 3. ใช้ d ตัวเล็ก
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Bar chart'}, # 4. เติมคอมม่าตรงนี้
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'line', 'name': 'line chart'}
                ],
                'layout': {
                    'title': 'Graph title', 
                    'xaxis': {'title': 'x-axis'}, # 5. ใช้ xaxis (ไม่มีขีด)
                    'yaxis': {'title': 'y-axis'}  # 6. ใช้ yaxis (ไม่มีขีด)
                }
            }
        )
    ]
)

# 7. แก้ไข __name__ และ __main__ ให้มี underline 2 ตัว
if __name__ == '__main__':
    app.run(debug=True)