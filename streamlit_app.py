import streamlit
import pandas

streamlit.title('My parents\' healthy diner')

streamlit.header('Breakfast Favourities')
streamlit.text('🥣 Omega & Blueberry Oatmeal')
streamlit.text('🥗 Kale Spinach Rocket Smoothie')
streamlit.text('🐔 Hard Boiled Free Range egg')
streamlit.text('🥑🍞Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
