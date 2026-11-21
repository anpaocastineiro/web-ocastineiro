import {readdir,readFile,writeFile,mkdir,cp,rm} from 'node:fs/promises';
import path from 'node:path';
const root=process.cwd(),out=path.join(root,'dist');
await rm(out,{recursive:true,force:true});await mkdir(out,{recursive:true});
for(const name of ['index.html','iniciativas.html','privacidade.html','__forms.html'])await cp(path.join(root,name),path.join(out,name));
for(const folder of ['assets','admin'])await cp(path.join(root,folder),path.join(out,folder),{recursive:true});
async function readItems(folder){const dir=path.join(root,'content',folder);const files=(await readdir(dir)).filter(n=>n.endsWith('.json')).sort(),items=[];for(const file of files){const item=JSON.parse(await readFile(path.join(dir,file),'utf8'));if(item.publicado!==true)continue;item.id=file.replace(/\.json$/,'');items.push(item)}return items}
// Conservar só unha mostra ficticia por estado, sen confundir as demais coas propostas reais.
const exemplosVisibles=new Set([
  'espazos-de-sombra-no-patio',
  'convivencia-e-metodoloxias',
  'espazo-de-intercambio-de-libros',
  'exemplo-caixa-de-material-escolar'
]);
const items=(await readItems('iniciativas')).filter(item=>item.exemplo!==true||exemplosVisibles.has(item.id));
items.sort((a,b)=>String(b.data||'').localeCompare(String(a.data||'')));
const novas=await readItems('novas'),axenda=await readItems('axenda');
novas.sort((a,b)=>String(b.data).localeCompare(String(a.data)));axenda.sort((a,b)=>String(a.data).localeCompare(String(b.data)));
await mkdir(path.join(out,'content'),{recursive:true});
await writeFile(path.join(out,'content','ideas.json'),JSON.stringify({items},null,2)+'\n');
await writeFile(path.join(out,'content','actualidade.json'),JSON.stringify({novas,axenda},null,2)+'\n');
const axudas=(await readItems('axudas')).filter(x=>x.estado==='aberta'&&typeof x.titulo==='string'&&x.titulo.trim());
axudas.sort((a,b)=>String(a.data||'9999').localeCompare(String(b.data||'9999')));
await writeFile(path.join(out,'content','axudas.json'),JSON.stringify({items:axudas.map(({titulo,tipo,descripcion,detalle,tempo,data,hora,hora_fin,lugar,persoas,material,data_confirmada,imaxe,imaxe_alt})=>({titulo,tipo:['actividade_puntual','chamada_colaboracion','iniciativa','encontro','outra'].includes(tipo)?tipo:'chamada_colaboracion',descripcion,detalle:typeof detalle==='string'?detalle:'',tempo,data,data_confirmada:data_confirmada===true,persoas:typeof persoas==='string'?persoas:'',material:typeof material==='string'?material:'',hora:typeof hora==='string'?hora.trim():'',hora_fin:typeof hora_fin==='string'?hora_fin.trim():'',lugar,imaxe:typeof imaxe==='string'&&imaxe.startsWith('/assets/uploads/')&&!imaxe.includes('../')&&!imaxe.includes('\\')&&/\.(?:jpe?g|png|webp|gif)$/i.test(imaxe)?imaxe:'',imaxe_alt:typeof imaxe_alt==='string'?imaxe_alt:'',estado:'aberta',publicado:true}))},null,2)+'\n');
const categoriasTransparencia=new Set(['estatutos','actas','contas']);
const transparencia=(await readItems('transparencia')).filter(x=>categoriasTransparencia.has(x.categoria)&&typeof x.titulo==='string');
transparencia.sort((a,b)=>String(b.data||'').localeCompare(String(a.data||'')));
await writeFile(path.join(out,'content','transparencia.json'),JSON.stringify({items:transparencia.map(({titulo,categoria,data,resumo,contido,estado,resposta,documento,ligazon})=>({titulo,categoria,data,resumo,contido,estado,resposta,documento,ligazon}))},null,2)+'\n');
console.log('Compilación rematada: '+items.length+' iniciativas, '+novas.length+' novas, '+axenda.length+' actividades e '+transparencia.length+' publicacións de transparencia.');
