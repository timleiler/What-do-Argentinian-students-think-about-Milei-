import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
from scipy import stats
import openpyxl

#Reading the file / Create the dataframe
df = pd.read_excel("Auswertung.xlsx")

print(df.head())



#Descriptive Statistic
print("------Descriptive Statistic-------")

numerical_vars = ['Edad', '3. Buen político', '5. Ideas libertarias', '9. Resolver los problemas económicos', '11. Resolver los problemas de seguridad interior',
'12. Milei un político peligroso', '13. Corrupción', '14. Figura de autoridad fuerte', '16. Conocimientos económicos', '17. Perspectivas personales a futuro']

#Question 5 -> 0 means "No sé"

categorical_vars = ['Género', 'Lugar de nacimiento provincia', 'Lugar de residencia provincia', 'Lugar de residencia (En formato: ciudad/provincia)', 'Universidad', 'Facultad (UNC)',
                    'Faculdad (UNLP)', 'Faculdad (UBA)', '1. Primera vuelta', '2. Segunda vuelta', '4. Buena persona', '6. La mejor opción primera vuelta',
                    '7. La mejor opción segunda vuelta', '8. Oratoria', '10. Traerá más "libertad" a Argentina', '15. Sería mejor un gobierno peronista']


print(numerical_vars, type(numerical_vars))
print(categorical_vars, type(categorical_vars))
print()

print("Numerical Variables Summary:")
print(df[numerical_vars].describe())

print("\nCategorical Variables Summary:")
for var in categorical_vars:
    print(f"\n{var.upper()}:")
    print(df[var].value_counts(normalize=True).round(3))

#plotting style
plt.style.use('default')
sns.set_palette("husl")
fig_size = (15, 12)
fig, axes = plt.subplots(3, 3, figsize=fig_size)
fig.suptitle('Univariate Analysis of Survey Data', fontsize=16, fontweight='bold')


#Plot 1: Age Distribution (Histogram with KDE)

axes[0, 0].hist(df['Edad'], bins=20, alpha=0.7, color='skyblue', edgecolor='black')

axes[0, 0].axvline(df['Edad'].mean(), color='red', linestyle='--', 
                   label=f'Mean: {df["Edad"].mean():.1f}')

axes[0, 0].axvline(df['Edad'].median(), color='green', linestyle='--', 
                   label=f'Median: {df["Edad"].median():.1f}')

axes[0, 0].set_xlabel('Age (years)')
axes[0, 0].set_ylabel('Frequency')
axes[0, 0].legend()


#Plot 2: 13. Corrupción  (boxplot)

box_plot = axes[0, 2].boxplot(df['13. Corrupción'], patch_artist=True)
box_plot['boxes'][0].set_facecolor('lightblue')

axes[0, 2].set_title('Do you thin Milei is corrupt? (From not very (1) to very corrupt (10))', fontweight='bold')
axes[0, 2].set_ylabel('Score (1-10)')
axes[0, 2].grid(True, alpha=0.3)


# Plot 3: Political Orientation (Pie Chart) (First election round)

political_counts = df['1. Primera vuelta'].value_counts()
colors = ['#ff9999', '#66b3ff', "#108f10", '#ffcc99', '#ff99cc', '#76048d', "#40fff5", "#FFFB04FF"]
wedges, texts, autotexts = axes[1, 0].pie(political_counts.values, 
                                          labels=political_counts.index,
                                          autopct='%1.1f%%',
                                          colors=colors,
                                          startangle=90)
axes[1, 0].set_title('Political Orientation Distribution - First election round', fontweight='bold')

# Plot 4: Political Orientation (Pie Chart) (Second election round)

political_counts = df['2. Segunda vuelta'].value_counts()
colors = ["#1430d1", "#ebfa17", "#108f10", '#ffcc99', '#ff99cc']
wedges, texts, autotexts = axes[1, 1].pie(political_counts.values, 
                                          labels=political_counts.index,
                                          autopct='%1.1f%%',
                                          colors=colors,
                                          startangle=90)
axes[1, 1].set_title('Political Orientation Distribution - Second election round', fontweight='bold')


plt.show()
