import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc  # Import Bootstrap components
import pandas as pd
import plotly.express as px
import datetime

# Use an external stylesheet (you need to install dash-bootstrap-components)
external_stylesheets = [dbc.themes.BOOTSTRAP]

# Load in dataframes
# UK Data
deaths = pd.read_csv('Deaths.csv')
infections = pd.read_csv('Infections.csv')
vaccines = pd.read_csv('Vaccines.csv')
hospitalisations = pd.read_csv('Hospitalisations.csv')
# International Data
world_ind = pd.read_csv("world_indicator.csv")
world_loc = pd.read_csv("world_location.csv")
hdi_comp = pd.read_csv("hdi_comp.csv")

# Data Wrangling
hdi_comp['year'] = hdi_comp['year'].astype(str)

w_labels = {
    "week_start": "Week",
    "average_weekly_percent_population_vaccinated": "",
    "total_weekly_new_cases_per_ten_million": "",
    "total_weekly_new_deaths_per_million": "",
    "total_weekly_icu_patients_per_million": "",
    "total_weekly_new_vaccinatons_per_thousand": "",
    "average_new_cases_per_ten_million": "Average Daily New Cases per Ten Million",
    "average_icu_patients_per_million": "Average Daily Intensive Care Patients per Million",
    "average_new_deaths_per_million": "Average Daily Deaths per Million",
    "European Union": "",
    "France": "",
    "Germany": "",
    "New Zealand": "",
    "United Kingdom": "",
    "United States": "",
    "indicator": "Indicators"
}

w_order = {
    "indicator": ["New cases per ten million", "ICU patients per million", "Deaths per million"],
}

# Dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Define figures here
# UK Boxplots
uk_box1 = px.box(deaths, x="Nation", y="newDeaths", title="UK New Deaths Boxplot")
uk_box2 = px.box(infections, x="Nation", y="newCases", title="UK New Cases Boxplot")
uk_box3 = px.box(vaccines, x="Nation", y="newVaccines", title="UK New Vaccines Boxplot")
uk_box4 = px.box(hospitalisations, x="Nation", y="newAdmissions", title="UK New Admissions Boxplot")

# UK Line Charts
deaths['rollingNewDeathsPer100000'] = deaths['newDeathsper100000'].rolling(7).mean()
infections['rollingNewCasesPer100000'] = infections['newCasesper100000'].rolling(7).mean()
vaccines['rollingNewVaccinesPer100000'] = vaccines['newVacinesper100000'].rolling(7).mean()
hospitalisations['rollingNewAdmissionsPer100000'] = hospitalisations['newAdmissionsper100000'].rolling(7).mean()

# Deaths
deaths.date = pd.to_datetime(deaths['date'], format='%d/%m/%Y')
deaths_01 = px.line(
    deaths
    , x="date"
    , y="rollingNewDeathsPer100000"
    , color='Nation'
    , title="UK Deaths per 100,000"
    , template='plotly_white'
    , width=1000
    , height=500
    , color_discrete_sequence=px.colors.qualitative.Bold
)
deaths_01.add_vline(x=datetime.datetime(2020, 3, 23).timestamp() * 1000, line_color="black", line_dash="dash",
                    annotation_text="UK Lockdown", annotation_position="top")
deaths_01.add_vline(x=datetime.datetime(2020, 11, 5).timestamp() * 1000, line_color="purple", line_dash="dash",
                    line_width=1)
deaths_01.add_vline(x=datetime.datetime(2021, 1, 6).timestamp() * 1000, line_color="purple", line_dash="dash",
                    line_width=1)
deaths_01.add_vline(x=datetime.datetime(2020, 10, 23).timestamp() * 1000, line_color="goldenrod", line_dash="dash",
                    line_width=1)
deaths_01.add_vline(x=datetime.datetime(2020, 12, 28).timestamp() * 1000, line_color="goldenrod", line_dash="dash",
                    line_width=1)
deaths_01.add_vline(x=datetime.datetime(2020, 11, 27).timestamp() * 1000, line_color="green", line_dash="dash",
                    line_width=1)
deaths_01.add_vline(x=datetime.datetime(2020, 12, 26).timestamp() * 1000, line_color="green", line_dash="dash",
                    line_width=1)
