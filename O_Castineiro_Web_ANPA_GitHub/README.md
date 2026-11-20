# O Castiñeiro · web da ANPA

Web pública da asociación de familias do CEIP Eladia Mariño (Cabanas).

- **Web:** https://web-ocastineiro.netlify.app/
- **Administración (Decap CMS):** https://web-ocastineiro.netlify.app/admin/
- **Código:** https://github.com/anpaocastineiro/web-ocastineiro
- **Rama de publicación:** `main`
- **Carpeta raíz do proxecto:** `O_Castineiro_Web_ANPA_GitHub`

## Netlify
O `netlify.toml` da raíz do repositorio configura:
- Base: `O_Castineiro_Web_ANPA_GitHub`
- Comando: `node scripts/build.mjs`
- Publicación: `dist`

O script recompila os ficheiros públicos de iniciativas, transparencia e outras coleccións. Para despregar desde Git, Netlify debe estar conectado ao repositorio e rama indicados.

## Decap CMS
O panel está servido desde `admin/index.html` e usa o backend `turbo-github`.

**Aínda falta a autenticación externa:** crear un sitio na organización da ANPA en Decap Turbo, instalar a aplicación GitHub de Decap Turbo con acceso só a `anpaocastineiro/web-ocastineiro`, e substituír `SUBSTITUIR_POLO_SITE_ID_DA_ANPA` en `admin/config.yml` polo Site ID real. O ID non é un contrasinal. A aplicación **ChatGPT Codex Connector** non substitúe a de Decap Turbo.

Datos que hai que introducir no panel de Decap Turbo:
- Nome: `O Castiñeiro`
- Provedor: `GitHub`
- Repositorio: `anpaocastineiro/web-ocastineiro`
- Rama: `main`
- Ruta de configuración: `O_Castineiro_Web_ANPA_GitHub/admin/config.yml`
- Enderezo de administración: `https://web-ocastineiro.netlify.app/admin/`

Plan gratuíto de Turbo: 1 sitio e 1 persoa editora. A conta propietaria debería quedar baixo control da ANPA, non dunha conta persoal allea.

## Contidos editables
- **Ideas en marcha:** `content/iniciativas`, filtradas por `publicado: true`.
- **Información para participar:** `content/transparencia`, con actas e acordos, propostas e respostas, convocatorias, contas e orzamentos.
- **Novas e Axenda:** estruturas preparadas, actualmente non visibles na portada.

Os ficheiros novos gardados polo CMS en GitHub poden activar un novo despregamento desde `main`.

## Privacidade
**Este repositorio é público.** Mesmo os ficheiros cunha marca `publicado: false` son públicos en GitHub. Non gardar no CMS:
- Datos de altas de socias, nomes ou datos identificativos das crianzas.
- Mensaxes privadas das familias ou de menores.
- Actas completas sen autorización de publicación nin documentos financeiros reservados.

Revisar e anonimizar calquera texto ou PDF **antes** de incorporalo ao CMS. Os formularios de contacto e de alta están separados do repositorio e deberán comprobarse no panel de Netlify Forms, incluída a súa notificación ao correo da ANPA e a información legal.

## Manter e recuperar a web
O código e os contidos públicos están versionados no GitHub da ANPA. Se un cambio editorial causa un problema, pode revisarse ou reverterse no historial de commits; os contrasinais e identificadores de sesión nunca deben gardarse neste repositorio.

## Recepción de formularios en Netlify

A web dispón de tres formularios de uso ordinario: `alta-socias`, `propostas-familias` e `ideas-crianzas`. O cuarto, `atencion-familias` («Falamos en privado»), **está habilitado na web** unicamente para solicitar datos mínimos de contacto, sen un campo de mensaxe libre. Recoméndase aprobar o protocolo de atención e limitar os permisos de acceso antes de atender casos reais.

**Configuración necesaria no panel de Netlify (non se pode facer só desde GitHub):**

1. Abrir o proxecto `web-ocastineiro` en Netlify → **Forms** → **Enable form detection** (se aínda non está activada).
2. Facer un novo **deploy** desde a rama `main` despois de activar a detección. O ficheiro `__forms.html` inclúese en `dist` e contén os tres esquemas estáticos que Netlify debe detectar.
3. Comprobar que en **Forms → Active forms** aparecen os formularios detectados, incluído `atencion-familias` cando Netlify o procese; a detección por si soa non significa que o formulario estea aberto ao público.
4. En **Forms → Submission notifications**, engadir unha **Email notification** para todos os formularios, co destino `anpa.o.castineiro@gmail.com`. Os asuntos están definidos no HTML mediante un campo oculto `subject`, e teñen prioridade sobre un asunto configurado no panel de Netlify.
5. Se Netlify envía un correo de confirmación ao destinatario, abrilo desde a conta da ANPA e confirmar a notificación.
6. Probar cada formulario con datos ficticios e comprobar a chegada á sección Forms e ao Gmail da ANPA; revisar a bandexa de spam de Netlify se faltan probas.

