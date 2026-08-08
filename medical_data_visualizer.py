import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Import the data from medical_examination.csv
df = pd.read_csv('medical_examination.csv')

# 2. Add 'overweight' column
bmi = df['weight'] / ((df['height'] / 100) ** 2)
df['overweight'] = (bmi > 25).astype(int)

# 3. Normalize data by making 0 always good and 1 always bad
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4. Draw Categorical Plot
def draw_cat_plot():
    # 5. Create DataFrame for cat plot using pd.melt
    df_cat = pd.melt(
        df, 
        id_vars=['cardio'], 
        value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']
    )

    # 6. Group and reformat the data to show counts of each feature
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # 7. Create catplot using sns.catplot()
    catplot = sns.catplot(
        data=df_cat,
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        kind='bar'
    )

    # 8. Get the figure for the output
    fig = catplot.fig

    # 9. Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

# 10. Draw Heat Map
def draw_heat_map():
    # 11. Clean the data in df_heat
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12. Calculate the correlation matrix
    corr = df_heat.corr()

    # 13. Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14. Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 12))

    # 15. Plot correlation matrix
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.1f',
        linewidths=0.5,
        square=True,
        cbar_kws={'shrink': 0.5},
        ax=ax
    )

    # 16. Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig