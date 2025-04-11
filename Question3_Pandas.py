import streamlit as st
import pandas as pd
import altair as alt

# Chemin des fichiers CSV
athletes_path = "donnees_jeux_olympiques/athlete_events.csv"
nocs_path = "donnees_jeux_olympiques/noc_regions.csv"


st.set_page_config(page_title="Médailles JO", layout="wide")


# Chargement des données
@st.cache_data
def load_data():
    athlete_events = pd.read_csv(athletes_path)
    noc_regions = pd.read_csv(nocs_path)
    data = pd.merge(athlete_events, noc_regions, on="NOC", how="left")
    return data


data = load_data()

st.markdown(
    """
    <style>
        .main {background-color: #f8f9fa;}
        h1, h2, h3 {color: #003366;}
        .stDataFrame th, .stDataFrame td {text-align: left;}
    </style>
""",
    unsafe_allow_html=True,
)

st.title("\U0001f3c6 Tableau des médailles aux Jeux Olympiques")

# Choix des paramètres
all_countries = sorted(data["region"].dropna().unique())
country = st.selectbox("Choisissez un pays :", ["Tous"] + all_countries)
years = sorted(data["Year"].unique())
year = st.selectbox("Choisissez une année :", years)
season = st.radio(
    "Saison :",
    ["Summer", "Winter"],
    format_func=lambda x: "Été" if x == "Summer" else "Hiver",
)

# Filtrage principal
data_filtered = data[(data["Year"] == year) & (data["Season"] == season)]
if country != "Tous":
    data_filtered = data_filtered[data_filtered["region"] == country]

# Filtrage par discipline et événement
all_disciplines = sorted(data_filtered["Sport"].dropna().unique())
selected_discipline = st.selectbox(
    "Filtrer par discipline (facultatif) :", ["Toutes"] + all_disciplines
)

if selected_discipline != "Toutes":
    data_filtered = data_filtered[data_filtered["Sport"] == selected_discipline]

# Suppression des doublons pour les épreuves par équipe
medals = data_filtered.dropna(subset=["Medal"])
grouped_medals = medals.groupby(["Team", "NOC", "Year", "Season", "Event", "Medal"])
unique_medals = grouped_medals.agg(
    {"Name": lambda x: list(x.unique()), "Sport": "first", "region": "first"}
).reset_index()

# Comptage des médailles
medal_counts = (
    unique_medals.groupby("Medal")
    .size()
    .reindex(["Gold", "Silver", "Bronze"], fill_value=0)
)
medal_counts.index = medal_counts.index.map(
    {"Gold": "Or", "Silver": "Argent", "Bronze": "Bronze"}
)
medal_counts["Total"] = medal_counts.sum()

st.subheader("\U0001f4ca Tableau des médailles")
st.dataframe(
    medal_counts.reset_index().rename(columns={0: "Nombre", "index": "Médaille"})
)

# Graphique interactif
st.subheader("\U0001f4c8 Graphique des médailles")
chart_data = medal_counts.drop("Total").reset_index()
chart_data.columns = ["Médaille", "Nombre"]
chart = (
    alt.Chart(chart_data)
    .mark_bar()
    .encode(
        x=alt.X("Médaille", sort=["Or", "Argent", "Bronze"]),
        y="Nombre",
        color="Médaille",
    )
    .properties(width=500, height=300)
)
st.altair_chart(chart)

# Détail des médailles avec noms
st.subheader("\U0001f4cb Détail des événements")
for sport in sorted(unique_medals["Sport"].unique()):
    with st.expander(sport):
        details = unique_medals[unique_medals["Sport"] == sport][
            ["Event", "Medal", "Name"]
        ]
        details = details.rename(
            columns={"Event": "Événement", "Medal": "Médaille", "Name": "Athlètes"}
        )
        details["Médaille"] = details["Médaille"].map(
            {"Gold": "Or", "Silver": "Argent", "Bronze": "Bronze"}
        )
        details["Athlètes"] = details["Athlètes"].apply(lambda names: ", ".join(names))
        st.dataframe(details.reset_index(drop=True))
