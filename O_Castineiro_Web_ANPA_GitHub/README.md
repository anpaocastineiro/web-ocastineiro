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
