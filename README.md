# Finzome_Technologies_Financial_Data_Analysis

### Overview

This Flask-based web application allows users to upload financial market data in either CSV or Excel format. The application processes the data to calculate daily and annualized volatility, and then displays the results along with the data table on the web page.

### Requirements

Before running the application, make sure you have the following modules installed:

- Flask
- pandas

You can install the required modules using the following command:

```bash
pip install Flask pandas
```

To upload and manipulate excel(.xlsx) files install the following library
```bash
pip install openpyxl
```


To Run the Flask application:

   ```bash
   python app.py
   ```

4. Open your web browser and go to [http://localhost:5000](http://localhost:5000).

5. Upload a financial market data file (CSV or Excel) using the provided form.

6. View the calculated daily and annualized volatility, along with the data table.

### Project Structure

- **app.py**: Flask application script containing the main logic for processing financial data and rendering the web page.
- **templates/index.html**: HTML template for the web page with file upload form and result display.

### Dependencies

- [Flask](https://pypi.org/project/Flask/): A web framework for Python.
- [pandas](https://pypi.org/project/pandas/): A data manipulation library for Python.
