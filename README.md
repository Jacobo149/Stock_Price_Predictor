# Stock Price Predictor
Stock Price Predictor, the  web scraper scrapes the (user-determined) Yahoo finance page for the current stock price. The program executes this action 10 times over a (user-determined) time.  
The data processor class will use this data to run a linear regression to predict the next determined stock price.

## 3rd Party Libraries
- Requests
- BeautifulSoup
- Pandas
- Scikit-learn
- Time


## How To Run
- Download repository
- Download 3rd party libraries
- Run application
```
python Main.py
```
- When prompted, input desired time interval between data collection points and the ticker symbol of the desired company
