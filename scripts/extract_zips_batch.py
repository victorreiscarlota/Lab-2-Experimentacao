import zipfile
import os
from tqdm import tqdm

os.makedirs('repos_extracted', exist_ok=True)
for fname in tqdm(os.listdir('repos')):
    if fname.endswith('.zip'):
        zipf_path = os.path.join('repos', fname)
        outdir = os.path.join('repos_extracted', fname.replace('.zip', ''))
        if not os.path.exists(outdir):
            try:
                with zipfile.ZipFile(zipf_path, 'r') as z:
                    z.extractall(outdir)
            except Exception as e:
                print(f"Erro ao extrair {fname}: {e}")