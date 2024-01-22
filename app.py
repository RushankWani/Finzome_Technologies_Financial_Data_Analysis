from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
app = Flask(__name__)


def process_data(file):
    Name,Extention = file.filename.split('.')
    df = pd.read_csv(file, index_col=False) if Extention == "csv" else pd.read_excel(file, index_col=False)
    df['Daily Returns'] = ( df['Close '] / df['Close '].shift(1)) -1
    Daily_Volatility = df['Daily Returns'].std()
    Annualized_Volatility = Daily_Volatility*(len(df)**(1/2))
    return df,Daily_Volatility,Annualized_Volatility

# Route for the main page
@app.route('/', methods=['GET', 'POST'])
# 
def index():
    if request.method == 'POST':
        # Check if file is uploaded
        if 'file' in request.files:
            file = request.files['file']
            df,Daily_Volatility,Annualized_Volatility = process_data(file)

        # Render the HTML page with the DataFrame content
        if df is not None:
            return render_template('index.html',valued=Daily_Volatility,valuea=Annualized_Volatility, table=df.to_html())
        else:
            return render_template('index.html', error="Error processing data")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