deaths_01.add_vline(x=datetime.datetime(2021, 1, 6).timestamp() * 1000, line_color="blue", line_dash="dash",
                    line_width=1)
deaths_01.add_vline(x=datetime.datetime(2020, 12, 8).timestamp() * 1000, annotation_text="First Vaccine",
                    annotation_position="top")
# Deaths Total
deaths.date = pd.to_datetime(deaths['date'], format='%d/%m/%Y')
deaths_total = px.line(
    deaths
    ,x="date"
    ,y="newDeaths"
    ,color='Nation'
    ,title="UK reported Deaths"
    ,template='plotly_white'
    ,width=1000
    ,height=500
    ,color_discrete_sequence=px.colors.qualitative.Bold)

# Infections
infections.date = pd.to_datetime(infections['date'], format='%d/%m/%Y')
infections_01 = px.line(
    infections
    , x="date"
    , y="rollingNewCasesPer100000"
    , color='Nation'
    , title="UK infections per 100,000"
    , template='plotly_white'
    , width=1000
    , height=500
    , color_discrete_sequence=px.colors.qualitative.Bold
)
infections_01.add_vline(x=datetime.datetime(2020, 3, 23).timestamp() * 1000, line_color="black", line_dash="dash",
                        annotation_text="UK Lockdown", annotation_position="top")
infections_01.add_vline(x=datetime.datetime(2020, 11, 5).timestamp() * 1000, line_color="purple", line_dash="dash",
                        line_width=1)
infections_01.add_vline(x=datetime.datetime(2021, 1, 6).timestamp() * 1000, line_color="purple", line_dash="dash",
                        line_width=1)
infections_01.add_vline(x=datetime.datetime(2020, 10, 23).timestamp() * 1000, line_color="goldenrod", line_dash="dash",
                        line_width=1)
infections_01.add_vline(x=datetime.datetime(2020, 12, 28).timestamp() * 1000, line_color="goldenrod", line_dash="dash",
                        line_width=1)
infections_01.add_vline(x=datetime.datetime(2020, 11, 27).timestamp() * 1000, line_color="green", line_dash="dash",
                        line_width=1)
infections_01.add_vline(x=datetime.datetime(2020, 12, 26).timestamp() * 1000, line_color="green", line_dash="dash",
                        line_width=1)
infections_01.add_vline(x=datetime.datetime(2021, 1, 6).timestamp() * 1000, line_color="blue", line_dash="dash",
                        line_width=1)
infections_01.add_vline(x=datetime.datetime(2020, 12, 8).timestamp() * 1000, annotation_text="First Vaccine",
                        annotation_position="top")

# Vaccinations
vaccines.date = pd.to_datetime(vaccines['date'], format='%d/%m/%Y')
vaccines_01 = px.line(
    vaccines
    , x="date"
    , y="rollingNewVaccinesPer100000"
    , color='Nation'
    , title="UK Vaccines per 100,000"
    , template='plotly_white'
    , width=1000
    , height=500
    , color_discrete_sequence=px.colors.qualitative.Bold
)

# Hospitalisations
hospitalisations.date = pd.to_datetime(hospitalisations['date'], format='%d/%m/%Y')
hospitalisations_01 = px.line(
    hospitalisations
    , x="date"
    , y="rollingNewAdmissionsPer100000"
    , color='Nation'
    , title="UK hospitalisations per 100,000"
    , template='plotly_white'
    , width=1000
    , height=500
    , color_discrete_sequence=px.colors.qualitative.Bold

)
hospitalisations_01.add_vline(x=datetime.datetime(2020, 3, 23).timestamp() * 1000, line_color="black", line_dash="dash",
                              annotation_text="UK Lockdown", annotation_position="top")
hospitalisations_01.add_vline(x=datetime.datetime(2020, 11, 5).timestamp() * 1000, line_color="purple",
                              line_dash="dash", line_width=1)
hospitalisations_01.add_vline(x=datetime.datetime(2021, 1, 6).timestamp() * 1000, line_color="purple", line_dash="dash",
                              line_width=1)
