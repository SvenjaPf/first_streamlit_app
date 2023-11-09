import streamlit
import pandas

streamlit.title('Mel\'s Parents Healty Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Blueberry Pancakes')
streamlit.text('🐔Scrambled Eggs')
streamlit.text('🥑🍞 Avocado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# before:
#streamlit.dataframe(my_fruit_list)
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

# after:
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

