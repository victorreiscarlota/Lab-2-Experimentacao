import os
import pandas as pd

REPOS_CSV = "./top_java_repos.csv"  # ajuste se necessário
METRICS_DIR = "metrics"

# Carrega dados dos repositórios (popularidade, idade, etc)
repos = pd.read_csv(REPOS_CSV)
repos['repo_id'] = repos['full_name'].apply(lambda x: x.replace("/", "_") + "_master")

rows = []
for idx, row in repos.iterrows():
    repo_id = row['repo_id']
    ck_file = os.path.join(METRICS_DIR, f"{repo_id}class.csv")
    if not os.path.exists(ck_file):
        continue
    try:
        df = pd.read_csv(ck_file)
        lcom_col = next((c for c in ["lcom", "lcom*", "lcom3", "lcom4"] if c in df.columns), None)
        metrics = {}
        # Métricas de qualidade
        for metric in ["cbo", "dit"]:
            if metric in df.columns:
                serie = pd.to_numeric(df[metric], errors="coerce").dropna()
                metrics[metric+"_mean"] = serie.mean()
                metrics[metric+"_median"] = serie.median()
                metrics[metric+"_std"] = serie.std()
        if lcom_col:
            serie = pd.to_numeric(df[lcom_col], errors="coerce").dropna()
            metrics["lcom_mean"] = serie.mean()
            metrics["lcom_median"] = serie.median()
            metrics["lcom_std"] = serie.std()
        # Tamanho: LOC e comentários
        if "loc" in df.columns:
            metrics["loc_sum"] = pd.to_numeric(df["loc"], errors="coerce").sum()
        if "comments" in df.columns:
            metrics["comments_sum"] = pd.to_numeric(df["comments"], errors="coerce").sum()
        out = {
            "repo": row['full_name'],
            "stars": row['stargazers_count'],
            "forks": row['forks_count'],
            "age": row['age_years'],
            **metrics
        }
        rows.append(out)
    except Exception as e:
        print(f"Erro processando {repo_id}: {e}")

df_out = pd.DataFrame(rows)
df_out.to_csv("all_metrics.csv", index=False)
print("Arquivo all_metrics.csv gerado!")