import pandas as pd, sys, statistics as st
path="data/metrics/repo0/ck/class.csv"
df=pd.read_csv(path)
df.columns=[c.lower() for c in df.columns]
cols=[c for c in ["cbo","dit","lcom"] if c in df.columns]
rows=[]
for c in cols:
    vals=[v for v in df[c].dropna().tolist() if isinstance(v,(int,float))]
    if not vals: 
        rows.append({"metric":c,"count":0,"mean":None,"median":None,"std":None}); continue
    rows.append({
      "metric":c,
      "count":len(vals),
      "mean":round(sum(vals)/len(vals),3),
      "median":round(st.median(vals),3),
      "std":round(st.pstdev(vals),3) if len(vals)>1 else 0.0
    })
out="summaries/ck_summary_repo0.csv"
import os; os.makedirs("summaries",exist_ok=True)
pd.DataFrame(rows).to_csv(out,index=False)
print("Resumo salvo em",out)