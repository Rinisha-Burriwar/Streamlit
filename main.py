import streamlit as st
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image,ImageFilter,ImageEnhance,ImageTk

# image = Image.open("D://Engagement2/backgrounds/500x400.png")
# backgroundImage=ImageTk.PhotoImage(image)

# Title and Subheader
st.title("Exploratory Data Analysis App")
st.subheader("EDA Web App with Streamlit ")

filename = st.text_input('Enter a file path:')
def read_data(filename):
    with open(filename) as input:
        df = pd.read_csv(os.path.join(filename))
    return df
        

# Show Dataset
if st.checkbox("Preview DataFrame"):
	data = read_data(filename)
	if st.button("Head"):
		st.write(data.head())
	if st.button("Tail"):
		st.write(data.tail())
	else:
		st.write(data.head(2))

# Show Entire Dataframe
if st.checkbox("Show All DataFrame"):
	data = read_data(filename)
	st.dataframe(data)

# Show Description
if st.checkbox("Show All Column Name"):
	data = read_data(filename)
	st.text("Columns:")
	st.write(data.columns)

# Dimensions
data_dim = st.radio('What Dimension Do You Want to Show',('Rows','Columns'))
if data_dim == 'Rows':
	data = read_data(filename)
	st.text("Showing Length of Rows")
	st.write(len(data))
if data_dim == 'Columns':
	data = read_data(filename)
	st.text("Showing Length of Columns")
	st.write(data.shape[1])


if st.checkbox("Show Summary of Dataset"):
	data = read_data(filename)
	st.write(data.describe())


# Show Plots
if st.checkbox("Simple Bar Plot with Matplotlib "):
	data = read_data(filename)
	data.plot(kind='bar')
	st.pyplot()


# Show Plots
if st.checkbox("Simple Correlation Plot with Matplotlib "):
	data = read_data(filename)
	plt.matshow(data.corr())
	st.pyplot()

# Show Plots
if st.checkbox("Simple Correlation Plot with Seaborn "):
	data = read_data(filename)
	st.write(sns.heatmap(data.corr(),annot=True))
	# Use Matplotlib to render seaborn
	st.pyplot()

# Show Plots
if st.checkbox("Simple boxplot "):
	data = read_data(filename)
	st.write(sns.boxplot(data = data, orient="h", palette="Set2"))
	# Use Matplotlib to render seaborn
	st.pyplot()

