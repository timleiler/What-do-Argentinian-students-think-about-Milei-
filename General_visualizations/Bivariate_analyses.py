import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
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

plt.ion()

df = pd.read_excel("Auswertung.xlsx")


numerical_vars = ['Edad', '3. Buen político', '5. Ideas libertarias', '9. Resolver los problemas económicos', '11. Resolver los problemas de seguridad interior',
'12. Milei un político peligroso', '13. Corrupción', '14. Figura de autoridad fuerte', '16. Conocimientos económicos', '17. Perspectivas personales a futuro']

#Question 5 -> 0 means "No sé"

categorical_vars = ['Género', 'Lugar de nacimiento provincia', 'Lugar de residencia provincia', 'Lugar de residencia (En formato: ciudad/provincia)', 'Universidad', 'Facultad (UNC)',
                    'Faculdad (UNLP)', 'Faculdad (UBA)', '1. Primera vuelta', '2. Segunda vuelta', '4. Buena persona', '6. La mejor opción primera vuelta',
                    '7. La mejor opción segunda vuelta', '8. Oratoria', '10. Traerá más "libertad" a Argentina', '15. Sería mejor un gobierno peronista']


# Bivariate Analyse

def analyze_numerical_vs_numerical(df, num_vars):
    """   Analyzes relationships between numerical variables"""
    print("\n" + "="*80)
    print("Analyzes relationships between numerical variables")
    print("="*80)
    
    if len(num_vars) < 2:
        print("At least 2 numeric variables required")
        return
    
    # Correlation matrix / Pearson correlation
    df_num = df[num_vars].select_dtypes(include=[np.number])
    correlation_matrix = df_num.corr()
    
    print("Correlation matrix (Pearson):")
    print(correlation_matrix.round(3))
    
    # Heatmap of Correlations
    plt.figure(figsize=(14, 10))
    mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))  # Hide upper triangular matrix
    sns.heatmap(correlation_matrix, 
                annot=True, 
                cmap='RdBu_r', 
                center=0,
                square=True, 
                mask=mask,
                cbar_kws={"shrink": .8})
    plt.title('Correlation Matrix - Numeric Variables', fontsize=16, pad=20)
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.savefig('correlation matrix.png', dpi=300, bbox_inches='tight')
    plt.show()
    input("Press Enter to continue...")


    # Identify strong correlations
    print("STRONG CORRELATIONS")
    strong_corr = []
    for i in range(len(correlation_matrix.columns)):
        for j in range(i+1, len(correlation_matrix.columns)):
            corr_val = correlation_matrix.iloc[i, j]
            if abs(corr_val) > 0.5:
                var1 = correlation_matrix.columns[i]
                var2 = correlation_matrix.columns[j]
                strong_corr.append((var1, var2, corr_val))
                print(f"   {var1} ↔ {var2}: r = {corr_val:.3f}")
    
    # Scatter-Plots strong correlations
    if strong_corr:
        n_plots = min(6, len(strong_corr))
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        axes = axes.flatten()
        
        for i, (var1, var2, corr_val) in enumerate(strong_corr[:n_plots]):
            # Scatter plot
            axes[i].scatter(df[var1], df[var2], alpha=0.6, s=50)
            
            # regression line
            sns.regplot(data=df, x=var1, y=var2, ax=axes[i], 
                       scatter=False, color='red', line_kws={'linewidth': 2})
            
            axes[i].set_xlabel(var1, fontsize=10)
            axes[i].set_ylabel(var2, fontsize=10)
            axes[i].set_title(f'{var1} vs {var2}\nCorrelation: r = {corr_val:.3f}', fontsize=11)
            
            # Statistical test
            clean_data = df[[var1, var2]].dropna()
            if len(clean_data) > 2:
                stat, p_val = pearsonr(clean_data[var1], clean_data[var2])
                axes[i].text(0.05, 0.95, f'p = {p_val:.3f}', 
                           transform=axes[i].transAxes, fontsize=9,
                           bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
        
        # Hide empty subplots
        for k in range(i + 1, len(axes)):
            axes[k].set_visible(False)
        
        plt.suptitle('Scatter-Plots for strong correlations', fontsize=16)
        plt.tight_layout()
        plt.savefig('scatter_plots_strong_corr.png', dpi=300, bbox_inches='tight')
        plt.show()
        input("Press Enter to continue...")

    else:
        print("Keine starken Korrelationen gefunden (|r| > 0.5)")

if __name__ == "__main__":
    analyze_numerical_vs_numerical(df, numerical_vars)