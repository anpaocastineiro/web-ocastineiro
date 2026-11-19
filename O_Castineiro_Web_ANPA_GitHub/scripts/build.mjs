import {readdir,readFile,writeFile,mkdir,cp,rm} from 'node:fs/promises';
import path from 'node:path';
const root=process.cwd(),out=path.join(root,'dist');
await rm(out,{recursive:true,force:true});await mkdir(out,{recursive:true});
for(const name of ['index.html','iniciativas.html'])await cp(path.join(root,name),path.join(out,name));
for(const folder of ['assets','admin'])await cp(path.join(root,folder),path.join(out,folder),{recursive:true});
async function readItems(folder){const dir=path.join(root,'content',folder);const files=(await readdir(dir)).filter(n=>n.endsWith('.json')).sort(),items=[];for(const file of files){const item=JSON.parse(await readFile(path.join(dir,file),'utf8'));if(item.publicado!==true)continue;item.id=file.replace(/\.json$/,'');items.push(item)}return items}
const items=await readItems('iniciativas');
items.sort((a,b)=>String(b.data||'').localeCompare(String(a.data||'')));
const novas=await readItems('novas'),axenda=await readItems('axenda');
novas.sort((a,b)=>String(b.data).localeCompare(String(a.data)));axenda.sort((a,b)=>String(a.data).localeCompare(String(b.data)));
await mkdir(path.join(out,'content'),{recursive:true});
await writeFile(path.join(out,'content','ideas.json'),JSON.stringify({items},null,2)+'\n');
await writeFile(path.join(out,'content','actualidade.json'),JSON.stringify({novas,axenda},null,2)+'\n');
console.log('Compilación rematada: '+items.length+' iniciativas, '+novas.length+' novas e '+axenda.length+' actividades.');
