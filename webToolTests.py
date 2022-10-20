# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 14:52:47 2022

@author: william.chupp
"""

# importing modules
import streamlit as st
import pandas as pd
import numpy as np

st.image('CMAQToolkitLogo.png')
'''
# Bicycle and Pedestrian Improvements

This calculator will estimate the reduction in emissions resulting from 
improvements to bicycle and pedestrian infrastructure and associated mode
shift from passenger vehicles to bicycling or walking, including but not 
limited to sidewalks, dedicated bicycle infrastructure, improved wayfinding, 
mid-block crossing installations, bike share systems, and bike parking 
improvements.

## INPUT										
        
'''
st.button('Reset Inputs')
yearSelect = range(2018, 2041)
col1, col2 = st.columns(2)
with col1:
    '''
        What is your project evaluation year?'''

with col2:
    year = st.selectbox('Project Evaluation Year', yearSelect, label_visibility='collapsed')


#  This is the pywebio hello-world

# # classify person
# class calculation:

# 	# defining method
# 	def BMIcalculator(Height, Mass):

# 		for t1, t2 in [(16, 'severely underweight'),
# 					(18.5, 'underweight'),
# 					(25, 'normal'),
# 					(30, 'overweight'),
# 					(35, 'moderately obese'),
# 					(float('inf'), 'severely obese')]:
# 			if BMI <= t1:
# 				put_text('Your BMI is', BMI, 'and the person is :', t2)
# 				break

# # classify and compute BMI
# class calculation:

# 	# defining method
# 	def BMIcalculator(self, Height, Mass):

# 		# compute BMI
# 		BMI = (Mass)/(Height*Height)

# 		# classify
# 		for t1, t2 in [(16, 'severely underweight'),
# 					(18.5, 'underweight'),
# 					(25, 'normal'), (30, 'overweight'),
# 					(35, 'moderately obese'),
# 					(float('inf'), 'severely obese')]:

# 			if BMI <= t1:
# 				put_text('Your BMI is', BMI, 'and the person is :', t2)
# 				break


# # height input
# Height = input("Please enter height in meters(m)", type=FLOAT)

# # Mass input
# Mass = input("Please enter Mass/Weight in Kilograms(Kg)", type=FLOAT)

# obj = calculation()
# obj.BMIcalculator(Height, Mass)

