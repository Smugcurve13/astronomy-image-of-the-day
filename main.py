import streamlit as st
import requests

api_key = 'pibf0KFEKtygZEIj9MnWIfXoawkXSRXgkjrPXJVg'

url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'

response = requests.get(url)

content = response.json()

# with open('apod.json','w') as file:
#     file.write(str(content))

# print(content)

st.title(f'{content['title']}\n')
st.image(content['hdurl'])
st.write(f'\n{content['explanation']}')