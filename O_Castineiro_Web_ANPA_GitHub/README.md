# O Castiñeiro · web da ANPA

## Preparación para GitHub
Este ZIP é unha **versión reconstruída para a entrega manual** a partir da web local e dos cambios recentes de GitHub. Conserva a identidade gráfica, a portada sen sección de noticias, o taboleiro de iniciativas, o arquivo, o bloque «Faite socia» cos 15 € e o IBAN, e a estrutura de Decap CMS.

1. Extraer o ZIP; subir **o contido interior** ao repositorio privado `anpaocastineiro/web-ocastineiro` (rama `main`).
2. En Netlify, usar **Import from Git**, escoller ese repositorio e rama `main`. O ficheiro `netlify.toml` xa define o comando de compilación e o cartafol `dist`.
3. Comprobar portada, imaxes, iniciativas e «Faite socia».
4. Crear o sitio da ANPA en Decap Turbo (nova organización/repositorio/enderezo `/admin/`). Substituír `SUBSTITUIR_POLO_SITE_ID_DA_ANPA` en `admin/config.yml` polo Site ID real.
5. Non activar o formulario de alta ata dispoñer de política de privacidade, destino e procedemento de tratamento dos datos persoais. O formulario **está desactivado** expresamente.
6. Confirmar coa ANPA a periodicidade da cota de 15 € e o procedemento de validación de transferencias antes de comunicar altas.

A sección «Novas/Axenda» **non se mostra na portada**. Mantéñense as coleccións no CMS como material desactivado para un eventual uso futuro.

## Publicación manual como ZIP en Netlify
Este ZIP é principalmente para **subir ao GitHub**. Para publicación manual en Netlify, primeiro executar `node scripts/build.mjs` e subir o cartafol `dist`, non a raíz: a compilación é necesaria para xerar `/content/ideas.json`.
