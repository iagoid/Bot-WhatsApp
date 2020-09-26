# Bot para enviar mensagens no WhatsApp
Feito com base nesse vídeo https://www.youtube.com/watch?v=ISYHWfWvp3E


# Requisitos:
Python 3 -> https://www.python.org/downloads/
Selenium -> pip install selenium
Chromedriver da versão de Google que você utiliza -> https://chromedriver.chromium.org/downloads


# Explicações
Abra o seu WhatsApp e verifique onde estão os items abaixo e quais são seus identificadores

Local onde o bot tem de clicar para entrar no grupo/pessoa, é o nome do grupo ou pessoa(digite exatamente igual, seu identificador é o title)
<span dir="auto" title="teste" class="_3ko75 _5h6Y_ _3Whw5">teste</span>

Local onde está o campo do chat (identificado class)
<div tabindex="-1" class="_3uMse">

Local de envio(seta ao lado do chat)
<span data-testid="send" data-icon="send" class="">


# Como executar:
Cole a versão do chrome driver que você usa dentro dessa pasta
Mude o self.mensagem e o self.grupos do código para a mensagem que você quer enviar e para quais grupos/pessoas respectivamente
Vá até a pasta pelo cmd e digite: *py.exe zapbot.py*

Nesse momento ele irá abrir o Google Chrome, você deve se conectar ao escanear o QRCode e entrar no seu WhatsApp