import re, sys
B='/Users/benq/Desktop/qnsc/opc/design/system/directions/modern/'
src=[open(B+'skin-modern.css').read(), open(B+'redesign/redesign.css').read(), open(B+'redesign/calm.css').read()]
HEX={'#ffffff':'var(--surface)','#fff':'var(--surface)','#f8f9fa':'var(--canvas-quiet)','#93370d':'var(--pend-ink)','#b54708':'var(--pend)',
'#e7f6ee':'var(--ok-soft)','#12b76a':'var(--truth-ok)','#32d583':'var(--truth-ok)','#12a35f':'var(--truth-ok)','#05603a':'var(--ok-strong)','#067647':'var(--ok)',
'#fff6e0':'var(--pend-soft)','#fffaf2':'var(--pend-soft)','#fff4e5':'var(--pend-soft)','#fff3e2':'var(--pend-soft)','#ffefc7':'var(--pend-soft-hover)','#ffe3a6':'var(--pend-stripe)',
'#f79009':'var(--truth-pend)','#e08a00':'var(--truth-pend)','#ffd56b':'var(--truth-pend)',
'#f2f7ff':'var(--act-soft)','#f0f6ff':'var(--act-soft)','#eef7fb':'var(--act-soft)','#e8f1ff':'var(--act-soft)','#e5efff':'var(--act-soft)',
'#f2f4f6':'var(--surface-sunk)','#e9f8ef':'var(--ok-soft)','#e9ecef':'var(--neutral-fill)','#d5dade':'var(--neutral-fill-hover)','#d5d9de':'var(--line-quiet)',
'#e7e9ec':'var(--line)','#c9ced5':'var(--truth-cash)','#d9eef6':'var(--act-ring)','#dbe8ff':'var(--act-ring)','#a6f4c5':'var(--ok-soft)','#75e0a7':'var(--ok-soft)',
'#0b6b93':'var(--act)','#08577a':'var(--act-hover)','#062f45':'var(--brand-900)'}
def items(css):
    out=[];i=0;n=len(css)
    while i<n:
        if css[i].isspace(): i+=1; continue
        if css.startswith('/*',i):
            j=css.index('*/',i)+2; out.append(('c',css[i:j])); i=j; continue
        j=css.index('{',i); head=css[i:j].strip(); d=1; k=j+1
        while d: d+= {'{':1,'}':-1}.get(css[k],0); k+=1
        body=css[j+1:k-1]; out.append(('a' if head.startswith('@') else 'r',head,body)); i=k
    return out
DROP=re.compile(r'r-money-hero|data-brand|^:root')
def is_r(sel): return bool(re.search(r'\.r-|\[data-tip', sel)) and not sel.startswith('.c-') or re.search(r'\.r-',sel) is not None
comp=[];rec=[]
def clean(body):
    decls=[d for d in body.split(';') if '--hero-' not in d]
    b=';'.join(decls)
    for h,v in sorted(HEX.items(),key=lambda x:-len(x[0])): b=re.sub(re.escape(h)+r'\b',v,b,flags=re.I)
    return b
def place(head,body,cm,rc):
    if DROP.search(head): return
    b=clean(body)
    if not b.strip().strip(';').strip(): return
    (rc if re.search(r'\.r-',head) else cm).append(f'{head} {{{b}}}')
for css in src:
    for it in items(css):
        if it[0]=='c': continue
        _,head,body=it
        if head.startswith('@keyframes'): comp.append(f'{head} {{{body}}}'); continue
        if head.startswith('@'):
            cm=[];rc=[]
            for sub in items(body):
                if sub[0]=='r': place(sub[1],sub[2],cm,rc)
            if cm: comp.append(head+' {\n  '+'\n  '.join(cm)+'\n}')
            if rc: rec.append(head+' {\n  '+'\n  '.join(rc)+'\n}')
        else: place(head,body,comp,rec)
open(B+'_merge/components-v4.css','w').write('\n'.join(comp)+'\n')
open(B+'_merge/recipes-v4.css','w').write('\n'.join(rec)+'\n')
left=re.findall(r'#[0-9a-fA-F]{3,8}\b','\n'.join(comp+rec))
print(len(comp),len(rec),'hex left:',sorted(set(left)))
print('hero refs left:', sum(x.count('--hero') for x in comp+rec))
