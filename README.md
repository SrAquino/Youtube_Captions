O que que esse programa faz?
- Dado um coleção de palavras do método PICO, o programa gera strings de buscas
- Baixa dois vídeo para cada string (ajustável)
- Extrai o audio e particiona (para que o google possa fazer uma transcrição)
- Gera uma transcrição do audio
- Faz screenshot a cada 10seg
- Gera uma descrição de cada screenshot
- Salva tudo no BD SQLite
- Normaliza os textos
- Vetoriza os textos
- Clusteriza as bases

(caso instancie dados no git que agora estão no .gitignore: 
> - git rm -r --cached . 
> - git add .
> - git commit -m "Atualiza o rastreamento de arquivos com base no .gitignore"
)

>> Recomendo que execute cada célula separadamente, pois como há thread, eventualmente a próxima célula inicia sem a ultima ter terminado, o que pode gerar erros

>> Também é interessante reiniciar o arquivo para cada céluna, eventualmente foi percebido problemas com a célula não finalizando o processo quando iniciadas em sequencia