**Implementación:** o ficheiro `__forms.html` define os nomes de todos os campos. A web envía por POST a `/__forms.html` coa codificación `application/x-www-form-urlencoded` e o campo `form-name`. Non introducir tokens de Gmail no código nin conectar a caixa de correo ao repositorio.

**Privacidade:** as respostas son datos de contacto privados. Non incluílas no repositorio público, no CMS nin nos logs de compilación. A asociación debe confirmar a información de protección de datos, os permisos de acceso a Netlify e os períodos de conservación antes de recibir solicitudes reais.

> Recompilación solicitada o 19/11/2026 tras activar a detección de formularios en Netlify. Non modifica o deseño nin os datos da web.


## Falamos en privado · preparación e activación
A portada inclúe a sección `#falamos-en-privado` e unha ligazón desde Participa. A finalidade é **pedir un contacto privado**, non recibir relatos de incidencias ou datos sensibles. O formulario `atencion-familias` está definido en `__forms.html` para a detección de Netlify e está habilitado na portada.

**Tarefas de configuración e funcionamento:**
1. Aprobar o protocolo de atención ás familias e designar as persoas que recibirán solicitudes e as substitutas en caso de conflito de intereses.
2. Validar a información legal de `privacidade.html`: finalidade, base xurídica, acceso, terceiros provedores, prazos de conservación e exercicio de dereitos.
3. Revisar os permisos de Netlify Forms e a conta de Gmail; non reenviar automaticamente solicitudes a persoas non autorizadas.
4. En Netlify → Forms → Submission notifications, crear/verificar unha notificación **específica do formulario `atencion-familias`** a `anpa.o.castineiro@gmail.com`. Este paso require acceso ao panel de Netlify; un commit en GitHub non o configura.
5. A sección xa está habilitada na interface; comprobar que o novo deploy inclúe este cambio e probar o envío só con datos ficticios.
6. Comprobar que o formulario chega a Netlify Forms e ao Gmail autorizado. Non empregar casos reais para as probas.

**Seguridade:** non incorporar unha caixa de mensaxe libre, non gardar información de familias en GitHub e non publicar os envíos en Decap CMS.


## Identificación de formularios no correo da ANPA
Cada envío leva un asunto específico (establecido nos formularios HTML, non modificable mediante a configuración xeral do panel):
- `alta-socias`: **[WEB ANPA] Alta de socia**
- `propostas-familias` ao usar «Tes unha idea?»: **[WEB ANPA] Proposta dunha familia**
- `propostas-familias` ao usar «Propoñer un tema para un encontro»: **[WEB ANPA] Tema para encontro**
- `ideas-crianzas`: **[WEB ANPA] Idea das crianzas**
- `atencion-familias`: **[WEB ANPA] Conversa privada**

Estes asuntos serven para identificar a orixe no Gmail da ANPA e crear filtros de Gmail por `subject:`; **os filtros non se crean automaticamente con este código**. Non alterar o campo `subject` sen actualizar tamén o esquema estático en `__forms.html` e volver despregar.

Hai un acceso directo a `#falamos-en-privado` no menú principal e, en pantalla pequena, dentro do menú despregable. As solicitudes privadas só recollen datos de contacto, sen relato libre.


## Bota unha man · tarefas concretas
Desde `/admin/` → **Bota unha man · axudas concretas** pódense engadir, editar e pechar peticións de colaboración: título, descrición, tempo estimado, data e lugar opcionais.
- Só aparecen na web tarefas con `publicado: true` e `estado: aberta`. Cambiar a `cuberta` ou `pechada` retíraas no seguinte despregamento.
- Por defecto non hai tarefas públicas inventadas. Pódese ofrecer colaboración espontánea cun formulario breve.
- Os envíos van polo formulario xa existente `propostas-familias`, co asunto `[WEB ANPA] Bota unha man`; non é necesario configurar unha nova notificación de Netlify.
- **GitHub é público**, incluso os borradores: nunca introducir datos identificativos de familias, menores ou persoas voluntarias nas tarefas do CMS.
