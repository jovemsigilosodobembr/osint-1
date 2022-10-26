
<h3><p align="center">
O conceito por trás do Seeker é simples, assim como hospedamos páginas de phishing para obter credenciais, por que não hospedar uma página falsa que solicita sua localização, como muitos sites populares baseados em localização!
    Seeker Hospeda um site falso que pede permissão de localização e se o alvo permitir, podemos obter:</h3>

Longitude
Latitude
Precisão
Altitude - Nem sempre disponível
Direção - Disponível apenas se o usuário estiver em movimento
Velocidade - Disponível apenas se o usuário estiver em movimento
    
Junto com as informações de localização, também obtemos **Informações do dispositivo** sem nenhuma permissão:

* ID exclusivo usando impressão digital em tela
* Modelo do dispositivo - nem sempre disponível
* Sistema operacional
* Plataforma
* Número de núcleos de CPU - Resultados aproximados
* Quantidade de RAM - Resultados Aproximados
* Resolução da tela
* Informações da GPU
* Nome e versão do navegador
* Endereço IP público
* Endereço IP local
* Porto Local

O reconhecimento automático de endereços IP é realizado após o recebimento das informações acima.

Esta ferramenta é uma prova de conceito e é apenas para fins educacionais, o Seeker mostra quais dados um site malicioso pode coletar sobre você e seus dispositivos e por que você não deve clicar em links aleatórios e permitir permissões críticas, como localização etc.

## Como isso é diferente do IP GeoLocation

* Outras ferramentas e serviços oferecem geolocalização IP que NÃO é exata e não fornece a localização do alvo, mas sim a localização aproximada do ISP.

* O Seeker usa a API HTML e obtém a Permissão de Localização e, em seguida, obtém a Longitude e a Latitude usando o Hardware GPS que está presente no dispositivo, então o Seeker funciona melhor com Smartphones, se o Hardware GPS não estiver presente, como em um Laptop, o Seeker faz fallbacks para IP Geolocalização ou procurará Coordenadas em Cache. 

* Geralmente, se um usuário aceitar a permissão de localização, a precisão das informações recebidas é **precisão de aproximadamente 30 metros**
* A precisão depende de vários fatores que você pode ou não controlar, como:
  * Dispositivo - Não funcionará em laptops ou telefones com GPS quebrado
  * Navegador - Alguns navegadores bloqueiam javascripts
  * Calibração do GPS - Se o GPS não estiver calibrado, você poderá obter resultados imprecisos e isso é muito comum
</p></h3>



<h3><p align="center">Modelos</p></h3>

* NearYou
* Google Drive (Suggested by @Akaal_no_one)
* WhatsApp (Suggested by @Dazmed707)
* Telegram
* Zoom (Made by @a7maadf)
* Google reCAPTCHA (Made by @MrEgyptian)


<h3><p align="center">Testado em:</p></h3>


* Kali Linux
* BlackArch Linux
* Ubuntu
* Kali Nethunter
* Termux
* Parrot OS
* OSX - Monterey v.12.0.1

 ```
git clone https://github.com/jovemsigilosodobembr/osint
cd osint/FERRAMENTAS/seeker/
chmod +x install.sh
./install.sh
 ```

 PARA NORMALMENTE
 ```
 cd osint/FERRAMENTAS/seeker/
 ```
 
 <h3><p align="center">Mais Informação embereve</p></h3>
