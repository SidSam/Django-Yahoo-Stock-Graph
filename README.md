This app extracts the last 10 days of stock data from Yahoo! Finance and displays them in a graph

There are basically two URLs:

/webstock/goc/string_company_name/date   -   This returns a JSON object of the stored database stock information of the respective company on the respective date

/webstock/goc_range/string_company_name/start_date/end_date    -    This uses CanvasJS to draw two line graphs to show the opening and closing prices of the company in between the two dates

The dates are in DDMMYYYY format.

The company name is entered as its symbol. Example - 'YHOO' for Yahoo and 'ADBE' for Adobe

I have not added any styling to the first page since it's just a JSON object being displayed, and no styling in the second page either as it's just a graph.

Since this app uses CanvasJS and the Yahoo! Finance PyPi module, you'd have to install them to make the app run on your machine.

You can download the CanvasJS graph scripts from the offical site (http://canvasjs.com/download-html5-charting-graphing-library/) and install Yahoo! Finance by running

    pip install yahoo-finance
