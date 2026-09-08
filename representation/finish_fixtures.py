from pathlib import Path
import json, math, zipfile, xml.etree.ElementTree as ET
R=Path(__file__).parent
# These are stipulated symbolic worlds, not records of a person navigating or waiting.
def walk(start, heading, commands):
    p=list(start); h=heading
    vectors=[(0,1),(1,0),(0,-1),(-1,0)]
    for cmd in commands:
        if cmd=='R': h=(h+1)%4
        elif cmd=='L': h=(h-1)%4
        elif cmd=='F':
            dx,dy=vectors[h];p[0]+=dx;p[1]+=dy
        else: raise ValueError(cmd)
    return {'position':p,'heading':h}
def edits(items, operations):
    a=[dict(x) for x in items]
    for op,key in operations:
        if op=='delete_position': a.pop(key)
        elif op=='tag_position': a[key]['tag']=True
        elif op in ['delete_id','tag_id']:
            matches=[i for i,x in enumerate(a) if x['id']==key]
            if len(matches)!=1: return {'error':'identity is not unique','matches':len(matches)}
            if op=='delete_id': a.pop(matches[0])
            else:a[matches[0]]['tag']=True
    return a
def timer(events, policy):
    starts=[];active=None;outputs=[]
    for kind,t in events:
        if kind=='ready':
            if policy=='every_ready' or active is None:
                active=t; starts.append(t)
        elif kind=='cancel':active=None
        elif kind=='poll' and active is not None:
            outputs.append({'at':t,'remaining':max(0,5-(t-active)),'due':t>=active+5})
    return {'starts':starts,'active':active,'outputs':outputs}
items=[{'id':'A','text':'alpha'},{'id':'B','text':'beta'},{'id':'C','text':'gamma'}]
results={
'route':{
 'same_words_different_heading':{'north':walk([0,0],0,'FRFF'),'east':walk([0,0],1,'FRFF')},
 'same_position_different_heading':{'start':walk([0,0],0,''),'open_square':walk([0,0],0,'FRFRFRF')},
 'held_out_anchored':{'east_FRFF':walk([2,3],1,'FRFF'),'north_FRFF':walk([2,3],0,'FRFF')},
 'mirror':{'right':walk([0,0],0,'FRF'),'left':walk([0,0],0,'FLF')},
 'reverse_turn_order':{'FRF':walk([0,0],0,'FRF'),'RFF':walk([0,0],0,'RFF')}
},
'edit':{
 'live_vs_initial_position':{'live':edits(items,[('delete_position',0),('tag_position',1)]),'initial_identity':edits(items,[('delete_id','A'),('tag_id','B')])},
 'reordered_held_out':edits([items[2],items[0],items[1]],[('delete_id','A'),('tag_id','B')]),
 'duplicate_identity':edits([{'id':'A'},{'id':'B'},{'id':'B'}],[('tag_id','B')]),
 'delete_noncommuting':{'delete_then_tag':edits(items,[('delete_position',0),('tag_position',1)]),'tag_then_delete':edits(items,[('tag_position',1),('delete_position',0)])},
 'stable_id_commuting':{'delete_then_tag':edits(items,[('delete_id','A'),('tag_id','B')]),'tag_then_delete':edits(items,[('tag_id','B'),('delete_id','A')])}
},
'clock':{
 'anchor_difference':{'display_anchor_due':0+5,'ready_anchor_due':3+5},
 'duplicate_ready':{'restart':timer([('ready',3),('ready',6),('poll',8)],'every_ready'),'first':timer([('ready',3),('ready',6),('poll',8)],'first_ready')},
 'cancel_and_restart':timer([('ready',3),('cancel',4),('ready',10),('poll',14),('poll',15)],'first_ready'),
 'late_poll':timer([('ready',3),('poll',10)],'first_ready'),
 'held_out':timer([('ready',11),('ready',13),('poll',15),('poll',16)],'first_ready')
}}
(R/'finish-fixture-results.json').write_text(json.dumps(results,indent=2))
# Refresh an audit extract against the actual exported artifact; no deck source changes.
with zipfile.ZipFile(R/'representation-scope-specimen.pptx') as z:
    slides=[]
    for name in sorted(n for n in z.namelist() if __import__('re').fullmatch(r'ppt/slides/slide\d+.xml',n)):
        texts=[x.text or '' for x in ET.fromstring(z.read(name)).iter('{http://schemas.openxmlformats.org/drawingml/2006/main}t')]
        slides.append({'slide':name,'texts':texts,'word_count':sum(len(t.split()) for t in texts)})
(R/'slides-build/text-check.json').write_text(json.dumps(slides,indent=2))
print(json.dumps(results,indent=2))
