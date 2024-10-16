# import streamlit
import streamlit
from streamlit_option_menu import option_menu

# import libraries
import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objs as go

# Título da página do streamlit
st.set_page_config(
    page_tite='Dashboard of Energy Cost'
    page_icon=':)',
    layout='wide'    
) 

# sidebar superior
st.sidebar.image()
