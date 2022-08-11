# Agendador ePROC


## Agendador de intimações judiciais pendentes no ePROC ao Google Agenda
Esse programa foi criado com o intuito de efetuar o download de planilhas de intimações pendentes no ePROC, em ambos os estados - Santa Catarina e Paraná, tendo como data de ocorrência do evento a data limite para cumprimento de prazo das respectivas intimações.

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
python -m PyInstaller --onedir --windowed --icon=icone.ico --name="Agendador ePROC" agendador.py
``` 

> O parâmetro `--windowed` pode ser retirado caso ocorra algum problema, retirar o parâmetro mostrará o log de console do programa enquanto o mesmo estiver em execução, desta forma, possíveis mensagens de erro podem ser detectadas.
##


## Informações
* O arquivo de ícone - `icone.ico` está disponível no repositório, e pode ser realocado à pasta `./Agendador ePROC/dist/Agendador ePROC/`
* O arquivo que contém a imagem de fundo do programa `background.png` também pode ser movida à pasta `./Agendador ePROC/dist/Agendador ePROC/` e também está contida no repositório.