hospitalisations_01.add_vline(x=datetime.datetime(2020, 10, 23).timestamp() * 1000, line_color="goldenrod",
                              line_dash="dash", line_width=1)
hospitalisations_01.add_vline(x=datetime.datetime(2020, 12, 28).timestamp() * 1000, line_color="goldenrod",
                              line_dash="dash", line_width=1)
hospitalisations_01.add_vline(x=datetime.datetime(2020, 11, 27).timestamp() * 1000, line_color="green",
                              line_dash="dash", line_width=1)
hospitalisations_01.add_vline(x=datetime.datetime(2020, 12, 26).timestamp() * 1000, line_color="green",
                              line_dash="dash", line_width=1)
hospitalisations_01.add_vline(x=datetime.datetime(2021, 1, 6).timestamp() * 1000, line_color="blue", line_dash="dash",
                              line_width=1)
hospitalisations_01.add_vline(x=datetime.datetime(2020, 12, 8).timestamp() * 1000, annotation_text="First Vaccine",
                              annotation_position="top")


# International Figures
w_01 = px.line(
    world_ind
    , x="week_start"
    , y="average_weekly_percent_population_vaccinated"
    , color='location'
    , title="Percent of Population Fully Vaccinated (2 Doses)"
    , labels=w_labels
    , template='plotly_white'
)
w_01.update_xaxes(
    range=[datetime.datetime(2020, 11, 30).timestamp() * 1000, datetime.datetime(2021, 12, 13).timestamp() * 1000])
w_01.add_vline(x=datetime.datetime(2020, 8, 12).timestamp() * 1000, annotation_text="First Vaccine Globally",
               annotation_position="top right")

w_02 = px.line(
    world_ind
    , x="week_start"
    , y="total_weekly_new_cases_per_ten_million"
    , color='location'
    , title="Weekly New Cases per Ten Million"
    , labels=w_labels
    , template='plotly_white'
)
# w_02.update_xaxes(range=[9,125])
# w_02.add_vline(x=49, annotation_text="First Vaccine Globally", annotation_position="top left")
w_02.update_xaxes(
    range=[datetime.datetime(2020, 3, 2).timestamp() * 1000, datetime.datetime(2021, 12, 13).timestamp() * 1000])
w_02.add_vline(x=datetime.datetime(2020, 8, 12).timestamp() * 1000, annotation_text="First Vaccine Globally",
               annotation_position="top right")

w_03 = px.line(
    world_ind
    , x="week_start"
    , y="total_weekly_icu_patients_per_million"
    , color='location'
    , title="Weekly Intensive Care Unit (ICU) Admissions per Million"
    , labels=w_labels
    , template='plotly_white'
)
# w_03.update_xaxes(range=[9,125])
# w_03.add_vline(x=49, annotation_text="First Vaccine Globally", annotation_position="top left")
w_03.update_xaxes(
    range=[datetime.datetime(2020, 3, 2).timestamp() * 1000, datetime.datetime(2021, 12, 13).timestamp() * 1000])
w_03.add_vline(x=datetime.datetime(2020, 8, 12).timestamp() * 1000, annotation_text="First Vaccine Globally",
               annotation_position="top right")

w_04 = px.line(
    world_ind
    , x="week_start"
    , y="total_weekly_new_deaths_per_million"
    , color='location'
    , title="Weekly Deaths per Million"
    , labels=w_labels
    , template='plotly_white'
)
# w_04.update_xaxes(range=[9,125])
# w_04.add_vline(x=49, annotation_text="First Vaccine Globally", annotation_position="top left")
w_04.update_xaxes(
    range=[datetime.datetime(2020, 3, 2).timestamp() * 1000, datetime.datetime(2021, 12, 13).timestamp() * 1000])
w_04.add_vline(x=datetime.datetime(2020, 8, 12).timestamp() * 1000, annotation_text="First Vaccine Globally",
               annotation_position="top right")

w_05 = px.line(
    world_ind
    , x="week_start"
    , y="total_weekly_new_vaccinatons_per_thousand"
    , color='location'
    , title="Weekly Vaccinations per Thousand"
    , labels=w_labels
    , template='plotly_white'
)
# w_05.update_xaxes(range=[9,125])
# w_05.add_vline(x=49, annotation_text="First Vaccine Globally", annotation_position="top left")
w_05.update_xaxes(
    range=[datetime.datetime(2020, 3, 2).timestamp() * 1000, datetime.datetime(2021, 12, 13).timestamp() * 1000])
