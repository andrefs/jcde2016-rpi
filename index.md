---
title: JCDE 2016 -- Raspberry Pi
layout: default
---

# O que é a Raspberry Pi?

A Raspberry Pi é um minicomputador que se caracteriza pelo seu baixo custo e tamanho reduzido.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Raspberry_Pi_3_Model_B.png/450px-Raspberry_Pi_3_Model_B.png" alt="Raspberry Pi 3 Modelo B" align="right" />

A ideia inicial surgiu por volta de 2006 na Universidade de Cambridge, quando se detetou que os estudantes que frequentavam as primeiras cadeiras de ciências da computação tinham cada vez menos conhecimentos prévios de programação: se nos anos 90 era comum a maior parte dos alunos programarem nos tempos livres, nos anos 2000 o candidato típico tinha feito apenas um pouco de _web design_.

Foram identificadas várias causas para este problema, entre os quais a substituição dos _Amigas_, _BBC Micros_, _Spectrum ZX_ e _Commodore 64_ (as máquinas em que as pessoas de gerações anteriores tipicamente aprendiam a programar) pelos modernos PCs e consolas de jogos.

Deu-se então início à conceçao e desenvolvimento de um computador barato e de tamanho reduzido, que pudesse ser usado e abusado por crianças sem os receios que surgiriam num computador doméstico tradicional, de custo mais elevado.

Por volta de 2008, os avanços tecnológicos na produção de processadores para dispositivos móveis tornaram-nos suficientemente potentes para suportarem multimédia com boa qualidade, o que permitiria desenvolver um computador atrativo mesmo para crianças que inicialmente não estivessem interessadas numa máquina puramente orientada para a programação. Foi então fundada a _Raspberry Pi Foundation_, e o primeiro modelo lançado em 2012. Em 2013 atingiu-se a marca dos 2.000.000 de unidades vendidas.

# Que modelos existem?

Desde a primeira versão lançada em 2012, outros modelos têm sido criados. Atualmente, estão disponíveis:

* **Pi 1 Modelo A+** (versão _low cost_ da Raspberry Pi com 256MB de RAM, 1 porta USB)
* **Pi 1 Modelo B+** (revisão final da Raspberry Pi original com 512MB de RAM, 4 portas USB, 1 porta ethernet)
* **Pi 2 Modelo B** (similar à Pi 1 Modelo B+, mas com processador 900MHz quad-core ARM Cortex-A7 e 1GB de RAM)
* **Pi 3 Modelo B** (processador 1.2GHz 64-bit quad-core ARM Cortex-A53, 1GB de RAM, wireless e bluetooth integrados)
* **Pi Zero** (metade do tamanho do modelo A+, processador single-core 1Ghz, 512MB de RAM e portas mini-[HDMI](#HDMI) e USB) -- *ESGOTADO*

# Primeiros passos

Para começar a trabalhar com a Raspberry Pi, é primeiro necessário seguir os seguintes passos:

1. Formatar um cartão SD ([instruções](https://www.raspberrypi.org/documentation/installation/sdxc_formatting.md)). Em Windows, em vez de fazer a formatação com as ferramentas do sistema, é aconselhado que se use antes uma aplicação como o [FAT32 Format](http://www.ridgecrop.demon.co.uk/guiformat.htm).
1. Descarregar o NOOBS [aqui](http://www.raspberrypi.org/downloads/). O NOOBS é um gestor de instalação de sistemas operativos (OS), que permite facilmente escolher o OS a usar na Pi. Depois de descarregar, extrair os ficheiros para o cartão SD ([instruções](https://www.raspberrypi.org/help/noobs-setup/)).
1. Ligar os periféricos à Pi (teclado, rato, monitor, cabo de rede, ...) e ligar a Pi à alimentação (cabo micro-USB). ![Ligações básicas da Raspberry Pi. Source: https://leanpub.com/RPiMRE](https://leanpub.com/site_images/RPiMRE/board-04.png)
1. Na primeira utilização, escolher o sistema operativo (na dúvida, instalar o Raspbian).
1. Depois de a Pi iniciar, ligar a Pi à [breadboard](#breadboard).

  * [Ligações internas de uma breadboard](images/breadboard.png)
  * [Códigos de cores das resistências](images/resistors.jpg)
  * [Esquema do GPIO](images/gpio.png)


# Onde comprar

## Em Portugal

* **BotNRoll**
  * [www.botnroll.com](http://www.botnroll.com)
  * 253 554 214
  * Rua Teixeira de Pascoais nº136, Azurém, 4800-023 Guimarães
* **PtRobotics**
  * [www.ptrobotics.com](http://www.ptrobotics.com)
  * geral@ptrobotics.com
* **ClickPlus**
  * [www.clickplus.pt](http://www.clickplus.pt)
  * info@clickplus.pt
* **GlobalData**
  * [www.globaldata.pt](http://www.globaldata.pt)
  * 222 011 151
  * Rua de Gonçalo Cristóvão, 132, 4000-264 Porto


## Internacional

* [eud.dx.com](http://eud.dx.com)
* [www.adafruit.com](http://www.adafruit.com)
* [www.sparkfun.com](http://www.sparkfun.com)
* [shop.cyntech.co.uk](http://shop.cyntech.co.uk)

# Acessórios

Para trabalhar com um Raspberry Pi são geralmente precisos vários periféricos: monitor, rato, teclado.

Existe também uma grande quantidade de outros acessórios disponíveis para os vários modelos da Raspberry Pi. Por exemplo, geralmente é boa ideia arranjar uma caixa que proteja a Raspberry Pi, e existem várias disponíveis, como [esta](https://www.raspberrypi.org/products/raspberry-pi-case/), [esta](https://www.adafruit.com/products/1326) ou [esta](http://www.dx.com/p/protective-case-w-camera-hole-for-raspberry-pi-red-431734). Outros exemplos de acessórios são:

* _dongle WiFi_
* câmara de vídeo
* cartão SD
* ...

Para projetos de eletrónica também é conveniente comprar componentes como resistências, LEDs, sensores, motores, _jumper wires_ (fios de ligação), etc, que frequentemente são disponibilizados em kits ([exemplo](http://www.dx.com/p/t-type-expansion-board-breadboard-kit-for-raspberry-pi-b-multicolored-359606)).


# Lista de livros

* 


# Projectos similares

* [Tessel](https://tessel.io/)
* [BeagleBone](http://beagleboard.org/bone)
* [Banana Pi](http://www.bananapi.org/)


* [Arduino](https://www.arduino.cc/)



# Glossário

* <a name="HDMI">**HDMI**</a>: *High-Definition Multimedia Interface* (HDMI) é uma interface condutiva totalmente digital de áudio e vídeo capaz de transmitir dados não comprimidos (...) -- *fonte: [Wikipedia](https://pt.wikipedia.org/wiki/High-Definition_Multimedia_Interface)*
* <a name="breadboard">**breadboard**</a>: (...) é uma placa com furos (ou orifícios) e conexões condutoras para montagem de circuitos elétricos experimentais. -- *fonte: [Wikipedia](https://pt.wikipedia.org/wiki/Placa_de_Ensaio)*

# Links úteis

* [Ligações detalhadas da Raspberry Pi](http://images.coolestech.com/uploads/2013/06/Untitled.jpg) *([fonte](http://www.coolestech.com))*


# Contactos

* andrefs [at] andrefs [dot] com
* luispsantos [at] sapo [dot] pt

