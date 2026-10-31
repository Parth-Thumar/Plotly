# About Plotly
# -> Plotly is a Data Viz library by the company Plotly based out of Canada with support in languages such as Python, Js, Julia etc.

# Advantages
# - Multi language support
# - Lot's of graphs
# - Interactive plots
# - Beautiful plots

# - Does not work with live data streams. Dash can be explored for that.

# The Plotly Roadmap
# - Plotly Go
# - Plotly Express
# - Dash

# Working with plotyly
# import libraries
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# import datasets
tips = px.data.tips()
iris = px.data.iris()
gap = px.data.gapminder()

# scatter plot using plotly go
temp_df = gap[gap['year'] == 2007]

trace1 = go.Scatter(x=temp_df['lifeExp'], y=temp_df['gdpPercap'],mode='markers')
trace2 = go.Scatter(x=[0,1,2], y=[0,90,30000], mode='lines')
data = [trace1, trace2]

layout = go.Layout(title='Life Exp Vs GDP per Capital for 2007', xaxis={'title':'Life Exp'}, yaxis={'title':'GDP'})
fig = go.Figure(data, layout)

fig.show()

# plot life exp and gdp scatter plot -> continent as color -> pop as size -> hover name -> range_x/range_y -> log_x/log_y
fig = px.scatter(temp_df, x='lifeExp', y='gdpPercap', color='continent', size='pop', size_max=100, hover_name='country')
fig.show()

# plot animation of the above curve on the basic of year
fig = px.scatter(gap, x='lifeExp', y='gdpPercap',
                 color='continent', size='pop',
                 size_max=100, hover_name='country',
                 range_x=[30, 95],
                 animation_frame='year', animation_group='country')
fig.write_html('gapminder_animation.html', auto_open=True)


# line plot
# plot india pop line plot

temp_df = gap[gap['country'] == 'India']
fig = px.line(temp_df, x='year', y='pop', title='India population growth')
fig.show()

# plot india china pak line plot
temp_df = gap[gap['country'].isin(['India', 'China', 'Pakistan'])].pivot(index='year', columns='country', values='lifeExp')
fig = px.line(temp_df, x=temp_df.index, y=temp_df.columns)
fig.show()

# bar chart 
# india's pop over the years
temp_df = gap[gap['country'] == 'India']
fig = px.bar(temp_df, x='year', y='pop')
fig.show()

# pop comp of 3 countries
temp_df = gap[gap['country'].isin(['India', 'China', 'Pakistan'])].pivot(index='year', columns='country', values='pop')
# grouped bar chart -> text_auto
fig = px.bar(temp_df, x=temp_df.index, y=temp_df.columns, barmode='group', log_y=True, text_auto=True)
fig.show()

# stacked bar chart
# pop contribution per country to a continents pop stacked a perticy=ular year(2007)
temp_df = gap[gap['year'] == 2007]
fig = px.bar(temp_df, x='continent', y='pop', color='country', log_y=True)
fig.show()

# bar chart animation 
fig = px.bar(gap, x='continent', y='pop', color='continent', animation_frame='year', animation_group='country', range_y=[0, 4000000000])
fig.show()

# histogram
# plot histogram of life expt of all countries in 2007 -> nbins -> text_auto
temp_df = gap[gap['year'] == 2007]
fig = px.histogram(temp_df, x='lifeExp', nbins=30, text_auto=True)
fig.show()

# plot histogram of sepal length of all iris species
iris = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Backend\\Python\\Plotly\\iris.csv')
fig = px.histogram(iris, x='SepalLengthCm', color='Species', nbins=30, text_auto=True)
fig.show()

# pie -> values -> names
# find the pie chart of pop of european countries in 2007
temp_df = gap[(gap['year'] == 2007) & (gap['continent'] == 'Europe')]
fig = px.pie(temp_df, values='pop', names='country')
fig.show()

# plot pie chart of world pop in 1952 continent wise ->  -> explode(pull)
temp_df = gap[gap['year'] == 1952].groupby('continent')['pop'].sum().reset_index()
fig = px.pie(temp_df, values='pop', names='continent')
fig.show()

# Sunburst plot -> Sunburst plots visualize hierachical data spanning outwards radially from root to leaves. -> color
# path  ->  [], values
temp_df = gap[gap['year'] == 2007]
fig = px.sunburst(temp_df, path=['continent', 'country'], values='pop', color='lifeExp')
fig.show()

fig = px.sunburst(tips, path=['sex', 'smoker', 'day', 'time'], values='total_bill', color='size')
fig.show()

# Treemap
temp_df = gap[gap['year'] == 2007]
fig = px.treemap(temp_df, path=[px.Constant('World'), 'continent', 'country'], values='pop', color='lifeExp')
fig.show()

# Heatmap -> find heatmap of all comtinents with year on avg of life exp
temp_df = tips.pivot_table(index='day', columns='sex', values='total_bill', aggfunc='sum')
fig = px.imshow(temp_df)
fig.show()

temp_df = gap.pivot_table(index='year', columns='continent', values='lifeExp', aggfunc='mean')
fig = px.imshow(temp_df)
fig.show()

# 3d scatterplot
# plot a 3d scatter plot of all country data for 2007
temp_df = gap[gap['year'] == 2007]
fig = px.scatter_3d(temp_df, x='lifeExp', y='pop', z='gdpPercap', log_y=True, color='continent', hover_name='country')
fig.show()

fig = px.scatter_3d(iris, x='SepalLengthCm', y='SepalWidthCm', z='PetalLengthCm', color='Species')
fig.show()

# scatter_matrix -> dimansions
fig = px.scatter_matrix(iris, dimensions=['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'], color='Species')
fig.show()