w_05.add_vline(x=datetime.datetime(2020, 8, 12).timestamp() * 1000, annotation_text="First Vaccine Globally",
               annotation_position="top right")

w_06 = px.line(
    world_loc
    , x="week_start"
    , y="United Kingdom"
    , color='indicator'
    , title="Comparison of Indicators - United Kingdom"
    , color_discrete_sequence=['#ff99cc', '#cc3366', '#990033']
    , labels=w_labels
    , category_orders=w_order
    , template='plotly_white'
)
w_06.update_yaxes(range=[0, 800])
w_06.add_vline(x=datetime.datetime(2020, 3, 23).timestamp() * 1000, annotation_text="Lockdowns",
               annotation_position="top left", annotation_font_color="orange", line_color="orange")
w_06.add_vline(x=datetime.datetime(2020, 11, 5).timestamp() * 1000,
               line_color="orange")  # NOTE lockdowns 2 and 3 are England, not UK
w_06.add_vline(x=datetime.datetime(2021, 1, 6).timestamp() * 1000, line_color="orange")
w_06.add_vline(x=datetime.datetime(2020, 12, 8).timestamp() * 1000, annotation_text="First Vaccine",
               annotation_position="top")

w_07 = px.line(
    world_loc
    , x="week_start"
    , y="Germany"
    , color='indicator'
    , title="Comparison of indicators - Germany"
    , color_discrete_sequence=['#ff99cc', '#cc3366', '#990033']
    , labels=w_labels
    , category_orders={
        "indicator": ["New cases per ten million", "ICU patients per million", "Deaths per million"],
    }
    , template='plotly_white'
)
w_07.update_yaxes(range=[0, 800])
w_07.add_vline(x=datetime.datetime(2020, 3, 22).timestamp() * 1000, annotation_text="Partial Lockdowns",
               annotation_position="top left", annotation_font_color="blue", line_color="blue")
w_07.add_vline(x=datetime.datetime(2020, 12, 16).timestamp() * 1000, annotation_text="Lockdown",
               annotation_position="top left", annotation_font_color="orange", line_color="orange")
w_07.add_vline(x=datetime.datetime(2020, 10, 2).timestamp() * 1000, line_color="blue")
w_07.add_vline(x=datetime.datetime(2021, 3, 7).timestamp() * 1000, line_color="blue")
w_07.add_vline(x=datetime.datetime(2021, 1, 11).timestamp() * 1000, annotation_text="First Vaccine",
               annotation_position="top")

w_09 = px.line(
    world_loc
    , x="week_start"
    , y="United States"
    , color='indicator'
    , title="Comparison of indicators - United States of America"
    , color_discrete_sequence=['#ff99cc', '#cc3366', '#990033']
    , labels=w_labels
    , category_orders=w_order
    , template='plotly_white'
)
w_09.update_yaxes(range=[0, 800])
w_09.add_vline(x=datetime.datetime(2020, 12, 14).timestamp() * 1000, annotation_text="First Vaccine",
               annotation_position="top")

w_10 = px.scatter(
    hdi_comp
    , x="average_new_deaths_per_million"
    , y="average_new_cases_per_ten_million"
    , color='year'
    , symbol='uk_other'
    , title="Did the UKs Approach Make a Difference?"
    , color_discrete_sequence=['#ff3399', '#9933ff']
    , labels=w_labels
    , category_orders=w_order
    , symbol_sequence=['circle', 'star']
    , template='plotly_white'
    , size='marker_size'
    , size_max=10
)

w_11 = px.scatter(
    hdi_comp
    , x="average_icu_patients_per_million"
    , y="average_new_cases_per_ten_million"
    , color='year'
    , symbol='uk_other'
    , title=""
    , color_discrete_sequence=['#ff3399', '#9933ff']
    , labels=w_labels
    , category_orders=w_order
    , symbol_sequence=['circle', 'star']
    , template='plotly_white'
    , size='marker_size'
    , size_max=10
)

