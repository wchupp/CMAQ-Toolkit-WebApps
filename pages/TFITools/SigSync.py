import streamlit as st
import pandas as pd
import numpy as np
from st_aggrid_cmaq import AgGrid
from st_aggrid_cmaq import GridOptionsBuilder, JsCode, GridUpdateMode, ColumnsAutoSizeMode
from utils import InputTable
from streamlit_extras import switch_page_button

def sigsync():
    st.markdown(
'''
# Traffic Signal Synchronization						

This calculator will estimate the emission reductions resulting from synchronizing the traffic signals along a previously unsynchronized corridor.

------					
''')

    st.markdown(
        '''
        <style>
        p {
            font-size: large;
            word-break: break-word;
        }
        li {
            word-break: break-word;
            }
        </style>
        ''',unsafe_allow_html=True
    )
    
    container2 = st.container()
    
    beforeAfter = pd.DataFrame({"Before":[0], "After": [0]})
    
    edited = st.experimental_data_editor(beforeAfter, use_container_width=True, width=100)
    # Put all new code here
    
    hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody tr th:first-child {display:none}
                button.step-up {display: none;}
                button.step-down {display: none;}
                div[data-baseweb] {border-radius: 4px;}
                </style>
                """
    
    # Inject CSS with Markdown
    st.markdown(hide_table_row_index, unsafe_allow_html=True)
    edited['change'] = edited['Before'] - edited['After']
    container2.table(edited)
    col1, col2 = st.columns([2, 1])
    rowLabels = range(6)
    collabels = ['Before', 'After']
    with col2:
        #table1 = InputTable.InputTable(dimensions=(6,2), rowLabels = rowLabels, colLabels = collabels)
        table1 = InputTable.InputTable(dimensions=(6,2), rowLabels = rowLabels, colLabels = collabels)
        st.table(table1.data)
        
        #table2 = InputTable.InputTable(dimensions=(6,2), rowLabels = rowLabels, colLabels = collabels)