This app extracts the last 10 days of stock data from Yahoo! Finance and displays them in a graph

There are basically two URLs:

/webstock/goc/<string_company_name>/<date>   -   This returns a JSON object of the stored database stock information of the respective company on the respective date

/webstock/goc_range/<string_company_name>/<start_date>/<end_date>    -    This uses CanvasJS to draw a range graph to show the opening and closing prices of the company in between the two dates

I have not added any styling to the first page since it's just a JSON object being displayed.