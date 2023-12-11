### Retrospektiivi


Käytimme retrospektiivissa Start, Stop, Continue, More of, Less of Wheel -tapaa.


Start- ja Stop-osiot olivat molemmat tyhjiä, sillä meistä tuntui että kolmannessa sprintissä olimme jo hyvin älynneet, 
että mitä kannattaa tehdä ja mitä ei. Työskentely oli muutenkin sujunut kaikille mieluisalla tavalla, ja saimme hyvin
töitä aikaiseksi.


Continue-osiossa oli:
- Kommunikaatio. Meidän kaikkien mielestä kommunikaatiomme toimi hyvin koko sprintin ajan.
- Hyvälaatuinen koodi. Vaikka osa commiteistamme ei saanut passing-statusta yhden pahalaatuisen merge-errorin takia, 
mielestämme ainakin koodin laatutaso on pysynyt sprintin aikana korkealla.


More of -osiossa oli:
- Testit toimimaan ennen pushia. Pahan merge-errorin takia, jota ei huomattu ajoissa, osa commiteistamme ei päässyt CI-palvelun 
testien läpi. Suurin osa commiteista oli kuitenkin testattu ennen pushaamista.
- Ei tehdä työtä jota sprintissä ei vaadita. Tässä sprintissä olimme oppineet tehdä täsmällisesti mitä vaadittiin, emmekä
tehneet turhaa työtä, esimerkiksi jotain mitä asiakas ei vaatinut tai turhan monimutkaista koodia vain ulkonäön takia.


Less of -osiossa oli:
- Vähemmän epäonnistuineita committeja. Kerroin jo pahasta merge-errorista, joka poisti tärkeitä tiedostoja.


### Kehitystoimenpiteet:


- Testataan että testit menevät läpi ennen git commit tai git push komentoja.
