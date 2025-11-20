import streamlit as st

pages = [
    st.Page(page="pages/page1.py", tittle="Home", icon="🏠"),
    st.Page(page="pages/page2.py", tittle="Visualisasi Data", icon="📊"),
    st.Page(page="pages/page3.py", tittle="Settings", icon="⚙️",)
]

pg = st.navigation(
    pages,
    position="sidebar",
    expanded=True
)

pg.run()