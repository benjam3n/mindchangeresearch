import fs from 'node:fs/promises';
import {Presentation,PresentationFile} from '@oai/artifact-tool';
async function main(){
const root='/workspace/scratch/78b838bd97fc/mind-change-research/representation';
const p=Presentation.create({slideSize:{width:1280,height:720}});
const bg='#FAF9F6',ink='#1A1A1A',accent='#3D5A80';
function text(s,t,x,y,w,h,size,bold=false){const z=s.shapes.add({geometry:'textbox',name:t,position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});z.text=t;z.text.style={fontSize:size,bold,color:ink,fontFamily:'Arial'};return z;}
function node(s,t,x,y,fill=bg){const z=s.shapes.add({geometry:'ellipse',position:{left:x,top:y,width:176,height:176},fill,line:{fill:ink,width:4}});const lab=text(s,t,x+24,y+44,128,88,64,true);lab.text.style={fontSize:64,bold:true,color:ink,fontFamily:'Arial',alignment:'center'};return z;}
function line(s,x,y,w,h){return s.shapes.add({geometry:'line',position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:accent,width:5}})}
let cover=p.slides.add();cover.background.fill=bg;text(cover,'Intended mind change:',72,64,1136,96,64,true);text(cover,'Keep claims inside their evidence.',72,256,1136,120,56,true);text(cover,'Exceptions · unknowns · changed criteria',72,456,1136,72,40,false);cover.speakerNotes.textFrame.setText('Research opening required by the current user instruction. The concept slides that follow each contain six visible words/tokens. Intended reader: model/research reviewer familiar with 1/0 outcome notation, with the standalone reference supplied for definitions.');
let s=p.slides.add();s.background.fill=bg;
text(s,'Counterexamples refute universal claims.',72,64,1136,96,56,true);
node(s,'1',352,280);node(s,'0',752,280);
s.speakerNotes.textFrame.setText('Two stipulated operation outcomes: 1 = improved, 0 = did not improve. Not every improved is true; every failed to improve is false. No causal or human-learning inference follows. The nonempty domain is exactly these two operations.\n[Sources]\nLocal derivation: 012-difr-1.md; finite counterexample [1,0].\nDesign contrast: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html\nNon-color labels: https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html\n[/Sources]');
s=p.slides.add();s.background.fill=bg;
text(s,'Unknown keeps alternatives.',72,64,1136,96,64,true);
line(s,352,368,576,0);line(s,624,304,0,64);line(s,352,368,0,104);line(s,928,368,0,104);
const top=text(s,'[1,?]',448,208,352,96,64,true);top.text.style={fontSize:64,bold:true,color:ink,alignment:'center'};
const left=text(s,'[1,1]',224,480,256,96,64,true);left.text.style={fontSize:64,bold:true,color:ink,alignment:'center'};const right=text(s,'[1,0]',768,480,320,96,64,true);right.text.style={fontSize:64,bold:true,color:ink,alignment:'center'};
s.speakerNotes.textFrame.setText('The question mark means an unobserved outcome, not a zero. Two complete inputs remain: [1,1] makes every true; [1,0] makes every false. Some is already true in both because the first result is observed positive. This is a finite logical specimen, not a probability distribution.\n[Sources]\nLocal derivation: 013-difr-2.md.\n[/Sources]');
s=p.slides.add();s.background.fill=bg;
text(s,'Same observations.',72,64,1136,96,64,true);
text(s,'Coverage: B.',72,280,1136,96,64,true);
text(s,'Brevity: A.',72,448,1136,96,64,true);
s.speakerNotes.textFrame.setText('Constructed representation comparison: A contains two cases and B contains all three required cases. For complete three-case coverage B wins. If the task requires only the shared two cases, A has fewer represented cases. The counts stay fixed; the criterion changes. This is not an observation about human comprehension.\n[Sources]\nLocal constructed case: 023-op-1.md and consolidation-04.md.\n[/Sources]');
const close=p.slides.add();close.background.fill=bg;text(close,'Actual mind change:',72,64,1136,96,64,true);text(close,'Three distinctions now have visual forms.',72,200,1136,88,40,true);text(close,'Benefit: Local mappings preserved; human learning untested.',72,320,1136,64,32,false);text(close,'Verdict: KEEP for local artifact construction.',72,400,1136,64,32,false);text(close,'Organization: Visuals plus a standalone reference.',72,480,1136,64,32,false);text(close,'Next attempts: Reader and transfer tests.',72,560,1136,64,32,false);close.speakerNotes.textFrame.setText('Closing research fields required by the current user instruction. They are an explicit exception to the six-word concept-slide constraint. Actual mind change: The current model built and inspected exact visual forms of three existing distinctions. Benefit: Local artifact construction and mappings only; no human learning effect observed. Verdict: KEEP within that construction scope. Organization: Concept slides plus standalone reference. Next attempts: Actual reader and transfer tests.');
await fs.mkdir(root+'/slides-build/rendered',{recursive:true});
for(let i=0;i<p.slides.items.length;i++){const slide=p.slides.items[i];const b=await p.export({slide,format:'png',scale:1});await fs.writeFile(root+`/slides-build/rendered/slide-${i+1}.png`,new Uint8Array(await b.arrayBuffer()));const l=await slide.export({format:'layout'});await fs.writeFile(root+`/slides-build/slide-${i+1}.layout.json`,await l.text());}
await (await PresentationFile.exportPptx(p)).save(root+'/representation-scope-specimen.pptx');
await fs.writeFile(root+'/slides-build/source-notes.txt','All logical content is a constructed local specimen from 012, 013, 023. WCAG 2.2 sources are in speaker notes. VDP supplies the explicit near-black/warm-white/one-accent design direction. No external imagery.');
const bp=Presentation.create({slideSize:{width:1280,height:720}});const bs=bp.slides.add();bs.background.fill=bg;text(bs,'Counterexamples refute universal claims.',72,64,1136,96,56,true);for(const [x,c] of [[352,'#427A64'],[752,'#A94F47']]){bs.shapes.add({geometry:'ellipse',position:{left:x,top:280,width:176,height:176},fill:c,line:{fill:ink,width:4}});}text(bs,'Green: improved. Red: did not improve.',72,568,1136,80,40,false);const bpng=await bp.export({slide:bs,format:'png',scale:1});await fs.writeFile(root+'/slides-build/color-only-baseline.png',new Uint8Array(await bpng.arrayBuffer()));
console.log('Created 5 slides and rendered each.');
}
main().catch(async e=>{await fs.writeFile("/workspace/scratch/78b838bd97fc/mind-change-research/representation/slides-build/error.txt",String(e.stack||e)); console.error(String(e.message||e));process.exitCode=1;});
