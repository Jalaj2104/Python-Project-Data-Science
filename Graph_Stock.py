import yfinance as yf
import pandas as pd
from bs4 import BeautifulSoup
import requests
import plotly.graph_objecta as go
from plotly.subplots import make_subplots
import plotly.io as pio
pio.renders.default = "iframe"
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
