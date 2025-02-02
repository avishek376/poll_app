import dash

from dash import html, dcc, Dash



app = Dash()

app.layout([
    html.Pre("Hello World...")
])

if __name__ == "__main__":
    app.run(debug=True)