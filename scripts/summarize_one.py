import argparse
import os
import sys
import pandas as pd
from pathlib import Path

LCOM_CANDIDATES = ["lcom", "lcom*", "lcom3", "lcom4"]

def guess_repo_name(csv_path: Path) -> str:
    parent = csv_path.parent.name
    if parent.startswith("metrics-"):
        return parent[len("metrics-"):]
    if parent in ("ck", "ck_output", "output"):
        grand = csv_path.parent.parent.name
        if grand.startswith("metrics-"):
            return grand[len("metrics-"):]
        return grand
    return parent

def detect_lcom_column(columns):
    for cand in LCOM_CANDIDATES:
        if cand in columns:
            return cand
    return None

def compute_stats(label: str, series: pd.Series):
    series = pd.to_numeric(series, errors="coerce").dropna()
    if len(series) == 0:
        return None
    return {
        "metric": label,
        "count": int(series.count()),
        "mean": round(float(series.mean()), 6),
        "median": round(float(series.median()), 6),
        "std": round(float(series.std()), 6)
    }

def summarize(df: pd.DataFrame):
    rows = []
    if "cbo" in df.columns:
        r = compute_stats("cbo", df["cbo"])
        if r: rows.append(r)
    if "dit" in df.columns:
        r = compute_stats("dit", df["dit"])
        if r: rows.append(r)

    lcom_col = detect_lcom_column(df.columns)
    if lcom_col:
        r = compute_stats("lcom", df[lcom_col])
        if r: rows.append(r)

    if not rows:
        raise ValueError("Nenhuma métrica (cbo/dit/lcom) encontrada no CSV.")

    return pd.DataFrame(rows)

def main():
    parser = argparse.ArgumentParser(description="Sumariza métricas CK (CBO, DIT, LCOM) a partir de class.csv.")
    parser.add_argument("--path", required=True, help="Caminho para class.csv gerado pelo CK.")
    parser.add_argument("--out", default="summaries", help="Diretório de saída (default: summaries).")
    parser.add_argument("--repo-name", help="Nome do repositório (senão é inferido).")
    args = parser.parse_args()

    csv_path = Path(args.path)
    if not csv_path.is_file():
        print(f"[ERRO] Arquivo não encontrado: {csv_path}", file=sys.stderr)
        sys.exit(1)

    try:
        df = pd.read_csv(csv_path)
    except Exception as e:
        print(f"[ERRO] Falha lendo CSV: {e}", file=sys.stderr)
        sys.exit(2)

    try:
        summary_df = summarize(df)
    except ValueError as e:
        print(f"[ERRO] {e}", file=sys.stderr)
        sys.exit(3)

    repo_name = args.repo_name or guess_repo_name(csv_path)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / f"ck_summary_{repo_name}.csv"

    summary_df.to_csv(out_file, index=False)
    print(f"Resumo salvo em: {out_file}")
    print(summary_df.to_string(index=False))

if __name__ == "__main__":
    main()