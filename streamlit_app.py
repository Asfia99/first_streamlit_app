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
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# Display the table on the page.
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/all")

streamlit.header("Fruityvice Fruit Advice!")
#streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
# normalises the data and puts it in a dataframe
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

streamlit.dataframe(fruityvice_normalized)


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
