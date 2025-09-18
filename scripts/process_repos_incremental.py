import os
import requests
import zipfile
import shutil
import subprocess

CK_JAR_PATH = "../ck-tool/ck.jar"  # ajuste se necessário
METRICS_DIR = "metrics"
TEMP_DIR = "temp_repo"
REPOS_FILE = "repos.txt"

os.makedirs(METRICS_DIR, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)

with open(REPOS_FILE) as f:
    urls = [line.strip() for line in f if line.strip()]

for url in urls:
    repo_id = url.split("/")[-4] + "_" + url.split("/")[-3] + "_" + url.split("/")[-2] + "_" + url.split("/")[-1].replace(".zip", "")
    zip_path = os.path.join(TEMP_DIR, f"{repo_id}.zip")
    print(f"\n[Baixando] {url} ...")
    try:
        r = requests.get(url, timeout=60, stream=True)
        if r.status_code == 200:
            with open(zip_path, "wb") as fzip:
                for chunk in r.iter_content(1024 * 1024):
                    fzip.write(chunk)
        else:
            print(f"[ERRO] Falha ao baixar: status {r.status_code}")
            continue
    except Exception as e:
        print(f"[ERRO] Falha ao baixar: {e}")
        continue

    shutil.rmtree(os.path.join(TEMP_DIR, "repo"), ignore_errors=True)
    os.makedirs(os.path.join(TEMP_DIR, "repo"), exist_ok=True)
    try:
        with zipfile.ZipFile(zip_path, 'r') as z:
            z.extractall(os.path.join(TEMP_DIR, "repo"))
    except Exception as e:
        print(f"[ERRO] Falha ao extrair: {e}")
        os.remove(zip_path)
        continue

    # Descobrir pasta principal extraída
    main_dir = None
    for item in os.listdir(os.path.join(TEMP_DIR, "repo")):
        full = os.path.join(TEMP_DIR, "repo", item)
        if os.path.isdir(full):
            main_dir = full
            break
    if not main_dir:
        print(f"[ERRO] Não encontrou pasta extraída.")
        os.remove(zip_path)
        continue

    # Só roda CK se houver arquivos Java
    has_java = False
    for root, dirs, files in os.walk(main_dir):
        for file in files:
            if file.endswith(".java"):
                has_java = True
                break
        if has_java: break

    if has_java:
        print(f"[CK] Rodando CK para {repo_id} ...")
        metrics_out = os.path.join(METRICS_DIR, repo_id)
        os.makedirs(metrics_out, exist_ok=True)
        try:
            subprocess.run([
                "java", "-jar", CK_JAR_PATH,
                main_dir, "false", "0", "true", metrics_out
            ], check=False)
        except Exception as e:
            print(f"[ERRO] Falha ao rodar CK: {e}")
    else:
        print(f"[SKIP] Sem arquivos Java em {repo_id}")

    shutil.rmtree(os.path.join(TEMP_DIR, "repo"), ignore_errors=True)
    os.remove(zip_path)