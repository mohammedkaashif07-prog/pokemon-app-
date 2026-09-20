import streamlit as st
import requests

def get_info(name):
    base_url = "https://pokeapi.co/api/v2/"
    url = f"{base_url}pokemon/{name}"

    with st.status('running'):
        try:
            
            response = requests.get(url, timeout = 5)

            if response.status_code == 200 :
                pokemon_data = response.json()
                return pokemon_data
                
            else :
                st.divider()
                st.badge("Search Failed")
                st.error(f"{name.upper()} is not found.") 

        except requests.exceptions.RequestException as e:
            st.error(f"Network error: {e}")
            return None

    st.title("🐾 PokéAPI Inspector")
            
    name = st.text_input("Enter the name of the pokemon (Q to quit): ").lower().strip()

    info = get_info(name)

    if info:
        detail = st.text_input("Search (Q to quit): ")
        clicked = st.button("Search")

        if clicked :
            if detail == 'q':
                pass
            else :
                try :
                    content = info[detail]
                    st.divider()
                    st.badge("Found")
                    st.image(info["sprites"]["front_default"])
                    st.write(f"{detail.upper()} : {content}")
                    st.balloons()

                except KeyError:
                    st.divider()
                    st.badge("Failed")
                    st.write(f"'{detail}' such detail is not found.")


