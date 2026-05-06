
from turtle import color

import streamlit as st
import pandas as pd


st.set_page_config("Youseif Hegazy CV")





st.markdown("""
<style>
.header-card {
    background-color: #ffffff;
    padding: 20px 30px;
    border-radius: 16px;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.08);
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 30px;
}

.header-left h2 {
    margin: 0;
    font-size: 26px;
    color: #2c7be5;
}

.header-left p {
    margin: 4px 0 0 0;
    color: #555;
    font-size: 15px;
}

.header-right p {
    margin: 4px 0;
    font-size: 15px;
    color: #333;
}
</style>

<div class="header-card">
<div class="header-left">
<h2>Youseif Hegazy</h2>
<p>Data Engineer</p>
</div>

<div class="header-right">
<p>Phone📞: 0115617785</p><p>Gmail✉️: youseifhegazy99@gmail.com</p>
</div>
</div>
""", unsafe_allow_html=True)



st.markdown("""
<style>
.about-card {
    background-color: #ffffff;
    padding: 24px 30px;
    border-radius: 16px;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.08);
    display: flex;
    gap: 24px;
    align-items: flex-start;
    max-width: 900px;
    margin-bottom: 30px;
}

.avatar {
    width: 130px;
    height: 130px;
    border-radius: 50%;
    overflow: hidden;
    border: 3px solid #2c7be5;
    flex-shrink: 0;
}

.avatar img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.about-text h3 {
    margin: 0;
    font-size: 22px;
    color: #2c7be5;
}

.about-text p {
    margin-top: 10px;
    font-size: 15px;
    line-height: 1.6;
    color: #444;
}
</style>

<div class="about-card">
<div class="avatar">
<img src="logo.png">
</div>

<div class="about-text">
<h3>About</h3>
<p>
Computer Science student at Cairo University,
             passionate about Data Engineering and building
             efficient data pipelines. Hands-on experience with Python, SQL, and data visualization tools
            , with a focus on transforming raw data into structured, reliable datasets.
             Aspiring Data Engineer aiming to contribute to innovative, data-driven solutions
</p>
</div>
</div>
""", unsafe_allow_html=True)
