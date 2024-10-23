import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import base64

# Google Sheets public URL
sheet_url = "https://docs.google.com/spreadsheets/d/1pha0SHJoXGSRZ9bSuMPu4D4ISZiKtCc5EG0pJ8qLW7w/export?format=csv&gid=164371720"

# Fetching data from Google Sheets directly using pandas
data = pd.read_csv(sheet_url)

# Filter data based on required columns
columns = ["KEYWORD", "Belongs to", "Rank - 9th September", "Rank - 2nd September", "Rank - 26th Aug", "Rank - 14th Aug", "Rank - 13th Aug", "Rank - 12th Aug", "Rank - 5th Aug", "Rank - 22nd July"]
filtered_data = data[columns]

# Streamlit app layout
st.title("Keyword Rankings Dashboard")

selected_category = st.selectbox("Select a Category", options=filtered_data['Belongs to'].unique())
search_query = st.text_input("Search keywords...")
graph_type = st.selectbox("Select Graph Type", options=['Bar', 'Line', 'Scatter'])

data_to_use = filtered_data.copy()

if search_query:
    data_to_use = data_to_use[data_to_use['KEYWORD'].str.contains(search_query, case=False)]

if selected_category:
    data_to_use = data_to_use[data_to_use['Belongs to'] == selected_category]

st.markdown(f"### Rankings for {selected_category or 'All Categories'}")

fig = go.Figure()
dates = ["Rank - 9th September", "Rank - 2nd September", "Rank - 26th Aug", "Rank - 14th Aug", "Rank - 13th Aug", "Rank - 12th Aug", "Rank - 5th Aug", "Rank - 22nd July"]
colors = px.colors.sequential.Viridis

# Ensure that all dates are present in the data
for date in dates:
    if date not in data_to_use.columns:
        st.error(f"Date column '{date}' is missing from the data.")
        continue

# Add traces to the figure based on selected graph type
for i, date in enumerate(dates):
    if date in data_to_use.columns:
        if graph_type == 'Bar':
            fig.add_trace(go.Bar(
                x=data_to_use['KEYWORD'],
                y=data_to_use[date],
                name=date,
                marker=dict(color=colors[i], opacity=1),
                text=data_to_use[date],
                textposition='inside',
                textfont=dict(color='black')
            ))
        elif graph_type == 'Line':
            fig.add_trace(go.Scatter(
                x=data_to_use['KEYWORD'],
                y=data_to_use[date],
                mode='lines+markers',
                name=date,
                line=dict(color=colors[i]),
                text=data_to_use[date],
                textposition='top center'
            ))
        elif graph_type == 'Scatter':
            fig.add_trace(go.Scatter(
                x=data_to_use['KEYWORD'],
                y=data_to_use[date],
                mode='markers',
                name=date,
                marker=dict(color=colors[i]),
                text=data_to_use[date],
                textposition='top center'
            ))

fig.update_layout(
    barmode='stack' if graph_type == 'Bar' else 'overlay',
    yaxis=dict(title='Rank', titlefont=dict(color='black'), tickfont=dict(color='black')),
    xaxis=dict(title='', titlefont=dict(color='black'), tickfont=dict(color='black')),
    plot_bgcolor='white',
    paper_bgcolor='white',
    template='plotly_white',
    height=600,
    width=1000,
    title_font=dict(color='black'),
    legend=dict(font=dict(color='black'))
)

st.plotly_chart(fig)

# Detailed view dropdown
selected_keyword = st.selectbox("Select a Keyword for Detailed View", options=data_to_use['KEYWORD'].unique())

if selected_keyword:
    detailed_data = data_to_use[data_to_use['KEYWORD'] == selected_keyword]

    detailed_fig = go.Figure()

    for i, date in enumerate(dates):
        if date in detailed_data.columns:
            detailed_fig.add_trace(go.Bar(
                x=[date],
                y=detailed_data[date],
                name=date,
                marker=dict(color=colors[i])
            ))

    detailed_fig.update_layout(
        barmode='group',
        title=f'Detailed Rankings for {selected_keyword}',
        yaxis=dict(title='Rank', titlefont=dict(color='black'), tickfont=dict(color='black')),
        xaxis=dict(title='', titlefont=dict(color='black'), tickfont=dict(color='black')),
        plot_bgcolor='white',
        paper_bgcolor='white',
        template='plotly_white',
        height=400,
        width=600,
        title_font=dict(color='black'),
        legend=dict(font=dict(color='black'))
    )

    st.plotly_chart(detailed_fig)

# Export filtered data to CSV
if st.button("Export to CSV"):
    csv = data_to_use.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="filtered_data.csv">Download CSV</a>'
    st.markdown(href, unsafe_allow_html=True)
