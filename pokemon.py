import streamlit as st
import requests


def get_info(name):
    base_url = "https://pokeapi.co/api/v2/"
    url = f"{base_url}pokemon/{name}"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        st.error(f"Could not load {name}: {error}")
        return None


st.title("PokéAPI Inspector")

name = st.text_input("Enter the name of the Pokémon").lower().strip()

if name:
    info = get_info(name)

    if info:
        st.image(info["sprites"]["front_default"], width=200)
        detail = st.text_input("Enter a detail to inspect", placeholder="height")

        if st.button("Search", type="primary") and detail:
            if detail in info:
                st.success("Detail found")
                st.write(f"**{detail.upper()}**: {info[detail]}")
            else:
                st.error(f"'{detail}' is not a valid Pokémon detail.")


