import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import zscore
import os

os.makedirs("figs", exist_ok=True)
df = pd.read_csv('all_metrics.csv')

# Adiciona colunas logarítmicas
for col in ['stars', 'age', 'loc_sum']:
    if col in df.columns:
        df[f'log_{col}'] = np.log10(df[col].replace(0, np.nan))

# 1. Matriz de correlação (processo + qualidade)
corr_cols = [col for col in ['stars','log_stars','age','log_age','loc_sum','log_loc_sum','cbo_mean','dit_mean','lcom_mean'] if col in df.columns]
corr = df[corr_cols].corr()
plt.figure(figsize=(10,8))
sns.heatmap(corr, annot=True, cmap='vlag', fmt=".2f")
plt.title("Matriz de Correlação: Processo e Qualidade")
plt.tight_layout()
plt.savefig("figs/1.png")
plt.close()

def plot_scatter_reg_outliers(x, y, x_label, y_label, title, fname):
    plt.figure(figsize=(8,6))
    sns.scatterplot(x=x, y=y, alpha=0.7, label="Dados")
    sns.regplot(x=x, y=y, scatter=False, color="red", label="Tendência")
    # Outliers em y (z-score > 3)
    if len(y.dropna()) > 0:
        zscores = np.abs(zscore(y.dropna()))
        outlier_idx = y[zscores > 3].index
        plt.scatter(x[outlier_idx], y[outlier_idx], color="orange", marker="x", s=60, label="Outliers")
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.savefig(fname)
    plt.close()

# 2. Popularidade (log estrelas) vs CBO (RQ1)
if 'log_stars' in df.columns and 'cbo_mean' in df.columns:
    plot_scatter_reg_outliers(
        df['log_stars'], df['cbo_mean'],
        "Log10 Estrelas", "CBO Médio",
        "RQ1: Popularidade vs CBO",
        "figs/2.png"
    )

# 3. Maturidade (log idade) vs DIT (RQ2)
if 'log_age' in df.columns and 'dit_mean' in df.columns:
    plot_scatter_reg_outliers(
        df['log_age'], df['dit_mean'],
        "Log10 Idade (anos)", "DIT Médio",
        "RQ2: Maturidade vs DIT",
        "figs/3.png"
    )

# 4. Tamanho (log LOC) vs LCOM (RQ4)
if 'log_loc_sum' in df.columns and 'lcom_mean' in df.columns:
    plot_scatter_reg_outliers(
        df['log_loc_sum'], df['lcom_mean'],
        "Log10 Tamanho (LOC)", "LCOM Médio",
        "RQ4: Tamanho vs LCOM",
        "figs/4.png"
    )