import streamlit as st

st.title("Галерия от любими животни")

# Инициализация на списъка
if "animals" not in st.session_state:
    st.session_state.animals = []

st.header("Добави ново животно")
name = st.text_input("Име на животното")
description = st.text_area("Описание")
image_url = st.text_input("URL на картинката")

if st.button("Добави"):
    if name and description and image_url:
        st.session_state.animals.append({
            "име": name,
            "описание": description,
            "картинка": image_url
        })
        st.success(f"{name} е добавено!")
    else:
        st.warning("Попълнете всички полета!")

st.header("Премахни животно")
remove_name = st.text_input("Име на животното за премахване")

if st.button("Премахни"):
    removed = False
    for a in st.session_state.animals:
        if a["име"] == remove_name:
            st.session_state.animals.remove(a)
            removed = True
            break

    if removed:
        st.success(f"{remove_name} е премахнато")
    else:
        st.warning(f"{remove_name} не е намерено")

st.header("Галерия")
if st.session_state.animals:
    cols = st.columns(3)
    for idx, animal in enumerate(st.session_state.animals):
        with cols[idx % 3]:
            st.subheader(animal["име"])
            st.image(animal["картинка"], use_column_width=True)
            st.write(animal["описание"])
else:
    st.info("Галерията е празна. Добавете животни!"
