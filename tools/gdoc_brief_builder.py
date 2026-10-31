"""Builds Google Docs batchUpdate requests for one TTM brief tab, simulating indexes.
Content model:
  block = ('p', runs, pstyle)  runs = [(text, tstyle)], pstyle in {'h2','left','center',None}
        | ('t', [[cell_blocks,...],...rows], opts)   opts: widths list, kind 'meta'|'subj'|'wire'|'card'
"""
import json
GREY={"red":0.451,"green":0.451,"blue":0.451}
NAVY={"red":0.302,"green":0.392,"blue":0.533}
def rgb(h): return {"red":int(h[1:3],16)/255,"green":int(h[3:5],16)/255,"blue":int(h[5:7],16)/255}
TS={
 'b':({"bold":True},"bold"),
 'i':({"italic":True},"italic"),
 'hero':({"bold":True,"fontSize":{"magnitude":24,"unit":"PT"}},"bold,fontSize"),
 'h15':({"bold":True,"fontSize":{"magnitude":15,"unit":"PT"}},"bold,fontSize"),
 'ph':({"italic":True,"fontSize":{"magnitude":9,"unit":"PT"},"foregroundColor":{"color":{"rgbColor":GREY}}},"italic,fontSize,foregroundColor"),
 'small':({"fontSize":{"magnitude":9,"unit":"PT"}},"fontSize"),
 'link':({"underline":True,"foregroundColor":{"color":{"rgbColor":NAVY}}},"underline,foregroundColor"),
}
class B:
    def __init__(s,tab):
        s.tab=tab; s.ins=[]; s.rng=[]; s.pst=[]; s.tst=[]
    def L(s,i): return {"index":i,"tabId":s.tab}
    def R(s,a,b): return {"startIndex":a,"endIndex":b,"tabId":s.tab}
    def container(s,p,blocks):
        """p = index of the container's empty paragraph. Returns length added."""
        cur=p; empty=True; added=0
        buf=[]  # pending paragraphs: (runs, ps)
        def flush():
            nonlocal cur,empty,added
            if not buf: return
            texts=[''.join(t for t,_ in r) for r,_ in buf]
            joined='\n'.join(texts)
            if empty:
                ins=joined; start=cur
            else:
                ins='\n'+joined; start=cur+1
            if ins: s.ins.append({"insertText":{"location":s.L(cur),"text":ins}})
            pos=start
            for (r,ps),tx in zip(buf,texts):
                q=pos
                for t,st in r:
                    if st and t: s.tst.append((q,q+len(t),st))
                    q+=len(t)
                if ps and ps!='center': s.pst.append((pos,pos+len(tx)+1,ps))
                pos+=len(tx)+1
            cur+=len(ins); added+=len(ins); empty=False; buf.clear()
        for bl in blocks:
            if bl[0]=='p':
                buf.append((bl[1],bl[2]))
            else:
                flush()
                rows,opts=bl[1],bl[2]
                R=len(rows); C=len(rows[0]); i=cur
                s.ins.append({"insertTable":{"rows":R,"columns":C,"location":s.L(i)}})
                tstart=i+1
                s.pst.append(('table',tstart,R,C,opts))
                off=0
                for r in range(R):
                    for c in range(C):
                        cp=i+4+r*(2*C+1)+2*c+off
                        off+=s.container(cp,rows[r][c])
                cur=i+3+R*(2*C+1)+off
                if opts.get('center'): s.rng.append((tstart,cur-1))
                added+=3+R*(2*C+1)+off
                empty=True
        flush()
        return added
    def requests(s):
        out=list(s.ins)
        for item in s.pst:
            if item[0]=='table':
                _,ts,R,C,o=item
                loc={"index":ts,"tabId":s.tab}
                for ci,w in enumerate(o.get('widths',[])):
                    out.append({"updateTableColumnProperties":{"tableStartLocation":loc,"columnIndices":[ci],"tableColumnProperties":{"widthType":"FIXED_WIDTH","width":{"magnitude":w,"unit":"PT"}},"fields":"widthType,width"}})
                bw=o.get('bw',1); bc=rgb(o.get('bc','#000000'))
                border={"color":{"color":{"rgbColor":bc}},"width":{"magnitude":bw,"unit":"PT"},"dashStyle":"SOLID"}
                pad=o.get('pad',(4,4))
                cs={"borderTop":border,"borderBottom":border,"borderLeft":border,"borderRight":border,
                    "paddingTop":{"magnitude":pad[0],"unit":"PT"},"paddingBottom":{"magnitude":pad[0],"unit":"PT"},
                    "paddingLeft":{"magnitude":pad[1],"unit":"PT"},"paddingRight":{"magnitude":pad[1],"unit":"PT"},"contentAlignment":"TOP"}
                f="borderTop,borderBottom,borderLeft,borderRight,paddingTop,paddingBottom,paddingLeft,paddingRight,contentAlignment"
                if o.get('fill'): cs["backgroundColor"]={"color":{"rgbColor":rgb(o['fill'])}}; f+=",backgroundColor"
                out.append({"updateTableCellStyle":{"tableRange":{"tableCellLocation":{"tableStartLocation":loc,"rowIndex":0,"columnIndex":0},"rowSpan":R,"columnSpan":C},"tableCellStyle":cs,"fields":f}})
                if o.get('labelfill'):
                    out.append({"updateTableCellStyle":{"tableRange":{"tableCellLocation":{"tableStartLocation":loc,"rowIndex":0,"columnIndex":0},"rowSpan":R,"columnSpan":1},"tableCellStyle":{"backgroundColor":{"color":{"rgbColor":rgb(o['labelfill'])}}},"fields":"backgroundColor"}})
        for a,b in s.rng:
            out.append({"updateParagraphStyle":{"range":s.R(a,b),"paragraphStyle":{"alignment":"CENTER","spaceAbove":{"magnitude":2,"unit":"PT"},"spaceBelow":{"magnitude":2,"unit":"PT"},"lineSpacing":100},"fields":"alignment,spaceAbove,spaceBelow,lineSpacing"}})
        for item in s.pst:
            if item[0]!='table':
                a,b,ps=item
                if ps in ('h2','h3'):
                    out.append({"updateParagraphStyle":{"range":s.R(a,b),"paragraphStyle":{"namedStyleType":"HEADING_2" if ps=='h2' else "HEADING_3"},"fields":"namedStyleType"}})
                else:
                    al={"center":"CENTER","left":"START"}[ps]
                    out.append({"updateParagraphStyle":{"range":s.R(a,b),"paragraphStyle":{"alignment":al,"spaceAbove":{"magnitude":2,"unit":"PT"},"spaceBelow":{"magnitude":2,"unit":"PT"},"lineSpacing":100},"fields":"alignment,spaceAbove,spaceBelow,lineSpacing"}})
        for a,b,st in s.tst:
            for k in st.split('+'):
                ts,f=TS[k]
                out.append({"updateTextStyle":{"range":s.R(a,b),"textStyle":ts,"fields":f}})
        return out

