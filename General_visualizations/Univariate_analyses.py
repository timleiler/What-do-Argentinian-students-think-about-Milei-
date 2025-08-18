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

numerical_vars = ['Edad (en números)', '3. En tu opinión, ¿hasta qué punto Milei es un buen político? (De 1 "muy malo" a 10 "muy bueno") ', '9. En tu opinión, ¿hasta qué punto es capaz Milei de resolver los problemas económicos de Argentina? (De 1 "Es absolutamente incapaz" a 10 "Es absolutamente capaz")', '11. En tu opinión, ¿hasta qué punto es capaz Milei de resolver los problemas de seguridad interior? (De 1 «Es absolutamente incapaz» a 10 «Es absolutamente capaz»)'
, '12. ¿ En tu opinión, ¿es Milei un político peligroso? (De 1 “No, en absoluto” a 10 “Sí, absolutamente”)', '13.  En tu opinión, ¿es Milei corrupto? (De 1 „No, en absoluto“ a 10 „Sí, absolutamente” )', '14. ¿Crees que Milei es una figura de autoridad fuerte? (De 1 „No, en absoluto“ a 10 „Sí, absolutamente”)', '16. ¿Cómo valoras los conocimientos económicos de Milei? (De 1 "Muy malos” a 10 “Muy buenos”)'
, '17. ¿ Cómo ves tus perspectivas personales a futuro? (De 1 "muy negativas" a 10 "muy positivas")', '5. ¿Qué opinas de las ideas libertarias de Milei?  (rechazo del socialismo y el intervencionismo, compromiso con la propiedad privada y la economía de mercado, voluntarismo y antiestatismo) (De 1 "muy negativas" a 10 "muy positivas")']

#Question 5 -> 0 means "No sé"

categorical_vars = ['Genero', 'Lugar de naciemiento provincia', 'Lugar de residencia provincia', 'Universidad', 'Facultad (UNC)', 'Faculdad (UNLP)', 'Faculdad (UBA)', '1. ¿A quién votaste en la primera vuelta de las elecciones presidenciales de 2023?', '2. ¿A quién votaste en la segunda vuelta de las elecciones presidenciales de 2023?', '4. Más allá de tu posición política, ¿te parece que Milei es una buena persona?',
                    '6.  En tu opinión, ¿era Milei la mejor opción en la primera vuelta de las elecciones presidenciales de 2023?', '7. En tu opinión, ¿Milei era la mejor opción en la segunda vuelta de las elecciones presidenciales?', '8. ¿ Qué opinas de la oratoria de Milei?','10. En tu opinion, ¿en qué medida Milei traerá más "libertad" a Argentina?,'
                    '15.  En tu opinión ¿sería mejor un gobierno peronista que el gobierno actual']


print(numerical_vars, type(numerical_vars))
print(categorical_vars, type(categorical_vars))
print()

print("Numerical Variables Summary:")
print(df[numerical_vars].describe())

print("\nCategorical Variables Summary:")
for var in categorical_vars:
    print(f"\n{var.upper()}:")
    print(df[var].value_counts(normalize=True).round(3))

