import os, math, time, csv, requests
from datetime import datetime, timezone
TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = {"Accept":"application/vnd.github+json","User-Agent":"lab-metrics"}
if TOKEN: HEADERS["Authorization"] = f"Bearer {TOKEN}"
OUT="data/raw/top_java_repos.csv"
def main():
    os.makedirs("data/raw", exist_ok=True)
    rows=[]
    for page in range(1,11):  
        r=requests.get("https://api.github.com/search/repositories",
                        params={"q":"language:Java","sort":"stars","order":"desc","per_page":100,"page":page},
                        headers=HEADERS)
        if r.status_code!=200:
            print("ERRO",r.status_code,r.text); break
        for repo in r.json().get("items",[]):
            created=repo["created_at"]
            dt=datetime.fromisoformat(created.replace("Z","+00:00"))
            age_years=(datetime.now(timezone.utc)-dt).days/365.25
            rows.append({
              "full_name":repo["full_name"],
              "stargazers_count":repo["stargazers_count"],
              "forks_count":repo["forks_count"],
              "created_at":created,
              "age_years":round(age_years,3)
            })
        time.sleep(1)
    if rows:
        with open(OUT,"w",newline="",encoding="utf-8") as f:
            w=csv.DictWriter(f,fieldnames=rows[0].keys())
            w.writeheader(); w.writerows(rows)
        print("OK:",len(rows),"salvos em",OUT)
if __name__=="__main__":
    main()