import os
import pandas as pd
from tqdm import tqdm

repos = pd.read_csv('data/raw/top_java_repos.csv')
summary_rows = []
for idx, row in tqdm(repos.iterrows(), total=len(repos)):
    repo = row['full_name']
    repo_dir = f"repos_extracted/{repo.replace('/', '_')}_master"
    ck_csv = f"metrics/{repo_dir}/class.csv"
    if not os.path.exists(ck_csv):
        continue
    try:
        df = pd.read_csv(ck_csv)
        lcom_col = next((c for c in ["lcom", "lcom*", "lcom3", "lcom4"] if c in df.columns), None)
        metrics = {}
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
        out = {
            "repo": repo,
            "stargazers_count": row['stargazers_count'],
            "forks_count": row['forks_count'],
            "age_years": row['age_years'],
            **metrics
        }
        summary_rows.append(out)
    except Exception as e:
        print(f"Erro processando {repo}: {e}")
pd.DataFrame(summary_rows).to_csv("all_metrics_1000.csv", index=False)