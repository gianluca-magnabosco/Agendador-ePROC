# Agendador ePROC


## Agendador de intimações judiciais pendentes no ePROC ao Google Agenda
Esse programa foi criado com o intuito de efetuar o download de planilhas de intimações pendentes no ePROC, em ambos os estados - Santa Catarina e Paraná, e adicioná-los à eventos do Google Agenda (Google Calendar), tendo como data de ocorrência do evento a data limite para cumprimento de prazo das respectivas intimações.


![Agendador ePROC](https://cdn.discordapp.com/attachments/810687915045814293/934955120821682206/3aebb01f4ab9edab8d093e0b6188ac35.png)
## 
</br >

## Instruções
O programa foi feito para uso com o navegador Google Chrome, porém sintam-se a vontade para alterar o código para compatibilidade com outros navegadores. </br >

```java
Para que o programa funcione, o arquivo de driver de navegador "chromedriver.exe" deve estar dentro da pasta:

"./Agendador ePROC/dist/Agendador ePROC/"
``` 

</br >


O script já foi instalado como programa e depositado nesse repositório, porém caso tenha problema com a versão disponível no repositório, o recomendado é instalar o programa utilizando o `PyInstaller` com a linha de comando já explicitada no código e que segue:
```python
python -m PyInstaller --onedir --windowed --icon=icone.ico --name="Agendador ePROC" Agendador.py
``` 
> É necessário mudar o nome do script contido nesse repositório para `Agendador.py`

> O parâmetro `--windowed` pode ser retirado caso ocorra algum problema, retirar o parâmetro mostrará o log de console do programa enquanto o mesmo estiver em execução, desta forma, possíveis mensagens de erro podem ser detectadas.
##

Ao baixar ou instalar o programa, é necessário, antes de executá-lo, criar um projeto na Google Cloud Platform, que pode ser realizado no link abaixo:
### <https://console.cloud.google.com/>

### Após criar ou logar em sua conta do Google, crie um projeto para o programa:
![eproc1](https://media.discordapp.net/attachments/810687915045814293/935418466641543208/eproc_1.png)

</br >

### Ative a biblioteca do Google Calendar API:
<div>
  
  ![eproc8](https://media.discordapp.net/attachments/810687915045814293/935422903497932910/eproc_8.png)
  
  ![eproc9](https://media.discordapp.net/attachments/810687915045814293/935422913648148540/eproc_9.png)
  
  ![eproc10](https://media.discordapp.net/attachments/810687915045814293/935422921755738142/eproc_10.png)
  
  ![eproc11](https://media.discordapp.net/attachments/810687915045814293/935422928785399858/eproc_11.png)
</div>

</br >

### Configure a tela de consentimento:
<div>
  
  ![eproc2](https://media.discordapp.net/attachments/810687915045814293/935418476418433025/eproc_2.png)

  ![eproc3](https://media.discordapp.net/attachments/810687915045814293/935418484739952660/eproc_3.png)

</div>

</br >

### Crie uma chave de autenticação OAuth, e baixe o json da mesma:
<div>
  
  ![eproc4](https://media.discordapp.net/attachments/555940526554218496/935528342403305552/eproc_4.png)

  ![eproc5](https://media.discordapp.net/attachments/810687915045814293/935418523969257522/eproc_5.png)

  ![eproc6](https://media.discordapp.net/attachments/810687915045814293/935418532739559444/eproc_6.png?width=1200&height=476)
  
  ![eproc7](https://media.discordapp.net/attachments/810687915045814293/935418548501766144/eproc_7.png)
</div>


> Renomeie o arquivo baixado para _`client_secret.json`_ e coloque na pasta `./Agendador ePROC/dist/Agendador ePROC/`
## 
</br >

## Informações
* O arquivo de ícone - `icone.ico` está disponível no repositório, e pode ser realocado à pasta `./Agendador ePROC/dist/Agendador ePROC/`
* O arquivo que contém a imagem de fundo do programa `background.png` também pode ser movida à pasta `./Agendador ePROC/dist/Agendador ePROC/` e também está contida no repositório.
