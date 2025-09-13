import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
from scipy import stats
from scipy.stats import chi2_contingency, pearsonr, spearmanr, kendalltau

import warnings
warnings.filterwarnings('ignore')



df = pd.read_excel("Auswertung.xlsx")

print(df.head())


numerical_vars = ['Edad', '3. Buen político', '5. Ideas libertarias', '9. Resolver los problemas económicos', '11. Resolver los problemas de seguridad interior',
'12. Milei un político peligroso', '13. Corrupción', '14. Figura de autoridad fuerte', '16. Conocimientos económicos', '17. Perspectivas personales a futuro']

#Question 5 -> 0 means "No sé"

categorical_vars = ['Género', 'Lugar de nacimiento provincia', 'Lugar de residencia provincia', 'Lugar de residencia (En formato: ciudad/provincia)', 'Universidad', 'Facultad (UNC)',
                    'Faculdad (UNLP)', 'Faculdad (UBA)', '1. Primera vuelta', '2. Segunda vuelta', '4. Buena persona', '6. La mejor opción primera vuelta',
                    '7. La mejor opción segunda vuelta', '8. Oratoria', '10. Traerá más "libertad" a Argentina', '15. Sería mejor un gobierno peronista']


# Bivariate Analyse


