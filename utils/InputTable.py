import streamlit as st
import pandas as pd
import numpy as np
from st_aggrid_cmaq import AgGrid
from st_aggrid_cmaq import GridOptionsBuilder, JsCode, GridUpdateMode, ColumnsAutoSizeMode
import extra_streamlit_components as stx

class InputTable:
    def __init__(self, dimensions=(0,0), rowLabels = [], colLabels = [], data = pd.DataFrame()):
        table = []
        
        if len(rowLabels)>0 and len(rowLabels) != (dimensions[0]):
           raise ValueError("Length of row labels does not equal the dimensions of the table. Row dimensions = {}; row labels length = {}".format(dimensions[0], len(rowLabels)))
        if len(colLabels)>0 and len(colLabels) != (dimensions[1]):
           raise ValueError("Length of column labels does not equal the dimensions of the table. Col dimensions = {}; col labels length = {}".format(dimensions[1], len(colLabels)))
        
        hasColLabels = 0
        if len(colLabels)>0:
            hasColLabels = 1
            
        for i in range(hasColLabels + dimensions[0]):
            

            hasRowLabels = 0
            if len(rowLabels)>0:
                hasRowLabels = 1
            
            if hasColLabels and hasRowLabels:
                colLabels.insert(0, "")
                
            cols = st.columns(hasRowLabels + dimensions[1])
            if hasColLabels:
                if i > 0:
                    table.append([])
            else:
                table.append([])

            j=0                
            for col in cols:
                if hasColLabels and i == 0:
                    col.write(str(colLabels[j]))
                elif hasRowLabels and j == 0:
                    col.write(str(rowLabels[i-hasColLabels])) 
                else:
                    table[i-hasColLabels].append(col.text_input(label="Table{}{}", label_visibility = 'collapsed', key="Table{}{}".format(i, j)))
                j+=1
        
        print(table)     
        self.data = table