# ---- content helpers
import re
def runs(text, base=None):
    """**bold** markup -> runs"""
    out=[]
    for k,part in enumerate(re.split(r'\*\*',text)):
        if not part: continue
        st=base
        if k%2==1: st=(base+'+b') if base else 'b'
        out.append((part,st))
    return out or [('',None)]
def P(text, st=None, ps='center'): return ('p',runs(text,st),ps)
def H2(text): return ('p',[(text,None)],'h2')
def H3(text): return ('p',[(text,None)],'h3')
def BL(): return ('p',[('',None)],None)
def T(rows,**o): return ('t',rows,o)
def meta(name,date,brief):
    lab=lambda x:[('p',[(x,'b')],None)]
    val=lambda x:[('p',runs(x),None)]
    return T([[lab('Email name'),val(name)],[lab('Send date'),val(date)],[lab('Brief'),val(brief)]],widths=[105,345])
def subj(sl,pv,sn):
    lab=lambda x:[('p',[(x,'b')],None)]
    val=lambda x:[('p',runs(x),None)]
    return T([[lab('Subject line'),val(sl)],[lab('Preview line'),val(pv)],[lab('Sender name'),val(sn)]],widths=[105,345],labelfill='#C9DAF8')
def wire(rows): return T([[r] for r in rows],widths=[450],pad=(10,14),center=True)
def cards(cols, items):
    w={1:[410],2:[205,205],3:[136,136,136]}[cols]
    rows=[items[i:i+cols] for i in range(0,len(items),cols)]
    return T(rows,widths=w,fill='#F3F3F3',bc='#BFBFBF',bw=0.75,pad=(8,8))
def build(tab, blocks):
    b=B(tab); b.container(1,blocks); return b.requests()
