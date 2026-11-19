# Publicación da sección «Información para participar»

Aquí Decap CMS gardará unha entrada JSON por publicación. As catro categorías son: actas, propostas, convocatorias e contas.

IMPORTANTE: este repositorio de GitHub é PÚBLICO. Incluso as entradas co campo `publicado: false` e os documentos subidos a `assets/uploads` son accesibles desde GitHub. Non introducir borradores confidenciais, nomes ou datos identificativos de crianzas, contactos de familias, documentos bancarios internos nin actas sen revisar.

`publicado: false` só impide que o compilador mostre a entrada na web; NON crea un espazo privado.

Procedemento recomendado: revisar e anonimizar o documento fóra de GitHub, obter a autorización de publicación que corresponda, crear a entrada no CMS e marcar «Publicar na web» cando estea lista. Ao gardar o CMS no repositorio, Netlify recompilará a páxina se a conexión de despregamento está activa.

Formato: ficheiros .json, un por publicación. Campos: titulo, categoria, data, resumo, contido, estado (opcional), resposta (opcional), documento (opcional), ligazon (opcional), publicado.
