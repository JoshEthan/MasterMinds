from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

ts = TimeSeries(key="VEBHU4J9S5T4AR81", output_format='pandas')
data, meta_data = ts.get_intraday(
    symbol='MSFT', interval='1min', outputsize='full')
print(data.head(2))
print(meta_data)