# App Layout
app.title = 'COVID-19 Dashboard'

app.layout = dbc.Container([
    dbc.NavbarSimple(
        brand="COVID-19 Dashboard",
        brand_href="#",
        color='danger',
        dark=True
    ),
    html.Div([
        dcc.Tabs([
            dcc.Tab(label='Introduction', children=[
                dcc.Markdown("""
                
                                ## Introduction
                
                                In this analysis, we explore the experiences of several nations during the COVID-19 
                                pandemic, including countries within the United Kingdom (UK), Germany, France, 
                                New Zealand (NZ), and the United States of America (USA).
                                
                                The COVID-19 pandemic has had an unprecedented impact on societies around the world. 
                                Governments and health authorities implemented a wide range of strategies and 
                                measures to combat the virus, including vaccination campaigns, lockdowns, and public 
                                health guidelines. Understanding the effectiveness of these strategies and their impact 
                                on key metrics like hospital admissions and mortality rates is vital for informed 
                                decision-making.
                                
                                ## Key Questions We Explore
                                In this dashboard, we aim to address two fundamental questions:
                                ### 1. How Successful Was the UK's Vaccination Strategy?
                                We delve into the UK's vaccination strategy to assess its effectiveness in preventing 
                                hospital admissions and deaths compared to other developed nations. By analysing 
                                vaccination coverage, hospitalisation rates, and mortality data, we aim to provide 
                                valuable insights into the impact of vaccination efforts.
                                
                                ### 2. Regional Variations Within the UK and International Comparisons
                                We explore regional variations within the UK to identify areas that may have 
                                underperformed or excelled compared to others. Additionally, we extend our analysis to 
                                international comparisons, focusing on Germany, France, New Zealand, and the United 
                                States. These comparisons allow us to gain a broader perspective on the global response 
                                to the pandemic.

                                """)
            ]),
            dcc.Tab(label='UK Analysis', children=[
                dcc.Tabs(id="emile-subtabs", value="emile-subtab1", children=[
                    dcc.Tab(label='Overview', value="emile-subtab1", children=[
                        dcc.Graph(id='boxplot1', figure=uk_box1),
                        dcc.Graph(id='boxplot2', figure=uk_box2),
                        dcc.Graph(id='boxplot3', figure=uk_box3),
                        dcc.Graph(id='boxplot4', figure=uk_box4),
                        dcc.Graph(id='deaths-total', figure=deaths_total)
                    ]),
                    dcc.Tab(label='Deaths', value="emile-subtab2", children=[
                        dcc.Graph(id='uk-deaths', figure=deaths_01)
                    ]),
                    dcc.Tab(label='Infections', value="uk-subtab3", children=[
                        dcc.Graph(id='uk-infections', figure=infections_01)
                    ]),
                    dcc.Tab(label='Vaccinations', value="uk-subtab4", children=[
                        dcc.Graph(id='uk-vaccine', figure=vaccines_01)
                    ]),
                    dcc.Tab(label='Hospital Admissions', value="uk-subtab5", children=[
                        dcc.Graph(id='uk-hospital', figure=hospitalisations_01)
                    ])
                ])
            ]),
            dcc.Tab(label='International Analysis', children=[
                dcc.Tabs(id="int-subtabs", value="int-subtab0", children=[
                    dcc.Tab(label='Race to 70%', value="int-subtab1", children=[
                        dcc.Markdown("""
                        
                        **"We think it needs at least 60 to 70% of the population to have immunity to really break the 
                        chain of transmission."** - Dr Soumya Swaminathan, *WHO Chief Scientist*, 28 August 2020
                        """),
                        dcc.Graph(id='w-01', figure=w_01)
                    ]),
                    dcc.Tab(label='Impact of Vaccination', value="int-subtab2", children=[
                        dcc.Graph(id='w-02', figure=w_02),
                        dcc.Graph(id='w-03', figure=w_03),
                        dcc.Graph(id='w-04', figure=w_04),
                        dcc.Graph(id='w-05', figure=w_05)
                    ]),
                    dcc.Tab(label='Impact of Vaccination Pt.2', value="int-subtab3", children=[
                        dcc.Graph(id='w-09', figure=w_09),
                        dcc.Graph(id='w-07', figure=w_07),
                        dcc.Graph(id='w-06', figure=w_06),
                    ]),
                    dcc.Tab(label='UK Approach Impact', value="int-subtab4", children=[
                        dcc.Graph(id='w-10', figure=w_10),
                        dcc.Graph(id='w-11', figure=w_11)
                    ])
                ])

            ]),

            dcc.Tab(label='Challenges', children=[
                dcc.Markdown("""
                                ### General Considerations
                                **1. Lockdown Definitions:** Different countries had slightly different definitions of 
                                lockdowns, making it challenging to compare them directly.
                                
                                **2. Lockdown Duration:** It's difficult to pinpoint the exact start and end dates of 
                                lockdowns because restrictions were often phased out gradually, and many measures were 
                                introduced or lifted on the same date.
                                
                                **3. Regional Variations:** In the case of the US and EU data, it's important to 
                                acknowledge that these regions encompassed various states or countries, each implementing 
                                its own unique strategies and measures.
                                
                                **4. Correlation vs Causation:** Highlight that correlation does not imply causation, 
                                meaning it's challenging to conclusively state that a specific restriction directly 
                                caused fewer deaths.
                                
                                **5. Small Adjustments:** Besides major events like lockdowns, countries made numerous 
                                small adjustments throughout the pandemic (e.g., changing guidance, self-isolation times,
                                mask requirements, and business closures), which could have had significant impacts.
                                However, it's impractical to track every move every country made.
                                  
                                **6. Compliance Variability:** The rules imposed by governments do not necessarily 
                                reflect what people actually did. Some regions, like Paris, experienced issues with 
                                rule-breaking, so assumptions should not be made about universal compliance.
                                
                               ### Challenges in Data Collection
                               
                               **1. Data Sources:** There are multiple data sources for different metrics, and 
                               countries have different data collection approaches. Metrics may not always be directly 
                               comparable, and some metrics might be incomplete or differently defined.
                               
                               **2. Vaccination Strategies:**  Different countries had varying vaccination rollout 
                               strategies, which might not be fully discernible from quantitative data. For instance, 
                               some countries prioritised specific groups, while others adopted a more generalised approach.
                               
                               **3. Incomplete Data:** Some nations stopped recording certain figures earlier than 
                               others, leading to incomplete datasets.
                               
                               **4. Early Reporting:** Early reporting was less reliable due to limited testing, 
                               affecting the accuracy of COVID data.
                               
                               **5. Data Smoothing:** Daily data variations can make charts unreadable, so converting 
                               to rolling averages was used to provide a clearer representation.
                               
                               **6. Lag in Reporting:** Metrics such as reported deaths or cases take time to be 
                               registered, leading to a lag in reporting of approximately 11 days, which should be 
                               considered when analysing trends.

                                """)
            ]),

            dcc.Tab(label='Conclusion', children=[
                dcc.Tabs(id="conclusion", value="conclusion", children=[
                    dcc.Tab(label='Conclusion', value="conclusion1", children=[
                        dcc.Markdown("""
                        ### Varied Responses to a Global Crisis
                        The global response to the COVID-19 pandemic has been characterised by diversity. Each country 
                        adopted its unique strategies and measures, reflecting the complexity of this unprecedented 
                        health crisis. We acknowledge that no nation had a foolproof playbook for addressing the 
                        multifaceted challenges posed by the virus.
                        
                        ### The UK's Response Trajectory
                        
                        Our analysis suggests that the UK's initial response was marked by challenges and uncertainties.
                        While stay-at-home orders were issued broadly, comparing the endpoints of lockdowns remains 
                        complex due to the phased and gradual easing of restrictions in most instances.
                        
                        #### The Impact of Vaccination
                        
                        However, it is undeniable that the UK's vaccination program emerged as a significant milestone 
                        in the fight against COVID-19. Despite early hurdles, the vaccination rollout achieved 
                        considerable success. This success played a role in reducing hospital admissions and 
                        mortality rates.
                        
                        #### A Cautious Correlation
                        
                        It is important to emphasise that correlation does not imply causation. Our data analysis does 
                        not enable us to definitively assert that specific restrictions directly caused reductions in 
                        deaths. The relationship between public health measures and outcomes is multifaceted and 
                        influenced by various factors.
                        
                        """)
                    ]),

                    # how did the uk compare?

                    dcc.Tab(label='Data Sources', value="conclusion-ref", children=[
                        dcc.Markdown("""
                        ### UK Analysis
                        
                        [UK Population Figures](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/articles/overviewoftheukpopulation/january2021)
                        
                        [UK COVID Data](https://coronavirus.data.gov.uk/)
                        
                        ### International Analysis
                        
                        [World COVID Data](https://ourworldindata.org/explorers/coronavirus-data-explorer)                        
                        [World HDI](https://worldpopulationreview.com/country-rankings/hdi-by-country)
                        [WHO Quote](https://www.who.int/emergencies/diseases/novel-coronavirus-2019/media-resources/science-in-5/episode-1)
                        
                        ### COVID-19 Timeline Info
                        #### UK Timeline
                        
                        [Coronavirus Timeline](https://shorthand.radionz.co.nz/coronavirus-timeline/)
                       
                        [Commons Research Briefings](https://commonslibrary.parliament.uk/research-briefings/cbp-9068/)
                       
                        [Dec 2021 Lockdown Timeline](https://www.instituteforgovernment.org.uk/sites/default/files/2022-12/timeline-coronavirus-lockdown-december-2021.pdf)
                       
                        [First Vaccination](https://www.bbc.co.uk/news/uk-55227325)
                       
                        [Welsh Response](https://research.senedd.wales/research-articles/coronavirus-timeline-the-response-in-wales/)
                       
                        [Scotland Timeline](https://spice-spotlight.scot/2023/05/10/timeline-of-coronavirus-covid-19-in-scotland/)
                       
                        [Scotland COVID Data](https://data.gov.scot/coronavirus-covid-19/)
                       
                        [N. Ireland Timeline](//www.bbc.co.uk/news/uk-northern-ireland-55303928)
                        
                        #### Germany Timeline
                        [Germany Lockdown](https://www.politico.eu/article/germany-imposes-coronavirus-lockdown-for-the-unvaccinated/)
                        
                        [German Response](https://www.exemplars.health/emerging-topics/epidemic-preparedness-and-response/covid-19/germany#:~:text=Germany's%20prevention%20protocols%20facilitated%20the,use%20of%20ample%20hospital%20capacity.)
                        
                        [German Timeline](https://www.dw.com/en/covid-how-germany-battles-the-pandemic-a-chronology/a-58026877)
                        
                        [Berlin](https://apnews.com/article/coronavirus-pandemic-health-europe-epidemics-berlin-b61de99739774c1f52b4ba6860054d6d)
                        
                        #### France Timeline
                        [Paris Lockdown](https://medicalxpress.com/news/2020-11-paris-tightens-virus-lockdown.html)
                        
                        [France Lockdown](https://www.france24.com/en/france/20210317-in-pictures-a-look-back-one-year-after-france-went-into-lockdown)
                        
                        [Paris Restrictions](https://medicalxpress.com/news/2020-11-paris-tightens-virus-lockdown.html)
                        
                        [France Vaccinations](https://www.france24.com/en/live-news/20201227-france-begins-covid-19-vaccinations-as-78-year-old-woman-receives-country-s-first-dose)
                        
                        #### New Zealand
                        
                        [NZ Lockdown](https://www.health.govt.nz/news-media/media-releases/covid-19-update-21-march)
                        
                        [Auckland Restrictions](https://www.nzherald.co.nz/nz/covid-19-coronavirus-auckland-in-lockdown-rest-of-country-in-level-2-four-cases-of-community-transmission/IIQ7CJFGRRABYS5T6WNEGF7S74/?c_id=1&objectid=12355759)
                        
                        [NZ Vaccinations](https://www.health.govt.nz/about-ministry/information-releases/general-information-releases/super-saturday-and-vaxathon-information)
                        
                        #### US Timeline
                        [US Timeline](https://www.supremecourt.gov/opinions/urls_cited/ot2021/21a90/21a90-1.pdf)


                        """)
                    ])
                ]),
            ])
        ])
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
