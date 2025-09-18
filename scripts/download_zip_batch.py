import pandas as pd
import requests
import os
from tqdm import tqdm

repos = pd.read_csv('data/raw/top_java_repos.csv')
os.makedirs('repos', exist_ok=True)
for idx, row in tqdm(repos.iterrows(), total=len(repos)):
    repo = row['full_name']
    url = f"https://github.com/{repo}/archive/refs/heads/master.zip"
    dest = f"repos/{repo.replace('/', '_')}_master.zip"
    if not os.path.exists(dest):
        try:
            r = requests.get(url, timeout=40)
            if r.status_code == 200:
                with open(dest, 'wb') as f:
                    f.write(r.content)
        except Exception as e:
            print(f"Erro ao baixar {repo}: {e}")