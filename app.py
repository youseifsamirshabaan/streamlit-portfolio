import streamlit as st
import base64
import textwrap

#El 3enwan
st.set_page_config(page_title="Youseif Hegazy | Data Engineer", layout="wide")

#Tahweel El Sora
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return f"data:image/png;base64,{base64.b64encode(data).decode()}"
    except:
        return "https://via.placeholder.com/150"

img_html = get_base64_of_bin_file("logo.png")

#EL css
style = """
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<style>
.stApp { background-color: #0e1117; }
.cv-wrapper { max-width: 1200px; margin: auto; background: #1d2129; border-radius: 20px; border: 1px solid #2d323b; display: flex; flex-wrap: wrap; color: white; overflow: hidden; }
.side-bar { flex: 1; background: #161b22; padding: 40px 20px; text-align: center; border-right: 1px solid #2d323b; min-width: 300px; }
.main-body { flex: 2.5; padding: 40px; min-width: 500px; }
.profile-img { width: 180px; height: 180px; border-radius: 50%; border: 4px solid #4facfe; object-fit: cover; margin-bottom: 20px; }
.name-title { color: #4facfe; font-size: 32px; margin: 0; font-weight: bold; }
.sub-title { color: #90a4ae; font-size: 18px; margin-bottom: 30px; }
.contact-row { display: flex; align-items: center; gap: 15px; color: #cfd8dc; font-size: 14px; margin-bottom: 15px; text-decoration: none !important; justify-content: flex-start; padding-left: 20px; }
.contact-row i { color: #4facfe; width: 20px; font-size: 18px; }
.btn-cv { display: block; background: #4facfe; color: white !important; padding: 12px; border-radius: 8px; text-decoration: none !important; font-weight: bold; margin-top: 30px; }
.section-h { color: #4facfe; font-size: 20px; font-weight: bold; text-transform: uppercase; border-bottom: 2px solid #4facfe; display: inline-block; margin-bottom: 20px; padding-bottom: 5px; }
.exp-box { margin-bottom: 30px; }
.exp-head { display: flex; justify-content: space-between; font-weight: bold; font-size: 16px; }
.exp-sub { color: #4facfe; font-size: 14px; margin: 5px 0; font-style: italic; }
.tag-s { display: inline-block; background: rgba(79, 172, 254, 0.1); color: #4facfe; padding: 5px 12px; border-radius: 5px; font-size: 12px; margin: 4px; border: 1px solid #4facfe; }
ul { color: #cfd8dc; font-size: 14px; line-height: 1.7; }
b { color: #4facfe; }
a { color: inherit !important; text-decoration: none !important; }
</style>
"""

#El html
html = f"""
<div class="cv-wrapper">
<div class="side-bar">
<img src="{img_html}" class="profile-img">
<h1 class="name-title">Youseif Hegazy</h1>
<p class="sub-title">Data Engineer</p>
<div class="contact-row"><i class="fas fa-location-dot"></i><span>Giza, Egypt</span></div>
<div class="contact-row"><i class="fas fa-phone"></i><span>+20 115 651 7785</span></div>
<div class="contact-row"><i class="fas fa-envelope"></i><span>youseifhegazy99@gmail.com</span></div>
<a href="https://linkedin.com/in/youseif-hegazy-8ab15537a" class="contact-row" target="_blank"><i class="fab fa-linkedin"></i><span>LinkedIn Profile</span></a>
<a href="https://drive.google.com/file/d/1E3zT9FfGt1U0W5upT2g5sDCoFM8WNpPb/view?usp=drive_link" class="btn-cv">DOWNLOAD CV</a>
<div style="text-align: left; margin-top: 40px; padding-left: 10px;">
<h3 class="section-h" style="font-size: 16px;">Technical Stack</h3><br>
<b>Big Data:</b><br>
<span class="tag-s">Spark</span><span class="tag-s">Hadoop</span><span class="tag-s">Kafka</span><span class="tag-s">Airflow</span><span class="tag-s">Hive</span><span class="tag-s">HBase</span><span class="tag-s">Flume</span><span class="tag-s">Flink</span><br>
<b>Development:</b><br>
<span class="tag-s">Python</span><span class="tag-s">SQL</span><span class="tag-s">Flask</span><span class="tag-s">Streamlit</span><span class="tag-s">ETL</span><span class="tag-s">Git</span><span class="tag-s">GitHub</span><span class="tag-s">html</span><span class="tag-s">css</span><span class="tag-s">JavaScript</span>
</div>
</div>
<div class="main-body">
<div class="exp-box">
<h3 class="section-h">Professional Summary</h3>
<p style="color:#cfd8dc; font-size: 15px;">I'm a Computer Science student at Cairo University, passionate about Data Engineering and building efficient data pipelines. Hands-on experience with Python, SQL, and data visualization tools, with a focus on transforming raw data into structured, reliable datasets. Aspiring Data Engineer aiming to contribute to innovative, data-driven solutions</p>
</div>
<div class="exp-box">
<h3 class="section-h">Experience</h3>
<div class="exp-box">
<div class="exp-head"><span>DEPI – Big Data & AI Track</span><span>2025 – Present</span></div>
<div class="exp-sub">Trainee / Aspiring Data Engineer</div>
<ul>
<li>Implementing distributed data processing with <b>Apache Spark</b>.</li>
<li>Orchestrating data workflows and pipelines using <b>Airflow</b>.</li>
<li>Managing Big Data ingestion and storage via <b>Kafka, Flume and HDFS</b>.</li>
</ul>
</div>
<div class="exp-box">
<div class="exp-head"><span>Microsoft Power BI & Excel</span><span>2025</span></div>
<div class="exp-sub">Data Analyst Trainee</div>
<ul>
<li>Built interactive dashboards for real-world datasets.</li>
<li>Advanced data cleaning and reporting for engineering insights.</li>
</ul>
</div>
</div>
<div class="exp-box">
<h3 class="section-h">Projects</h3>
<p><b>Web Scraping & APIs:</b> Built scripts via <b>Selenium/BS4</b> & served data through <b>Flask</b>.</p>
<p><b>Data Apps:</b> Developed <b>Streamlit</b> apps for pipeline monitoring and data viz.</p>
<p><b>ETL Pipelines:</b> End-to-end automation of data cleaning and transformation.</p><p>Practiced data transformation, cleaning, and automation to support data engineering tasks.</p>
</div>
<div class="exp-box" style="display: flex; gap: 40px;">
<div style="flex:1;">
<h3 class="section-h">Education</h3>
<p><b>Cairo University</b><br><span style="color:#90a4ae; font-size:13px;">B.Sc. Computer Science (2027)</span></p>
</div>
<div style="flex:1;">
<h3 class="section-h">Certifications</h3>
<ul style="font-size:12px;">
<li>ITI (MaharaTech) Database Fundamental</li>
<li>Microsoft Data Analyst</li>
<li>Advanced Excel Certificate</li>
</ul>
</div>
</div>
</div>
</div>
"""

#Taked El html , css
st.markdown(style, unsafe_allow_html=True)
st.markdown(textwrap.dedent(html), unsafe_allow_html=True)