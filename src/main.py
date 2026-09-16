from pathlib import Path
import csv, heapq, math
ROOT=Path(__file__).resolve().parents[1]; DATA=ROOT/'data/pedidos.csv'; DOCS=ROOT/'docs'; DOCS.mkdir(exist_ok=True)
G={'A':{'B':4,'D':2},'B':{'A':4,'C':3,'E':1},'C':{'B':3,'F':2},'D':{'A':2,'E':3,'G':5},'E':{'B':1,'D':3,'F':2,'H':4},'F':{'C':2,'E':2,'I':3},'G':{'D':5,'H':2},'H':{'G':2,'E':4,'I':2},'I':{'F':3,'H':2}}
P={'A':(0,0),'B':(1,0),'C':(2,0),'D':(0,1),'E':(1,1),'F':(2,1),'G':(0,2),'H':(1,2),'I':(2,2)}
def h(a,b): return abs(P[a][0]-P[b][0])+abs(P[a][1]-P[b][1])
def path(prev,n):
 r=[n]
 while n in prev: n=prev[n]; r.append(n)
 return r[::-1]
def astar(s,t):
 q=[(h(s,t),0,s)]; cost={s:0}; prev={}
 while q:
  _,g,n=heapq.heappop(q)
  if n==t:return path(prev,n),g
  for v,w in G[n].items():
   ng=g+w
   if ng<cost.get(v,math.inf): cost[v]=ng;prev[v]=n;heapq.heappush(q,(ng+h(v,t),ng,v))
def bfs(s,t):
 q=[[s]];seen={s}
 while q:
  p=q.pop(0); n=p[-1]
  if n==t:return p
  for v in G[n]:
   if v not in seen:seen.add(v);q.append(p+[v])
def dist(p): return sum(G[p[i]][p[i+1]] for i in range(len(p)-1))
def kmeans(points,k=2):
 c=[points[0][:],points[-1][:]]; groups=[-1]*len(points)
 for _ in range(30):
  ng=[]
  for p in points: ng.append(min(range(k),key=lambda i:(p[0]-c[i][0])**2+(p[1]-c[i][1])**2))
  if ng==groups:break
  groups=ng
  for i in range(k):
   m=[p for p,g in zip(points,groups) if g==i]
   if m:c[i]=[sum(p[0] for p in m)/len(m),sum(p[1] for p in m)/len(m)]
 return groups,c
def main():
 a,ca=astar('A','I'); b=bfs('A','I'); cb=dist(b)
 with DATA.open(encoding='utf8') as f: rows=list(csv.DictReader(f))
 groups,cent=kmeans([[float(r['x']),float(r['y'])] for r in rows])
 out=[f'Rota A*: {" -> ".join(a)}',f'Distância A*: {ca} km',f'Rota BFS: {" -> ".join(b)}',f'Distância BFS: {cb} km',f'Economia do A*: {cb-ca} km','', 'Agrupamento K-Means:']+[f'{r["id"]} ({r["bairro"]}) -> grupo {g+1}' for r,g in zip(rows,groups)]
 text='\n'.join(out);print(text);(DOCS/'resultado.txt').write_text(text,encoding='utf8')
if __name__=='__main__':main()
