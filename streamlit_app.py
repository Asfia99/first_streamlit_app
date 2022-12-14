import streamlit
import pandas
import snowflake.connector
import requests
from urllib.error import URLError

streamlit.title('My parents\' healthy diner')

streamlit.header('Breakfast Favourities')
streamlit.text('ð¥£ Omega & Blueberry Oatmeal')
streamlit.text('ð¥ Kale Spinach Rocket Smoothie')
streamlit.text('ð Hard Boiled Free Range egg')
streamlit.text('ð¥ðAvocado Toast')

streamlit.header('ðð¥­ Build Your Own Fruit Smoothie ð¥ð')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# Display the table on the page.
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)


#######fruityvice_response = requests.get("https://fruityvice.com/api/fruit/all")


#New Section to display fruityvice api response
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
  
streamlit.header("Fruityvice Fruit Advice!")  
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)

except URLError as e:
  streamlit.error()
    
##not running anything past this point, troubleshooting
##streamlit.stop()


#streamlit.header("The fruit load list contains:")
streamlit.header("The fruit load list contains:")

##snowflake related functions
def get_fruit_load_list():
    my_cur = my_cnx.cursor()
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()

##add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)
 

#streamlit.stop()
def insert_row_snowflake(new_fruit):
  my_cur = my_cnx.cursor()
  my_cur.execute("insert into fruit_load_list values ('"+ new_fruit +"')")
  return "Thanks for adding"  + new_fruit

add_my_fruit = streamlit.text_input('What fruit would you like to add?')

if streamlit.button('Add a Fruit to the List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit)
  streamlit.text(back_from_function)

 #my_cur.execute("insert into fruit_load_list values ('from streamlit')")

streamlit.header('View Our Fruit List - Add Your Favourites!')
if streamlit.button('Get Fruit List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  my_cnx.close()
  streamlit.text(my_data_rows)


