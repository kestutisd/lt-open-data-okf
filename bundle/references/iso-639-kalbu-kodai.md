---
type: Reference
title: "ISO 639 kalbų kodai (ISO 639-1 / ISO 639-2 ir ES NAL ISO 639-3 poaibis)"
description: "ISO 639-1 (alpha-2), ISO 639-2 (alpha-3), ES leidinių biuro kalbų autoritetinės lentelės (NAL) įrašų ir specialiųjų žymų (zxx, und, mul, mis) klasifikatorius (731 įrašas)."
resource: "http://publications.europa.eu/resource/authority/language"
tags: [standards, iso-639, language-codes, kalbu-kodai, reference]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: std-iso639
    resource: "http://publications.europa.eu/resource/authority/language"
    title: "EU Publications Office — Language Authority Table (NAL)"
    author: "team:eu-publications-office"
    last_modified: "2026-09-23T00:00:00Z"
  - id: std-iso639-csv
    resource: "https://github.com/datasets/language-codes"
    title: "DataHub / ISO 639-2 Registration Authority — language-codes-full.csv (ODC-PDDL-1.0)"
    author: "team:frictionless-datasets"
---

# ISO 639 kalbų kodų klasifikatorius (ISO 639-1 / ISO 639-2 ir ES NAL ISO 639-3 poaibis)

Šis informacinis konceptas (`type: Reference`) apjungia **731 įrašas**: visus **ISO 639-1** (`alpha-2`) ir **ISO 639-2/B / 639-2/T** (`alpha-3`) kalbų kodus iš atvirojo `https://github.com/datasets/language-codes` rinkinio (`ODC-PDDL-1.0`), Europos Sąjungos leidinių biuro (*Publications Office of the European Union*) `language` autoritetinės lentelės (`http://publications.europa.eu/resource/authority/language`) įrašus su lietuviškais pavadinimais bei atitinkamas **ISO 639-3** žymas ir specialiuosius kodus `zxx`, `und`, `mul`, `mis`.[^std-iso639][^std-iso639-csv]

> **Aprėpties pastaba dėl ISO 639-3:** Pilnas **ISO 639-3** standartas apima ~7 900 individualių ir makrokalbų kodų; žemiau esančioje lentelėje pateikiamas praktinis poaibis (visi ISO 639-1 ir ISO 639-2 kodai bei ES leidinių biuro lietuviškais terminais aprašytos kalbos), o ne visas ~7 900 kalbų katalogas.[^std-iso639][^std-iso639-csv]

## Specialieji ISO 639-2 / ISO 639-3 kodai (būtina atskirti filtruojant duomenis)

Lietuvos atvirų duomenų rinkiniuose (pvz., archyvų, bibliotekų, švietimo, registrų ir publikacijų lentelėse) greta įprastų kalbų kodų (`lt` / `lit`, `en` / `eng`, `pl` / `pol`, `ru` / `rus`) naudojami 4 specialieji standartiniai kodai:[^std-iso639][^std-iso639-csv]

| ISO 639-2 / 639-3 kodas | ES autoritetinis kodas | Lietuviškas pavadinimas | Angliškas pavadinimas | Semantinė prasmė duomenų rinkiniuose |
| --- | --- | --- | --- | --- |
| `zxx` | `ZXX` | kalbinio turinio nėra | No linguistic content; Not applicable | Įraše nėra teksto jokia kalba (pvz., tik skaitiniai duomenys, natos, nuotraukos, instrumentinė muzika). |
| `und` | `UND` | nenustatyta kalba | Undetermined | Kalba egzistuoja, bet šaltinyje nenustatyta arba neįvardyta. |
| `mul` | `MUL` | kelios kalbos | Multiple languages | Dokumentas ar įrašas pateiktas keliomis kalbomis vienu metu. |
| `mis` | `MIS` | nekoduota kalba | Uncoded languages | Kalba, kuriai dar nesuteiktas atskiras ISO 639 kodas. |

## Spinta DSA kalbinių stulpelių taisyklės

- **Stulpelio pavadinimo sufiksas `@<iso639-1>`:** Spinta DSA specifikacijoje `text` tipo stulpeliai gali turėti dviejų raidžių ISO 639-1 kalbos žymą (`lang: en` vertimų eilutės arba `pavadinimas@lt`, `name@en`).[^std-iso639]
- **Kalbos kodo stulpeliai (`kalba`, `kalbos_kodas`, `lang`, `language`):** Priklausomai nuo rinkinio brandos ir šaltinio, reikšmės saugomos 2 raidžių (`lt`, `en`) arba 3 raidžių (`lit`, `eng`, `zxx`, `und`, `mul`, `mis`) formatu.[^std-iso639]

## ISO 639-1 / ISO 639-2 ir ES NAL kalbų kodų lentelė (731 įrašas)

> **Pastaba:** Stulpelyje *Pavadinimas ES NAL (LT)* pateikiami tik tie lietuviški terminai, kurie oficialiai paskelbti ES leidinių biuro `language` autoritetinėje lentelėje (`—` žymi ISO 639-2 kalbas iš `datasets/language-codes`, kurioms ES NAL lietuviško ekvivalento nepateikia).[^std-iso639][^std-iso639-csv]

| Kodas | ISO 639-1 | ISO 639-2/B | ISO 639-2/T | ISO 639-3 | Pavadinimas ES NAL (LT) | Title (EN) |
| --- | --- | --- | --- | --- | --- | --- |
| `AAR` | `aa` | `aar` | `aar` | `aar` | — | Afar |
| `ABK` | `ab` | `abk` | `abk` | `abk` | — | Abkhazian |
| `ACE` | `—` | `ace` | `ace` | `ace` | — | Achinese |
| `ACH` | `—` | `ach` | `ach` | `ach` | — | Acoli |
| `ADA` | `—` | `ada` | `ada` | `ada` | — | Adangme |
| `ADS` | `—` | `—` | `—` | `ads` | Adamorobo gestų kalba | Adamorobe Sign Language |
| `ADY` | `—` | `ady` | `ady` | `ady` | adigėjų | Adyghe |
| `AED` | `—` | `—` | `—` | `aed` | argentiniečių gestų kalba | Argentine Sign Language |
| `AEN` | `—` | `—` | `—` | `aen` | armėnų gestų kalba | Armenian Sign Language |
| `AFA` | `—` | `afa` | `afa` | `afa` | — | Afro-Asiatic languages |
| `AFG` | `—` | `—` | `—` | `afg` | afganistaniečių gestų kalba | Afghan Sign Language |
| `AFH` | `—` | `afh` | `afh` | `afh` | — | Afrihili |
| `AFR` | `af` | `afr` | `afr` | `afr` | afrikanų | Afrikaans |
| `AIN` | `—` | `ain` | `ain` | `ain` | — | Ainu |
| `AIQ` | `—` | `—` | `—` | `aiq` | aimakų | Aimaq |
| `AKA` | `ak` | `aka` | `aka` | `aka` | akanų | Akan |
| `AKK` | `—` | `akk` | `akk` | `akk` | — | Akkadian |
| `ALE` | `—` | `ale` | `ale` | `ale` | — | Aleut |
| `ALG` | `—` | `alg` | `alg` | `alg` | — | Algonquian languages |
| `ALT` | `—` | `alt` | `alt` | `alt` | — | Southern Altai |
| `AMH` | `am` | `amh` | `amh` | `amh` | amharų | Amharic |
| `ANG` | `—` | `ang` | `ang` | `ang` | — | English, Old (ca.450-1100) |
| `ANP` | `—` | `anp` | `anp` | `anp` | — | Angika |
| `APA` | `—` | `apa` | `apa` | `apa` | — | Apache languages |
| `APC` | `—` | `—` | `—` | `apc` | Levanto arabų | Levantine Arabic |
| `ARA` | `ar` | `ara` | `ara` | `ara` | arabų kalba | Arabic |
| `ARC` | `—` | `arc` | `arc` | `arc` | — | Official Aramaic (700-300 BCE); Imperial Aramaic (700-300 BCE) |
| `ARG` | `an` | `arg` | `arg` | `arg` | — | Aragonese |
| `ARN` | `—` | `arn` | `arn` | `arn` | — | Mapudungun; Mapuche |
| `ARO` | `—` | `—` | `—` | `aro` | araonų | Araona |
| `ARP` | `—` | `arp` | `arp` | `arp` | — | Arapaho |
| `ART` | `—` | `art` | `art` | `art` | — | Artificial languages |
| `ARW` | `—` | `arw` | `arw` | `arw` | — | Arawak |
| `ASE` | `—` | `—` | `—` | `ase` | amerikiečių gestų kalba | American Sign Language |
| `ASF` | `—` | `—` | `—` | `asf` | australų gestų kalba | Auslan |
| `ASM` | `as` | `asm` | `asm` | `asm` | — | Assamese |
| `ASP` | `—` | `—` | `—` | `asp` | alžyriečių gestų kalba | Algerian Sign Language |
| `ASQ` | `—` | `—` | `—` | `asq` | austrų gestų kalba | Austrian Sign Language |
| `AST` | `—` | `ast` | `ast` | `ast` | — | Asturian; Bable; Leonese; Asturleonese |
| `ASW` | `—` | `—` | `—` | `asw` | Australijos aborigenų gestų kalba | Australian Aborigines Sign Language |
| `ATH` | `—` | `ath` | `ath` | `ath` | — | Athapascan languages |
| `AUS` | `—` | `aus` | `aus` | `aus` | — | Australian languages |
| `AVA` | `av` | `ava` | `ava` | `ava` | — | Avaric |
| `AVE` | `ae` | `ave` | `ave` | `ave` | — | Avestan |
| `AWA` | `—` | `awa` | `awa` | `awa` | — | Awadhi |
| `AYM` | `ay` | `aym` | `aym` | `aym` | aimarų | Aymara |
| `AYO` | `—` | `—` | `—` | `ayo` | ajorėjų | Ayoreo |
| `AZE` | `az` | `aze` | `aze` | `aze` | azerbaidžaniečių kalba | Azerbaijani |
| `BAD` | `—` | `bad` | `bad` | `bad` | — | Banda languages |
| `BAI` | `—` | `bai` | `bai` | `bai` | — | Bamileke languages |
| `BAK` | `ba` | `bak` | `bak` | `bak` | — | Bashkir |
| `BAL` | `—` | `bal` | `bal` | `bal` | — | Baluchi |
| `BAM` | `bm` | `bam` | `bam` | `bam` | bambarų kalba | Bambara |
| `BAN` | `—` | `ban` | `ban` | `ban` | — | Balinese |
| `BAS` | `—` | `bas` | `bas` | `bas` | — | Basa |
| `BAT` | `—` | `bat` | `bat` | `bat` | — | Baltic languages |
| `BEJ` | `—` | `bej` | `bej` | `bej` | — | Beja; Bedawiyet |
| `BEL` | `be` | `bel` | `bel` | `bel` | baltarusių kalba | Belarusian |
| `BEM` | `—` | `bem` | `bem` | `bem` | — | Bemba |
| `BEN` | `bn` | `ben` | `ben` | `ben` | bengalų kalba | Bengali |
| `BER` | `—` | `ber` | `ber` | `ber` | — | Berber languages |
| `BFI` | `—` | `—` | `—` | `bfi` | britų gestų kalba | British Sign Language |
| `BFK` | `—` | `—` | `—` | `bfk` | Ban Khoro gestų kalba | Ban Khor Sign Language |
| `BHO` | `—` | `bho` | `bho` | `bho` | — | Bhojpuri |
| `BIH` | `—` | `bih` | `bih` | `bih` | — | Bihari languages |
| `BIK` | `—` | `bik` | `bik` | `bik` | — | Bikol |
| `BIN` | `—` | `bin` | `bin` | `bin` | — | Bini; Edo |
| `BIS` | `bi` | `bis` | `bis` | `bis` | bislama | Bislama |
| `BJM` | `—` | `—` | `—` | `bjm` | badželanių | Bajelani |
| `BLA` | `—` | `bla` | `bla` | `bla` | — | Siksika |
| `BNT` | `—` | `bnt` | `bnt` | `bnt` | — | Bantu languages |
| `BOD` | `bo` | `tib` | `bod` | `bod` | tibetiečių kalba | Tibetan |
| `BOF` | `—` | `—` | `—` | `bof` | bolonų | Bolon |
| `BOG` | `—` | `—` | `—` | `bog` | Bamako gestų kalba | Bamako Sign Language |
| `BOS` | `bs` | `bos` | `bos` | `bos` | bosnių kalba | Bosnian |
| `BQN` | `—` | `—` | `—` | `bqn` | bulgarų gestų kalba | Bulgarian Sign Language |
| `BQY` | `—` | `—` | `—` | `bqy` | Benkulu gestų kalba | Bengkala Sign Language |
| `BRA` | `—` | `bra` | `bra` | `bra` | — | Braj |
| `BRE` | `br` | `bre` | `bre` | `bre` | bretonų kalba | Breton |
| `BRG` | `—` | `—` | `—` | `brg` | baurių | Baure |
| `BTK` | `—` | `btk` | `btk` | `btk` | — | Batak languages |
| `BUA` | `—` | `bua` | `bua` | `bua` | — | Buriat |
| `BUG` | `—` | `bug` | `bug` | `bug` | — | Buginese |
| `BUL` | `bg` | `bul` | `bul` | `bul` | bulgarų kalba | Bulgarian |
| `BVL` | `—` | `—` | `—` | `bvl` | bolivų gestų kalba | Bolivian Sign Language |
| `BYN` | `—` | `byn` | `byn` | `byn` | — | Blin; Bilin |
| `BZS` | `—` | `—` | `—` | `bzs` | brazilų gestų kalba | Brazilian Sign Language |
| `CAD` | `—` | `cad` | `cad` | `cad` | — | Caddo |
| `CAI` | `—` | `cai` | `cai` | `cai` | — | Central American Indian languages |
| `CAL` | `—` | `—` | `—` | `cal` | karolinų | Carolinian |
| `CAO` | `—` | `—` | `—` | `cao` | čakobų | Chacobo |
| `CAR` | `—` | `car` | `car` | `car` | — | Galibi Carib |
| `CAS` | `—` | `—` | `—` | `cas` | čimanių | Chimane |
| `CAT` | `ca` | `cat` | `cat` | `cat` | katalonų kalba | Catalan |
| `CAU` | `—` | `cau` | `cau` | `cau` | — | Caucasian languages |
| `CAV` | `—` | `—` | `—` | `cav` | kavinenjų | Cavineña |
| `CAW` | `—` | `—` | `—` | `caw` | kaljavajų | Kallawaya |
| `CAX` | `—` | `—` | `—` | `cax` | čikitanų | Chiquitano |
| `CAZ` | `—` | `—` | `—` | `caz` | kaničanų | Canichana |
| `CDO` | `—` | `—` | `—` | `cdo` | Mindongo kinų | Min Dong Chinese |
| `CDS` | `—` | `—` | `—` | `cds` | čadiečių gestų kalba | Chadian Sign Language |
| `CEB` | `—` | `ceb` | `ceb` | `ceb` | — | Cebuano |
| `CEL` | `—` | `cel` | `cel` | `cel` | — | Celtic languages |
| `CES` | `cs` | `cze` | `ces` | `ces` | čekų kalba | Czech |
| `CHA` | `ch` | `cha` | `cha` | `cha` | čamorų | Chamorro |
| `CHB` | `—` | `chb` | `chb` | `chb` | — | Chibcha |
| `CHE` | `ce` | `che` | `che` | `che` | — | Chechen |
| `CHG` | `—` | `chg` | `chg` | `chg` | — | Chagatai |
| `CHK` | `—` | `chk` | `chk` | `chk` | — | Chuukese |
| `CHM` | `—` | `chm` | `chm` | `chm` | — | Mari |
| `CHN` | `—` | `chn` | `chn` | `chn` | — | Chinook jargon |
| `CHO` | `—` | `cho` | `cho` | `cho` | — | Choctaw |
| `CHP` | `—` | `chp` | `chp` | `chp` | — | Chipewyan; Dene Suline |
| `CHR` | `—` | `chr` | `chr` | `chr` | — | Cherokee |
| `CHU` | `cu` | `chu` | `chu` | `chu` | — | Church Slavic; Old Slavonic; Church Slavonic; Old Bulgarian; Old Church Slavonic |
| `CHV` | `cv` | `chv` | `chv` | `chv` | — | Chuvash |
| `CHY` | `—` | `chy` | `chy` | `chy` | — | Cheyenne |
| `CJY` | `—` | `—` | `—` | `cjy` | Dzinio kinų | Jinyu Chinese |
| `CKB` | `—` | `—` | `—` | `ckb` | vidurio kurdų | Central Kurdish |
| `CKM` | `—` | `—` | `—` | `ckm` | čakavų | Chakavian |
| `CLS` | `—` | `—` | `—` | `cls` | klasikinis sanskritas | Classical Sanskrit |
| `CMC` | `—` | `cmc` | `cmc` | `cmc` | — | Chamic languages |
| `CMN` | `—` | `—` | `—` | `cmn` | mandarinų kalbos | Mandarin Chinese |
| `CNP` | `—` | `—` | `—` | `cnp` | šiaurės pinghua kinų | Northern Ping Chinese |
| `CNR` | `—` | `cnr` | `cnr` | `cnr` | juodkalniečių kalba | Montenegrin |
| `COP` | `—` | `cop` | `cop` | `cop` | — | Coptic |
| `COR` | `kw` | `cor` | `cor` | `cor` | kornų kalba | Cornish |
| `COS` | `co` | `cos` | `cos` | `cos` | korsikiečių kalba | Corsican |
| `CPE` | `—` | `cpe` | `cpe` | `cpe` | — | Creoles and pidgins, English based |
| `CPF` | `—` | `cpf` | `cpf` | `cpf` | — | Creoles and pidgins, French-based |
| `CPP` | `—` | `cpp` | `cpp` | `cpp` | — | Creoles and pidgins, Portuguese-based |
| `CPX` | `—` | `—` | `—` | `cpx` | Pusianio kinų | Pu-Xian Chinese |
| `CRE` | `cr` | `cre` | `cre` | `cre` | krijų | Cree |
| `CRH` | `—` | `crh` | `crh` | `crh` | — | Crimean Tatar; Crimean Turkish |
| `CRP` | `—` | `crp` | `crp` | `crp` | — | Creoles and pidgins |
| `CRS` | `—` | `—` | `—` | `crs` | seišeliečių kreolų ir prancūzų kalba | Seselwa Creole French |
| `CSB` | `—` | `csb` | `csb` | `csb` | kašubų kalba | Kashubian |
| `CSC` | `—` | `—` | `—` | `csc` | katalonų gestų kalba | Catalan Sign Language |
| `CSD` | `—` | `—` | `—` | `csd` | Čiang Majaus gestų kalba | Chiangmai Sign Language |
| `CSE` | `—` | `—` | `—` | `cse` | čekų gestų kalba | Czech Sign Language |
| `CSF` | `—` | `—` | `—` | `csf` | kubiečių gestų kalba | Cuban Sign Language |
| `CSG` | `—` | `—` | `—` | `csg` | čiliečių gestų kalba | Chilean Sign Language |
| `CSL` | `—` | `—` | `—` | `csl` | kinų gestų kalba | Chinese Sign Language |
| `CSN` | `—` | `—` | `—` | `csn` | kolumbiečių gestų kalba | Colombian Sign Language |
| `CSP` | `—` | `—` | `—` | `csp` | pietų pinghua kinų | Southern Ping Chinese |
| `CSQ` | `—` | `—` | `—` | `csq` | kroatų gestų kalba | Croatian Sign Language |
| `CSR` | `—` | `—` | `—` | `csr` | kostarikiečių gestų kalba | Costa Rican Sign Language |
| `CUS` | `—` | `cus` | `cus` | `cus` | — | Cushitic languages |
| `CXH` | `—` | `—` | `—` | `cxh` | čarių | Cha'ari |
| `CYB` | `—` | `—` | `—` | `cyb` | kajubabų | Cayubaba |
| `CYM` | `cy` | `wel` | `cym` | `cym` | valų kalba | Welsh |
| `CZH` | `—` | `—` | `—` | `czh` | Huidžou kinų | Huizhou Chinese |
| `CZO` | `—` | `—` | `—` | `czo` | Mindžongo kinų | Min Zhong Chinese |
| `DAK` | `—` | `dak` | `dak` | `dak` | — | Dakota |
| `DAN` | `da` | `dan` | `dan` | `dan` | danų kalba | Danish |
| `DAR` | `—` | `dar` | `dar` | `dar` | — | Dargwa |
| `DAY` | `—` | `day` | `day` | `day` | — | Land Dayak languages |
| `DEH` | `—` | `—` | `—` | `deh` | dehvarių | Dehwari |
| `DEL` | `—` | `del` | `del` | `del` | — | Delaware |
| `DEN` | `—` | `den` | `den` | `den` | — | Slave (Athapascan) |
| `DEU` | `de` | `ger` | `deu` | `deu` | vokiečių kalba | German |
| `DGR` | `—` | `dgr` | `dgr` | `dgr` | — | Tlicho |
| `DIN` | `—` | `din` | `din` | `din` | — | Dinka |
| `DIQ` | `—` | `—` | `—` | `diq` | dimli | Dimli |
| `DIV` | `dv` | `div` | `div` | `div` | maldyvų kalba | Dhivehi |
| `DOI` | `—` | `doi` | `doi` | `doi` | — | Dogri |
| `DOQ` | `—` | `—` | `—` | `doq` | dominikiečių gestų kalba | Dominican Sign Language |
| `DRA` | `—` | `dra` | `dra` | `dra` | — | Dravidian languages |
| `DSB` | `—` | `dsb` | `dsb` | `dsb` | — | Lower Sorbian |
| `DSE` | `—` | `—` | `—` | `dse` | nyderlandų gestų kalba | Dutch Sign Language |
| `DSK` | `—` | `—` | `—` | `dsk` | dokšų | Dokshi |
| `DSL` | `—` | `—` | `—` | `dsl` | danų gestų kalba | Danish Sign Language |
| `DUA` | `—` | `dua` | `dua` | `dua` | — | Duala |
| `DUM` | `—` | `dum` | `dum` | `dum` | — | Dutch, Middle (ca.1050-1350) |
| `DYR` | `—` | `—` | `—` | `dyr` | djarimų | Dyarim |
| `DYU` | `—` | `dyu` | `dyu` | `dyu` | — | Dyula |
| `DZO` | `dz` | `dzo` | `dzo` | `dzo` | dzongkha | Dzongkha |
| `ECS` | `—` | `—` | `—` | `ecs` | ekvadoriečių gestų kalba | Ecuadorian Sign Language |
| `EFI` | `—` | `efi` | `efi` | `efi` | — | Efik |
| `EGY` | `—` | `egy` | `egy` | `egy` | — | Egyptian (Ancient) |
| `EKA` | `—` | `eka` | `eka` | `eka` | — | Ekajuk |
| `ELL` | `el` | `gre` | `ell` | `ell` | graikų kalba | Greek |
| `ELX` | `—` | `elx` | `elx` | `elx` | — | Elamite |
| `EMK` | `—` | `—` | `—` | `emk` | rytų maninkų | Eastern Maninkakan |
| `ENG` | `en` | `eng` | `eng` | `eng` | anglų kalba | English |
| `ENM` | `—` | `enm` | `enm` | `enm` | — | Middle English (1100-1500) |
| `EPO` | `eo` | `epo` | `epo` | `epo` | esperanto kalba | Esperanto |
| `ESE` | `—` | `—` | `—` | `ese` | esechų | Ese Ejja |
| `ESL` | `—` | `—` | `—` | `esl` | egiptiečių gestų kalba | Egyptian Sign Language |
| `ESN` | `—` | `—` | `—` | `esn` | salvadoriečių gestų kalba | Salvadoran Sign Language |
| `ESO` | `—` | `—` | `—` | `eso` | estų gestų kalba | Estonian Sign Language |
| `EST` | `et` | `est` | `est` | `est` | estų kalba | Estonian |
| `ETH` | `—` | `—` | `—` | `eth` | etiopų gestų kalba | Ethiopian Sign Language |
| `EUS` | `eu` | `baq` | `eus` | `eus` | baskų kalba | Basque |
| `EWE` | `ee` | `ewe` | `ewe` | `ewe` | evių kalba | Ewe |
| `EWO` | `—` | `ewo` | `ewo` | `ewo` | — | Ewondo |
| `FAN` | `—` | `fan` | `fan` | `fan` | — | Fang |
| `FAO` | `fo` | `fao` | `fao` | `fao` | farerų kalba | Faroese |
| `FAS` | `fa` | `per` | `fas` | `fas` | persų kalba | Persian |
| `FAT` | `—` | `fat` | `fat` | `fat` | — | Fanti |
| `FCS` | `—` | `—` | `—` | `fcs` | kvebekiečių gestų kalba | Quebec Sign Language |
| `FIJ` | `fj` | `fij` | `fij` | `fij` | fidžių | Fijian |
| `FIL` | `—` | `fil` | `fil` | `fil` | filipinų | Filipino |
| `FIN` | `fi` | `fin` | `fin` | `fin` | suomių kalba | Finnish |
| `FIU` | `—` | `fiu` | `fiu` | `fiu` | — | Finno-Ugrian languages |
| `FON` | `—` | `fon` | `fon` | `fon` | — | Fon |
| `FRA` | `fr` | `fre` | `fra` | `fra` | prancūzų kalba | French |
| `FRM` | `—` | `frm` | `frm` | `frm` | — | French, Middle (ca.1400-1600) |
| `FRO` | `—` | `fro` | `fro` | `fro` | — | French, Old (842-ca.1400) |
| `FRR` | `—` | `frr` | `frr` | `frr` | — | Northern Frisian |
| `FRS` | `—` | `frs` | `frs` | `frs` | — | Eastern Frisian |
| `FRY` | `fy` | `fry` | `fry` | `fry` | fryzų kalba | Frisian |
| `FSE` | `—` | `—` | `—` | `fse` | suomių gestų kalba | Finnish Sign Language |
| `FSL` | `—` | `—` | `—` | `fsl` | prancūzų gestų kalba | French Sign Language |
| `FSS` | `—` | `—` | `—` | `fss` | Suomijos švedų gestų kalba | Finland-Swedish Sign Language |
| `FUL` | `ff` | `ful` | `ful` | `ful` | fulų | Fula |
| `FUR` | `—` | `fur` | `fur` | `fur` | — | Friulan |
| `GAA` | `—` | `gaa` | `gaa` | `gaa` | — | Ga |
| `GAN` | `—` | `—` | `—` | `gan` | Gano kinų | Gan Chinese |
| `GAY` | `—` | `gay` | `gay` | `gay` | — | Gayo |
| `GBA` | `—` | `gba` | `gba` | `gba` | — | Gbaya |
| `GEM` | `—` | `gem` | `gem` | `gem` | — | Germanic languages |
| `GEZ` | `—` | `gez` | `gez` | `gez` | — | Geez |
| `GIL` | `—` | `gil` | `gil` | `gil` | — | Gilbertese |
| `GLA` | `gd` | `gla` | `gla` | `gla` | škotų gėlų kalba | Scottish Gaelic |
| `GLE` | `ga` | `gle` | `gle` | `gle` | airių kalba | Irish |
| `GLG` | `gl` | `glg` | `glg` | `glg` | galisų kalba | Galician |
| `GLV` | `gv` | `glv` | `glv` | `glv` | meniečių | Manx |
| `GMH` | `—` | `gmh` | `gmh` | `gmh` | — | German, Middle High (ca.1050-1500) |
| `GOH` | `—` | `goh` | `goh` | `goh` | — | German, Old High (ca.750-1050) |
| `GON` | `—` | `gon` | `gon` | `gon` | — | Gondi |
| `GOR` | `—` | `gor` | `gor` | `gor` | — | Gorontalo |
| `GOT` | `—` | `got` | `got` | `got` | — | Gothic |
| `GRB` | `—` | `grb` | `grb` | `grb` | — | Grebo |
| `GRC` | `—` | `grc` | `grc` | `grc` | — | Greek, Ancient (to 1453) |
| `GRN` | `gn` | `grn` | `grn` | `grn` | gvaranių | Guarani |
| `GSE` | `—` | `—` | `—` | `gse` | ganiečių gestų kalba | Ghanaian Sign Language |
| `GSG` | `—` | `—` | `—` | `gsg` | vokiečių gestų kalba | German Sign Language |
| `GSM` | `—` | `—` | `—` | `gsm` | gvatemaliečių gestų kalba | Guatemalan Sign Language |
| `GSS` | `—` | `—` | `—` | `gss` | graikų gestų kalba | Greek Sign Language |
| `GSW` | `—` | `gsw` | `gsw` | `gsw` | — | Swiss German; Alemannic; Alsatian |
| `GUG` | `—` | `—` | `—` | `gug` | Paragvajaus gvaranių | Paraguayan Guaraní |
| `GUJ` | `gu` | `guj` | `guj` | `guj` | — | Gujarati |
| `GUS` | `—` | `—` | `—` | `gus` | gvinėjiečių gestų kalba | Guinean Sign Language |
| `GWI` | `—` | `gwi` | `gwi` | `gwi` | — | Gwich'in |
| `GYR` | `—` | `—` | `—` | `gyr` | gvarajų | Guarayu |
| `HAB` | `—` | `—` | `—` | `hab` | Hanojaus gestų kalba | Hanoi Sign Language |
| `HAC` | `—` | `—` | `—` | `hac` | guranių | Gurani |
| `HAF` | `—` | `—` | `—` | `haf` | Haifongo gestų kalba | Haiphong Sign Language |
| `HAI` | `—` | `hai` | `hai` | `hai` | — | Haida |
| `HAK` | `—` | `—` | `—` | `hak` | hakų kinų | Hakka Chinese |
| `HAT` | `ht` | `hat` | `hat` | `hat` | haitiečių kalba | Haitian |
| `HAU` | `ha` | `hau` | `hau` | `hau` | hausų | Hausa |
| `HAW` | `—` | `haw` | `haw` | `haw` | — | Hawaiian |
| `HAZ` | `—` | `—` | `—` | `haz` | hazaragių | Hazaragi |
| `HBS` | `sh` | `—` | `—` | `hbs` | serbų-kroatų kalba | Serbo-Croatian |
| `HCA` | `—` | `—` | `—` | `hca` | andamanų kreolų hindi | Andaman Creole Hindi |
| `HDS` | `—` | `—` | `—` | `hds` | hondūriečių gestų kalba | Honduran Sign Language |
| `HEB` | `he` | `heb` | `heb` | `heb` | hebrajų kalba | Hebrew |
| `HER` | `hz` | `her` | `her` | `her` | — | Herero |
| `HIF` | `—` | `—` | `—` | `hif` | Fidžio hindi | Fiji Hindi |
| `HIL` | `—` | `hil` | `hil` | `hil` | — | Hiligaynon |
| `HIM` | `—` | `him` | `him` | `him` | — | Himachali languages; Western Pahari languages |
| `HIN` | `hi` | `hin` | `hin` | `hin` | hindi kalba | Hindi |
| `HIO` | `—` | `—` | `—` | `hio` | tsvanų | Tsoa |
| `HIT` | `—` | `hit` | `hit` | `hit` | — | Hittite |
| `HKS` | `—` | `—` | `—` | `hks` | Honkongo gestų kalba | Hong Kong Sign Language |
| `HMN` | `—` | `hmn` | `hmn` | `hmn` | — | Hmong; Mong |
| `HMO` | `ho` | `hmo` | `hmo` | `hmo` | hirimotų | Hiri Motu |
| `HNM` | `—` | `—` | `—` | `hnm` | Hainano kinų | Hainanese |
| `HOS` | `—` | `—` | `—` | `hos` | Hošimino gestų kalba | Ho Chi Minh City Sign Language |
| `HPS` | `—` | `—` | `—` | `hps` | Havajų pidžin gestų kalba | Hawai‘i Pidgin Sign Language |
| `HRV` | `hr` | `hrv` | `hrv` | `hrv` | kroatų kalba | Croatian |
| `HSB` | `—` | `hsb` | `hsb` | `hsb` | aukštutinių sorbų kalba | Upper Sorbian |
| `HSH` | `—` | `—` | `—` | `hsh` | vengrų gestų kalba | Hungarian Sign Language |
| `HSL` | `—` | `—` | `—` | `hsl` | hausų gestų kalba | Hausa Sign Language |
| `HSN` | `—` | `—` | `—` | `hsn` | Siango kinų | Xiang Chinese |
| `HUN` | `hu` | `hun` | `hun` | `hun` | vengrų kalba | Hungarian |
| `HUP` | `—` | `hup` | `hup` | `hup` | — | Hupa |
| `HYE` | `hy` | `arm` | `hye` | `hye` | armėnų kalba | Armenian |
| `IBA` | `—` | `iba` | `iba` | `iba` | — | Iban |
| `IBO` | `ig` | `ibo` | `ibo` | `ibo` | igbų kalba | Igbo |
| `ICL` | `—` | `—` | `—` | `icl` | islandų gestų kalba | Icelandic Sign Language |
| `IDO` | `io` | `ido` | `ido` | `ido` | — | Ido |
| `IGN` | `—` | `—` | `—` | `ign` | mochų ignasiečių | Ignaciano |
| `III` | `ii` | `iii` | `iii` | `iii` | — | Sichuan Yi; Nuosu |
| `IJO` | `—` | `ijo` | `ijo` | `ijo` | — | Ijo languages |
| `IKU` | `iu` | `iku` | `iku` | `iku` | — | Inuktitut |
| `ILE` | `ie` | `ile` | `ile` | `ile` | — | Interlingue; Occidental |
| `ILO` | `—` | `ilo` | `ilo` | `ilo` | — | Iloko |
| `INA` | `ia` | `ina` | `ina` | `ina` | interlingua | Interlingua |
| `INC` | `—` | `inc` | `inc` | `inc` | — | Indic languages |
| `IND` | `id` | `ind` | `ind` | `ind` | indoneziečių kalba | Indonesian |
| `INE` | `—` | `ine` | `ine` | `ine` | — | Indo-European languages |
| `INH` | `—` | `inh` | `inh` | `inh` | — | Ingush |
| `INL` | `—` | `—` | `—` | `inl` | indoneziečių gestų kalba | Indonesian Sign Language |
| `INS` | `—` | `—` | `—` | `ins` | indų gestų kalba | Indian Sign Language |
| `IPK` | `ik` | `ipk` | `ipk` | `ipk` | — | Inupiaq |
| `IRA` | `—` | `ira` | `ira` | `ira` | — | Iranian languages |
| `IRO` | `—` | `iro` | `iro` | `iro` | — | Iroquoian languages |
| `ISE` | `—` | `—` | `—` | `ise` | italų gestų kalba | Italian Sign Language |
| `ISG` | `—` | `—` | `—` | `isg` | airių gestų kalba | Irish Sign Language |
| `ISL` | `is` | `ice` | `isl` | `isl` | islandų kalba | Icelandic |
| `ISR` | `—` | `—` | `—` | `isr` | izraeliečių gestų kalba | Israeli Sign Language |
| `ITA` | `it` | `ita` | `ita` | `ita` | italų kalba | Italian |
| `ITE` | `—` | `—` | `—` | `ite` | itenių | Itene |
| `ITO` | `—` | `—` | `—` | `ito` | itonamų | Itonama |
| `JAD` | `—` | `—` | `—` | `jad` | džahanka | Jahanka |
| `JAV` | `jv` | `jav` | `jav` | `jav` | — | Javanese |
| `JBO` | `—` | `jbo` | `jbo` | `jbo` | — | Lojban |
| `JCS` | `—` | `—` | `—` | `jcs` | Jamaikos kaimo gestų kalba | Jamaican Country Sign Language |
| `JDT` | `—` | `—` | `—` | `jdt` | kalnų žydų | Judeo-Tat |
| `JHS` | `—` | `—` | `—` | `jhs` | Džankoto gestų kalba | Jhankot Sign Language |
| `JOS` | `—` | `—` | `—` | `jos` | jordaniečių gestų kalba | Jordanian Sign Language |
| `JPN` | `ja` | `jpn` | `jpn` | `jpn` | japonų kalba | Japanese |
| `JPR` | `—` | `jpr` | `jpr` | `jpr` | žydų persų | Judeo-Persian |
| `JRB` | `—` | `jrb` | `jrb` | `jrb` | — | Judeo-Arabic |
| `JSL` | `—` | `—` | `—` | `jsl` | japonų gestų kalba | Japanese Sign Language |
| `JUS` | `—` | `—` | `—` | `jus` | Džumlos gestų kalba | Jumla Sign Language |
| `KAA` | `—` | `kaa` | `kaa` | `kaa` | — | Kara-Kalpak |
| `KAB` | `—` | `kab` | `kab` | `kab` | — | Kabyle |
| `KAC` | `—` | `kac` | `kac` | `kac` | — | Kachin; Jingpho |
| `KAL` | `kl` | `kal` | `kal` | `kal` | kalaallisutų | Kalaallisut |
| `KAM` | `—` | `kam` | `kam` | `kam` | — | Kamba |
| `KAN` | `kn` | `kan` | `kan` | `kan` | — | Kannada |
| `KAO` | `—` | `—` | `—` | `kao` | hasonkų | Xaasongaxango |
| `KAR` | `—` | `kar` | `kar` | `kar` | — | Karen languages |
| `KAS` | `ks` | `kas` | `kas` | `kas` | — | Kashmiri |
| `KAT` | `ka` | `geo` | `kat` | `kat` | gruzinų kalba | Georgian |
| `KAU` | `kr` | `kau` | `kau` | `kau` | — | Kanuri |
| `KAW` | `—` | `kaw` | `kaw` | `kaw` | — | Kawi |
| `KAZ` | `kk` | `kaz` | `kaz` | `kaz` | kazachų kalba | Kazakh |
| `KBD` | `—` | `kbd` | `kbd` | `kbd` | — | Kabardian |
| `KCK` | `—` | `—` | `—` | `kck` | kalangų | Kalanga |
| `KGI` | `—` | `—` | `—` | `kgi` | Selangoro gestų kalba | Selangor Sign Language |
| `KHA` | `—` | `kha` | `kha` | `kha` | — | Khasi |
| `KHI` | `—` | `khi` | `khi` | `khi` | — | Khoisan languages |
| `KHM` | `km` | `khm` | `khm` | `khm` | khmerų kalba | Khmer |
| `KHO` | `—` | `kho` | `kho` | `kho` | — | Khotanese; Sakan |
| `KIK` | `ki` | `kik` | `kik` | `kik` | — | Kikuyu; Gikuyu |
| `KIN` | `rw` | `kin` | `kin` | `kin` | kinjaruandų | Kinyarwanda |
| `KIR` | `ky` | `kir` | `kir` | `kir` | kirgizų kalba | Kyrgyz |
| `KIU` | `—` | `—` | `—` | `kiu` | kurmandžių | Kirmanjki |
| `KMB` | `—` | `kmb` | `kmb` | `kmb` | — | Kimbundu |
| `KMR` | `—` | `—` | `—` | `kmr` | šiaurės kurdų | Northern Kurdish |
| `KOK` | `—` | `kok` | `kok` | `kok` | — | Konkani |
| `KOM` | `kv` | `kom` | `kom` | `kom` | — | Komi |
| `KON` | `kg` | `kon` | `kon` | `kon` | kongiečių (kikongo) kalba | Kikongo |
| `KOR` | `ko` | `kor` | `kor` | `kor` | korėjiečių kalba | Korean |
| `KOS` | `—` | `kos` | `kos` | `kos` | — | Kosraean |
| `KPE` | `—` | `kpe` | `kpe` | `kpe` | — | Kpelle |
| `KRC` | `—` | `krc` | `krc` | `krc` | — | Karachay-Balkar |
| `KRL` | `—` | `krl` | `krl` | `krl` | karelų | Karelian |
| `KRO` | `—` | `kro` | `kro` | `kro` | — | Kru languages |
| `KRU` | `—` | `kru` | `kru` | `kru` | — | Kurukh |
| `KUA` | `kj` | `kua` | `kua` | `kua` | — | Kuanyama; Kwanyama |
| `KUM` | `—` | `kum` | `kum` | `kum` | — | Kumyk |
| `KUR` | `ku` | `kur` | `kur` | `kur` | kurdų kalba | Kurdish |
| `KUT` | `—` | `kut` | `kut` | `kut` | — | Kutenai |
| `KVK` | `—` | `—` | `—` | `kvk` | korėjiečių gestų kalba | Korean Sign Language |
| `KXD` | `—` | `—` | `—` | `kxd` | Brunėjaus malajiečių | Brunei Malay |
| `LAD` | `—` | `lad` | `lad` | `lad` | — | Ladino |
| `LAH` | `—` | `lah` | `lah` | `lah` | — | Lahnda |
| `LAM` | `—` | `lam` | `lam` | `lam` | — | Lamba |
| `LAO` | `lo` | `lao` | `lao` | `lao` | lao kalba | Lao |
| `LAT` | `la` | `lat` | `lat` | `lat` | lotynų kalba | Latin |
| `LAV` | `lv` | `lav` | `lav` | `lav` | latvių kalba | Latvian |
| `LBS` | `—` | `—` | `—` | `lbs` | libių gestų kalba | Libyan Sign Language |
| `LEC` | `—` | `—` | `—` | `lec` | lekų | Leco |
| `LEZ` | `—` | `lez` | `lez` | `lez` | — | Lezghian |
| `LIM` | `li` | `lim` | `lim` | `lim` | — | Limburgan; Limburger; Limburgish |
| `LIN` | `ln` | `lin` | `lin` | `lin` | lingala | Lingala |
| `LIT` | `lt` | `lit` | `lit` | `lit` | lietuvių kalba | Lithuanian |
| `LKI` | `—` | `—` | `—` | `lki` | lakių | Laki |
| `LLS` | `—` | `—` | `—` | `lls` | lietuvių gestų kalba | Lithuanian Sign Language |
| `LOL` | `—` | `lol` | `lol` | `lol` | — | Mongo |
| `LOZ` | `—` | `loz` | `loz` | `loz` | — | Lozi |
| `LSG` | `—` | `—` | `—` | `lsg` | Lyonso gestų kalba | Lyons Sign Language |
| `LSL` | `—` | `—` | `—` | `lsl` | latvių gestų kalba | Latvian Sign Language |
| `LSO` | `—` | `—` | `—` | `lso` | laosiečių gestų kalba | Laotian Sign Language |
| `LSP` | `—` | `—` | `—` | `lsp` | panamiečių gestų kalba | Panamanian Sign Language |
| `LST` | `—` | `—` | `—` | `lst` | Trinidado ir Tobago gyventojų gestų kalba | Trinidad and Tobago Sign Language |
| `LTC` | `—` | `—` | `—` | `ltc` | vėlyvoji vidurinė kinų | Late Middle Chinese |
| `LTZ` | `lb` | `ltz` | `ltz` | `ltz` | liuksemburgiečių kalba | Luxembourgish |
| `LUA` | `—` | `lua` | `lua` | `lua` | Luba-Lulua kalba | Luba-Lulua |
| `LUB` | `lu` | `lub` | `lub` | `lub` | — | Luba-Katanga |
| `LUG` | `lg` | `lug` | `lug` | `lug` | — | Ganda |
| `LUH` | `—` | `—` | `—` | `luh` | Leidžou kinų | Leizhou Chinese |
| `LUI` | `—` | `lui` | `lui` | `lui` | — | Luiseno |
| `LUN` | `—` | `lun` | `lun` | `lun` | — | Lunda |
| `LUO` | `—` | `luo` | `luo` | `luo` | — | Luo (Kenya and Tanzania) |
| `LUS` | `—` | `lus` | `lus` | `lus` | — | Lushai |
| `LZH` | `—` | `—` | `—` | `lzh` | klasikinė kinų | Literary Chinese |
| `MAD` | `—` | `mad` | `mad` | `mad` | — | Madurese |
| `MAG` | `—` | `mag` | `mag` | `mag` | — | Magahi |
| `MAH` | `mh` | `mah` | `mah` | `mah` | maršaliečių | Marshallese |
| `MAI` | `—` | `mai` | `mai` | `mai` | — | Maithili |
| `MAK` | `—` | `mak` | `mak` | `mak` | — | Makasar |
| `MAL` | `ml` | `mal` | `mal` | `mal` | — | Malayalam |
| `MAN` | `—` | `man` | `man` | `man` | mandingų | Manding |
| `MAP` | `—` | `map` | `map` | `map` | — | Austronesian languages |
| `MAR` | `mr` | `mar` | `mar` | `mar` | — | Marathi |
| `MAS` | `—` | `mas` | `mas` | `mas` | — | Masai |
| `MDF` | `—` | `mdf` | `mdf` | `mdf` | — | Moksha |
| `MDL` | `—` | `—` | `—` | `mdl` | maltiečių gestų kalba | Maltese Sign Language |
| `MDR` | `—` | `mdr` | `mdr` | `mdr` | — | Mandar |
| `MEN` | `—` | `men` | `men` | `men` | — | Mende |
| `MFS` | `—` | `—` | `—` | `mfs` | meksikiečių gestų kalba | Mexican Sign Language |
| `MGA` | `—` | `mga` | `mga` | `mga` | — | Irish, Middle (900-1200) |
| `MIC` | `—` | `mic` | `mic` | `mic` | — | Mi'kmaq; Micmac |
| `MIN` | `—` | `min` | `min` | `min` | minangkabau kalba | Minangkabau |
| `MIS` | `—` | `mis` | `mis` | `mis` | nekoduota kalba | Uncoded languages |
| `MKD` | `mk` | `mac` | `mkd` | `mkd` | makedoniečių kalba | Macedonian |
| `MKH` | `—` | `mkh` | `mkh` | `mkh` | — | Mon-Khmer languages |
| `MLG` | `mg` | `mlg` | `mlg` | `mlg` | malagasių kalba | Malagasy |
| `MLQ` | `—` | `—` | `—` | `mlq` | vakarų maninkų | Western Maninkakan |
| `MLT` | `mt` | `mlt` | `mlt` | `mlt` | maltiečių kalba | Maltese |
| `MNC` | `—` | `mnc` | `mnc` | `mnc` | — | Manchu |
| `MNI` | `—` | `mni` | `mni` | `mni` | — | Manipuri |
| `MNK` | `—` | `—` | `—` | `mnk` | mandinkų kalba | Mandinka |
| `MNO` | `—` | `mno` | `mno` | `mno` | — | Manobo languages |
| `MNP` | `—` | `—` | `—` | `mnp` | Minbėjaus kinų | Min Bei Chinese |
| `MOH` | `—` | `moh` | `moh` | `moh` | — | Mohawk |
| `MOL` | `mo` | `mol` | `mol` | `mol` | moldavų kalba | Moldavian |
| `MON` | `mn` | `mon` | `mon` | `mon` | mongolų kalba | Mongolian |
| `MOS` | `—` | `mos` | `mos` | `mos` | — | Mossi |
| `MPD` | `—` | `—` | `—` | `mpd` | mačinerių | Machinere |
| `MRE` | `—` | `—` | `—` | `mre` | Martos Vynuogyno gestų kalba | Martha’s Vineyard Sign Language |
| `MRI` | `mi` | `mao` | `mri` | `mri` | maorių | Māori |
| `MSA` | `ms` | `may` | `msa` | `msa` | malajų kalba | Malay |
| `MSD` | `—` | `—` | `—` | `msd` | jukatekų majų gestų kalba | Yucatec Maya Sign Language |
| `MSR` | `—` | `—` | `—` | `msr` | mongolų gestų kalba | Mongolian Sign Language |
| `MTP` | `—` | `—` | `—` | `mtp` | vičių noktenų | Wichí Lhamtés Nocten |
| `MUL` | `—` | `mul` | `mul` | `mul` | kelios kalbos | Multiple languages |
| `MUN` | `—` | `mun` | `mun` | `mun` | — | Munda languages |
| `MUS` | `—` | `mus` | `mus` | `mus` | — | Creek |
| `MWK` | `—` | `—` | `—` | `mwk` | Kitos maninkų | Kita Maninkakan |
| `MWL` | `—` | `mwl` | `mwl` | `mwl` | — | Mirandese |
| `MWR` | `—` | `mwr` | `mwr` | `mwr` | — | Marwari |
| `MYA` | `my` | `bur` | `mya` | `mya` | mjanmų | Burmese |
| `MYN` | `—` | `myn` | `myn` | `myn` | — | Mayan languages |
| `MYV` | `—` | `myv` | `myv` | `myv` | — | Erzya |
| `MZC` | `—` | `—` | `—` | `mzc` | madagaskariečių gestų kalba | Madagascar Sign Language |
| `MZG` | `—` | `—` | `—` | `mzg` | vienuolių gestų kalba | Monastic Sign Language |
| `MZP` | `—` | `—` | `—` | `mzp` | movimų | Movima |
| `MZY` | `—` | `—` | `—` | `mzy` | mozambikiečių gestų kalba | Mozambican Sign Language |
| `NAH` | `—` | `nah` | `nah` | `nah` | — | Nahuatl languages |
| `NAI` | `—` | `nai` | `nai` | `nai` | — | North American Indian languages |
| `NAN` | `—` | `—` | `—` | `nan` | Minanio kinų | Min Nan Chinese |
| `NAP` | `—` | `nap` | `nap` | `nap` | — | Neapolitan |
| `NAU` | `na` | `nau` | `nau` | `nau` | nauriečių | Nauruan |
| `NAV` | `nv` | `nav` | `nav` | `nav` | — | Navajo; Navaho |
| `NBL` | `nr` | `nbl` | `nbl` | `nbl` | pietų ndebelių | Southern Ndebele |
| `NBS` | `—` | `—` | `—` | `nbs` | namibiečių gestų kalba | Namibian Sign Language |
| `NCS` | `—` | `—` | `—` | `ncs` | nikaragviečių gestų kalba | Nicaraguan Sign Language |
| `NDC` | `—` | `—` | `—` | `ndc` | ndau | Ndau |
| `NDE` | `nd` | `nde` | `nde` | `nde` | šiaurės ndebelių | North Ndebele |
| `NDO` | `ng` | `ndo` | `ndo` | `ndo` | — | Ndonga |
| `NDS` | `—` | `nds` | `nds` | `nds` | — | Low German; Low Saxon; German, Low; Saxon, Low |
| `NEP` | `ne` | `nep` | `nep` | `nep` | nepalų kalba | Nepali |
| `NEW` | `—` | `new` | `new` | `new` | — | Nepal Bhasa |
| `NIA` | `—` | `nia` | `nia` | `nia` | — | Nias |
| `NIC` | `—` | `nic` | `nic` | `nic` | — | Niger-Kordofanian languages |
| `NIU` | `—` | `niu` | `niu` | `niu` | niujų | Niuean |
| `NLD` | `nl` | `dut` | `nld` | `nld` | nyderlandų kalba | Dutch |
| `NMQ` | `—` | `—` | `—` | `nmq` | nambjų | Nambya |
| `NNO` | `nn` | `nno` | `nno` | `nno` | norvegų niunoškas | Norwegian Nynorsk |
| `NOB` | `nb` | `nob` | `nob` | `nob` | norvegų bukmolas | Norwegian Bokmål |
| `NOG` | `—` | `nog` | `nog` | `nog` | — | Nogai |
| `NON` | `—` | `non` | `non` | `non` | — | Norse, Old |
| `NOR` | `no` | `nor` | `nor` | `nor` | norvegų kalba | Norwegian |
| `NQO` | `—` | `nqo` | `nqo` | `nqo` | — | N'Ko |
| `NSI` | `—` | `—` | `—` | `nsi` | nigeriečių gestų kalba | Nigerian Sign Language |
| `NSL` | `—` | `—` | `—` | `nsl` | norvegų gestų kalba | Norwegian Sign Language |
| `NSO` | `—` | `nso` | `nso` | `nso` | šiaurės sotų | Northern Sotho |
| `NSP` | `—` | `—` | `—` | `nsp` | nepaliečių gestų kalba | Nepalese Sign Language |
| `NSR` | `—` | `—` | `—` | `nsr` | jūrų gestų kalba | Maritime Sign Language |
| `NUB` | `—` | `nub` | `nub` | `nub` | — | Nubian languages |
| `NWC` | `—` | `nwc` | `nwc` | `nwc` | — | Classical Newari; Old Newari; Classical Nepal Bhasa |
| `NYA` | `ny` | `nya` | `nya` | `nya` | čičevų | Chichewa |
| `NYM` | `—` | `nym` | `nym` | `nym` | — | Nyamwezi |
| `NYN` | `—` | `nyn` | `nyn` | `nyn` | — | Nyankole |
| `NYO` | `—` | `nyo` | `nyo` | `nyo` | — | Nyoro |
| `NZI` | `—` | `nzi` | `nzi` | `nzi` | — | Nzima |
| `NZS` | `—` | `—` | `—` | `nzs` | naujazelandiečių gestų kalba | New Zealand Sign Language |
| `OCH` | `—` | `—` | `—` | `och` | senoji kinų | Old Chinese |
| `OCI` | `oc` | `oci` | `oci` | `oci` | oksitanų kalba | Occitan |
| `OJI` | `oj` | `oji` | `oji` | `oji` | — | Ojibwa |
| `ORI` | `or` | `ori` | `ori` | `ori` | — | Oriya |
| `ORM` | `om` | `orm` | `orm` | `orm` | — | Oromo |
| `OSA` | `—` | `osa` | `osa` | `osa` | — | Osage |
| `OSD` | `—` | `—` | `—` | `osd` | osetinų digorų | Digor Ossetic |
| `OSS` | `os` | `oss` | `oss` | `oss` | osetinų ironų | Iron Ossetic |
| `OTA` | `—` | `ota` | `ota` | `ota` | — | Turkish, Ottoman (1500-1928) |
| `OTO` | `—` | `oto` | `oto` | `oto` | — | Otomian languages |
| `PAA` | `—` | `paa` | `paa` | `paa` | — | Papuan languages |
| `PAG` | `—` | `pag` | `pag` | `pag` | — | Pangasinan |
| `PAL` | `—` | `pal` | `pal` | `pal` | — | Pahlavi |
| `PAM` | `—` | `pam` | `pam` | `pam` | — | Pampanga; Kapampangan |
| `PAN` | `pa` | `pan` | `pan` | `pan` | pendžabų kalba | Punjabi |
| `PAP` | `—` | `pap` | `pap` | `pap` | papjamento | Papiamento |
| `PAU` | `—` | `pau` | `pau` | `pau` | palaujiečių | Palauan |
| `PCP` | `—` | `—` | `—` | `pcp` | pakahuarų | Pacahuara |
| `PEO` | `—` | `peo` | `peo` | `peo` | senoji persų (apie 600–400 m. pr. Kr.) | Old Persian (ca. 600-400 B.C.) |
| `PES` | `—` | `—` | `—` | `pes` | Irano persų | Iranian Persian |
| `PHI` | `—` | `phi` | `phi` | `phi` | — | Philippine languages |
| `PHN` | `—` | `phn` | `phn` | `phn` | — | Phoenician |
| `PHV` | `—` | `—` | `—` | `phv` | pehlevanių | Pahlavani |
| `PIH` | `—` | `—` | `—` | `pih` | Pirkerno Norfolko | Pitcairn-Norfolk |
| `PKS` | `—` | `—` | `—` | `pks` | pakistaniečių gestų kalba | Pakistan Sign Language |
| `PLI` | `pi` | `pli` | `pli` | `pli` | — | Pali |
| `POL` | `pl` | `pol` | `pol` | `pol` | lenkų kalba | Polish |
| `PON` | `—` | `pon` | `pon` | `pon` | — | Pohnpeian |
| `POR` | `pt` | `por` | `por` | `por` | portugalų kalba | Portuguese |
| `PRA` | `—` | `pra` | `pra` | `pra` | — | Prakrit languages |
| `PRL` | `—` | `—` | `—` | `prl` | perujiečių gestų kalba | Peruvian Sign Language |
| `PRO` | `—` | `pro` | `pro` | `pro` | — | Provençal, Old (to 1500); Occitan, Old (to 1500) |
| `PRS` | `—` | `—` | `—` | `prs` | dari kalba | Dari |
| `PRZ` | `—` | `—` | `—` | `prz` | Apvaizdos salos gestų kalba | Providencia Sign Language |
| `PSC` | `—` | `—` | `—` | `psc` | irano gestų kalba | Iranian Sign Language |
| `PSD` | `—` | `—` | `—` | `psd` | prerijų indėnų gestų kalba | Plains Indian Sign Language |
| `PSG` | `—` | `—` | `—` | `psg` | Penango gestų kalba | Penang Sign Language |
| `PSL` | `—` | `—` | `—` | `psl` | puertorikiečių gestų kalba | Puerto Rican Sign Language |
| `PSM` | `—` | `—` | `—` | `psm` | pausernų | Pauserna |
| `PSO` | `—` | `—` | `—` | `pso` | lenkų gestų kalba | Polish Sign Language |
| `PSP` | `—` | `—` | `—` | `psp` | filipiniečių gestų kalba | Philippine Sign Language |
| `PSR` | `—` | `—` | `—` | `psr` | portugalų gestų kalba | Portuguese Sign Language |
| `PUQ` | `—` | `—` | `—` | `puq` | pukinų | Puquina |
| `PUS` | `ps` | `pus` | `pus` | `pus` | puštūnų kalba | Pashto |
| `QUE` | `qu` | `que` | `que` | `que` | kečujų | Quechua |
| `RAJ` | `—` | `raj` | `raj` | `raj` | — | Rajasthani |
| `RAP` | `—` | `rap` | `rap` | `rap` | — | Rapanui |
| `RAR` | `—` | `rar` | `rar` | `rar` | rarotongų | Rarotongan |
| `REY` | `—` | `—` | `—` | `rey` | rejesiečių | Reyesano |
| `RKM` | `—` | `—` | `—` | `rkm` | markų | Marka |
| `RMS` | `—` | `—` | `—` | `rms` | rumunų gestų kalba | Romanian Sign Language |
| `ROA` | `—` | `roa` | `roa` | `roa` | — | Romance languages |
| `ROH` | `rm` | `roh` | `roh` | `roh` | romanų kalba | Romansh |
| `ROM` | `—` | `rom` | `rom` | `rom` | romų kalba | Romani |
| `RON` | `ro` | `rum` | `ron` | `ron` | rumunų kalba | Romanian |
| `RSI` | `—` | `—` | `—` | `rsi` | Renelio gestų kalba | Rennellese Sign Language |
| `RSL` | `—` | `—` | `—` | `rsl` | rusų gestų kalba | Russian Sign Language |
| `RUN` | `rn` | `run` | `run` | `run` | kirundi | Kirundi |
| `RUP` | `—` | `rup` | `rup` | `rup` | — | Aromanian; Arumanian; Macedo-Romanian |
| `RUS` | `ru` | `rus` | `rus` | `rus` | rusų kalba | Russian |
| `SAD` | `—` | `sad` | `sad` | `sad` | — | Sandawe |
| `SAG` | `sg` | `sag` | `sag` | `sag` | sangų kalba | Sango |
| `SAH` | `—` | `sah` | `sah` | `sah` | — | Yakut |
| `SAI` | `—` | `sai` | `sai` | `sai` | — | South American Indian languages |
| `SAL` | `—` | `sal` | `sal` | `sal` | — | Salishan languages |
| `SAM` | `—` | `sam` | `sam` | `sam` | — | Samaritan Aramaic |
| `SAN` | `sa` | `san` | `san` | `san` | sanskritas | Sanskrit |
| `SAS` | `—` | `sas` | `sas` | `sas` | — | Sasak |
| `SAT` | `—` | `sat` | `sat` | `sat` | — | Santali |
| `SCN` | `—` | `scn` | `scn` | `scn` | — | Sicilian |
| `SCO` | `—` | `sco` | `sco` | `sco` | škotų kalba | Scots |
| `SCZ` | `—` | `—` | `—` | `scz` | šetlandiečių | Shaetlan |
| `SDB` | `—` | `—` | `—` | `sdb` | šabakų | Shabak |
| `SDF` | `—` | `—` | `—` | `sdf` | sarlių | Sarli |
| `SDH` | `—` | `—` | `—` | `sdh` | pietų kurdų | Southern Kurdish |
| `SDL` | `—` | `—` | `—` | `sdl` | Saudo Arabijos gestų kalba | Saudi Arabian Sign Language |
| `SEH` | `—` | `—` | `—` | `seh` | senų | Sena |
| `SEL` | `—` | `sel` | `sel` | `sel` | — | Selkup |
| `SEM` | `—` | `sem` | `sem` | `sem` | — | Semitic languages |
| `SFS` | `—` | `—` | `—` | `sfs` | Pietų Afrikos gestų kalba | South African Sign Language |
| `SGA` | `—` | `sga` | `sga` | `sga` | — | Irish, Old (to 900) |
| `SGG` | `—` | `—` | `—` | `sgg` | Šveicarijos vokiečių gestų kalba | Swiss-German Sign Language |
| `SGN` | `—` | `sgn` | `sgn` | `sgn` | ženklų kalbos | Sign Languages |
| `SGX` | `—` | `—` | `—` | `sgx` | sieraleoniečių gestų kalba | Sierra Leonean Sign Language |
| `SHN` | `—` | `shn` | `shn` | `shn` | — | Shan |
| `SID` | `—` | `sid` | `sid` | `sid` | — | Sidamo |
| `SIN` | `si` | `sin` | `sin` | `sin` | sinhalų kalba | Sinhala |
| `SIO` | `—` | `sio` | `sio` | `sio` | — | Siouan languages |
| `SIP` | `—` | `—` | `—` | `sip` | sikimiečių | Sikkimese |
| `SIT` | `—` | `sit` | `sit` | `sit` | — | Sino-Tibetan languages |
| `SJC` | `—` | `—` | `—` | `sjc` | Šaodziango kinų | Shaojiang Chinese |
| `SKQ` | `—` | `—` | `—` | `skq` | sininkerių | Sininkere |
| `SLA` | `—` | `sla` | `sla` | `sla` | slavų kalbos | Slavic languages |
| `SLF` | `—` | `—` | `—` | `slf` | Šveicarijos italų gestų kalba | Swiss-Italian Sign Language |
| `SLK` | `sk` | `slo` | `slk` | `slk` | slovakų kalba | Slovak |
| `SLS` | `—` | `—` | `—` | `sls` | singapūriečių gestų kalba | Singapore Sign Language |
| `SLV` | `sl` | `slv` | `slv` | `slv` | slovėnų kalba | Slovenian |
| `SMA` | `—` | `sma` | `sma` | `sma` | — | Southern Sami |
| `SME` | `se` | `sme` | `sme` | `sme` | šiaurės samių kalba | Northern Sami |
| `SMI` | `—` | `smi` | `smi` | `smi` | — | Sami languages |
| `SMJ` | `—` | `smj` | `smj` | `smj` | — | Lule Sami |
| `SMN` | `—` | `smn` | `smn` | `smn` | — | Inari Sami |
| `SMO` | `sm` | `smo` | `smo` | `smo` | samojiečių | Samoan |
| `SMS` | `—` | `sms` | `sms` | `sms` | — | Skolt Sami |
| `SNA` | `sn` | `sna` | `sna` | `sna` | šonų | Shona |
| `SND` | `sd` | `snd` | `snd` | `snd` | — | Sindhi |
| `SNK` | `—` | `snk` | `snk` | `snk` | — | Soninke |
| `SOG` | `—` | `sog` | `sog` | `sog` | — | Sogdian |
| `SOM` | `so` | `som` | `som` | `som` | somalių kalba | Somali |
| `SON` | `—` | `son` | `son` | `son` | — | Songhai languages |
| `SOT` | `st` | `sot` | `sot` | `sot` | pietų sotų | Southern Sotho |
| `SPA` | `es` | `spa` | `spa` | `spa` | ispanų kalba | Spanish |
| `SQI` | `sq` | `alb` | `sqi` | `sqi` | albanų kalba | Albanian |
| `SQS` | `—` | `—` | `—` | `sqs` | šrilankiečių gestų kalba | Sri Lankan Sign Language |
| `SRD` | `sc` | `srd` | `srd` | `srd` | — | Sardinian |
| `SRN` | `—` | `srn` | `srn` | `srn` | — | Sranan Tongo |
| `SRP` | `sr` | `srp` | `srp` | `srp` | serbų kalba | Serbian |
| `SRQ` | `—` | `—` | `—` | `srq` | sirionų | Sirionó |
| `SRR` | `—` | `srr` | `srr` | `srr` | — | Serer |
| `SSA` | `—` | `ssa` | `ssa` | `ssa` | — | Nilo-Saharan languages |
| `SSP` | `—` | `—` | `—` | `ssp` | ispanų gestų kalba | Spanish Sign Language |
| `SSR` | `—` | `—` | `—` | `ssr` | Šveicarijos prancūzų gestų kalba | Swiss-French Sign Language |
| `SSW` | `ss` | `ssw` | `ssw` | `ssw` | svazių | Swazi |
| `SUK` | `—` | `suk` | `suk` | `suk` | — | Sukuma |
| `SUN` | `su` | `sun` | `sun` | `sun` | — | Sundanese |
| `SUS` | `—` | `sus` | `sus` | `sus` | — | Susu |
| `SUX` | `—` | `sux` | `sux` | `sux` | — | Sumerian |
| `SVK` | `—` | `—` | `—` | `svk` | slovakų gestų kalba | Slovakian Sign Language |
| `SWA` | `sw` | `swa` | `swa` | `swa` | suahilių kalba | Swahili |
| `SWB` | `—` | `—` | `—` | `swb` | komorų mahorių | Comorian |
| `SWE` | `sv` | `swe` | `swe` | `swe` | švedų kalba | Swedish |
| `SWL` | `—` | `—` | `—` | `swl` | švedų gestų kalba | Swedish Sign Language |
| `SYC` | `—` | `syc` | `syc` | `syc` | — | Classical Syriac |
| `SYR` | `—` | `syr` | `syr` | `syr` | — | Syriac |
| `SYY` | `—` | `—` | `—` | `syy` | Saido beduinų gestų kalba | Al-Sayyid Bedouin Sign Language |
| `SZL` | `—` | `—` | `—` | `szl` | sileziečių kalba | Silesian |
| `TAH` | `ty` | `tah` | `tah` | `tah` | — | Tahitian |
| `TAI` | `—` | `tai` | `tai` | `tai` | — | Tai languages |
| `TAM` | `ta` | `tam` | `tam` | `tam` | tamilų kalba | Tamil |
| `TAT` | `tt` | `tat` | `tat` | `tat` | — | Tatar |
| `TEL` | `te` | `tel` | `tel` | `tel` | — | Telugu |
| `TEM` | `—` | `tem` | `tem` | `tem` | — | Timne |
| `TER` | `—` | `ter` | `ter` | `ter` | — | Tereno |
| `TET` | `—` | `tet` | `tet` | `tet` | tetum | Tetum |
| `TGK` | `tg` | `tgk` | `tgk` | `tgk` | tadžikų kalba | Tajik |
| `TGL` | `tl` | `tgl` | `tgl` | `tgl` | — | Tagalog |
| `THA` | `th` | `tha` | `tha` | `tha` | tajų kalba | Thai |
| `TIG` | `—` | `tig` | `tig` | `tig` | — | Tigre |
| `TIR` | `ti` | `tir` | `tir` | `tir` | tigrajų kalba | Tigrinya |
| `TIV` | `—` | `tiv` | `tiv` | `tiv` | — | Tiv |
| `TKL` | `—` | `tkl` | `tkl` | `tkl` | tokelau | Tokelauan |
| `TLH` | `—` | `tlh` | `tlh` | `tlh` | — | Klingon; tlhIngan-Hol |
| `TLI` | `—` | `tli` | `tli` | `tli` | — | Tlingit |
| `TMH` | `—` | `tmh` | `tmh` | `tmh` | — | Tamashek |
| `TNA` | `—` | `—` | `—` | `tna` | takanų | Tacana |
| `TNO` | `—` | `—` | `—` | `tno` | toromonų | Toromono |
| `TOG` | `—` | `tog` | `tog` | `tog` | — | Tonga (Nyasa) |
| `TOI` | `—` | `—` | `—` | `toi` | čitonga (Zambija) | Tonga (Zambia) |
| `TON` | `to` | `ton` | `ton` | `ton` | tongų | Tongan |
| `TPI` | `—` | `tpi` | `tpi` | `tpi` | tokpisinas | Tok Pisin |
| `TPJ` | `—` | `—` | `—` | `tpj` | tapietų | Tapieté |
| `TRN` | `—` | `—` | `—` | `trn` | mochų trinitarijiečių | Trinitario |
| `TSE` | `—` | `—` | `—` | `tse` | tunisiečių gestų kalba | Tunisian Sign Language |
| `TSI` | `—` | `tsi` | `tsi` | `tsi` | — | Tsimshian |
| `TSM` | `—` | `—` | `—` | `tsm` | turkų gestų kalba | Turkish Sign Language |
| `TSN` | `tn` | `tsn` | `tsn` | `tsn` | tsvanų | Tswana |
| `TSO` | `ts` | `tso` | `tso` | `tso` | tsongų | Tsonga |
| `TSQ` | `—` | `—` | `—` | `tsq` | tajų gestų kalba | Thai Sign Language |
| `TSS` | `—` | `—` | `—` | `tss` | taivaniečių gestų kalba | Taiwanese Sign Language |
| `TSY` | `—` | `—` | `—` | `tsy` | Tebulo gestų kalba | Tebul Sign Language |
| `TUK` | `tk` | `tuk` | `tuk` | `tuk` | turkmėnų kalba | Turkmen |
| `TUM` | `—` | `tum` | `tum` | `tum` | — | Tumbuka |
| `TUP` | `—` | `tup` | `tup` | `tup` | — | Tupi languages |
| `TUR` | `tr` | `tur` | `tur` | `tur` | turkų kalba | Turkish |
| `TUT` | `—` | `tut` | `tut` | `tut` | — | Altaic languages |
| `TVI` | `—` | `—` | `—` | `tvi` | tulajų | Tulai |
| `TVL` | `—` | `tvl` | `tvl` | `tvl` | tuvaliečių | Tuvaluan |
| `TWI` | `tw` | `twi` | `twi` | `twi` | — | Twi |
| `TYV` | `—` | `tyv` | `tyv` | `tyv` | — | Tuvinian |
| `TZA` | `—` | `—` | `—` | `tza` | tanzaniečių gestų kalba | Tanzanian Sign Language |
| `TZM` | `—` | `—` | `—` | `tzm` | Vidurio Atlaso tamazigtų | Central Atlas Tamazight |
| `UDM` | `—` | `udm` | `udm` | `udm` | — | Udmurt |
| `UGA` | `—` | `uga` | `uga` | `uga` | — | Ugaritic |
| `UGN` | `—` | `—` | `—` | `ugn` | ugandiečių gestų kalba | Ugandan Sign Language |
| `UGY` | `—` | `—` | `—` | `ugy` | urugvajiečių gestų kalba | Uruguayan Sign Language |
| `UIG` | `ug` | `uig` | `uig` | `uig` | — | Uighur; Uyghur |
| `UKL` | `—` | `—` | `—` | `ukl` | ukrainiečių gestų kalba | Ukrainian Sign Language |
| `UKR` | `uk` | `ukr` | `ukr` | `ukr` | ukrainiečių kalba | Ukrainian |
| `UKS` | `—` | `—` | `—` | `uks` | Urubu-Kaapor gestų kalba | Urubú-Kaapor Sign Language |
| `UMB` | `—` | `umb` | `umb` | `umb` | — | Umbundu |
| `UND` | `—` | `und` | `und` | `und` | nenustatyta kalba | Undetermined |
| `URD` | `ur` | `urd` | `urd` | `urd` | urdu kalba | Urdu |
| `URE` | `—` | `—` | `—` | `ure` | urų | Uru |
| `UZB` | `uz` | `uzb` | `uzb` | `uzb` | uzbekų kalba | Uzbek |
| `VAI` | `—` | `vai` | `vai` | `vai` | — | Vai |
| `VEN` | `ve` | `ven` | `ven` | `ven` | vendų | Venda |
| `VIE` | `vi` | `vie` | `vie` | `vie` | vietnamiečių kalba | Vietnamese |
| `VLS` | `—` | `—` | `—` | `vls` | flamandų kalba | Flemish |
| `VOL` | `vo` | `vol` | `vol` | `vol` | — | Volapük |
| `VOT` | `—` | `vot` | `vot` | `vot` | — | Votic |
| `VSI` | `—` | `—` | `—` | `vsi` | moldavų gestų kalba | Moldovan Sign Language |
| `VSL` | `—` | `—` | `—` | `vsl` | venesueliečių gestų kalba | Venezuelan Sign Language |
| `VSN` | `—` | `—` | `—` | `vsn` | vedų kalba | Vedic Sanskrit |
| `VSV` | `—` | `—` | `—` | `vsv` | Valensijos gestų kalba | Valencian Sign Language |
| `WAK` | `—` | `wak` | `wak` | `wak` | — | Wakashan languages |
| `WAL` | `—` | `wal` | `wal` | `wal` | — | Wolaytta |
| `WAR` | `—` | `war` | `war` | `war` | — | Waray |
| `WAS` | `—` | `was` | `was` | `was` | — | Washo |
| `WEN` | `—` | `wen` | `wen` | `wen` | — | Sorbian languages |
| `WLN` | `wa` | `wln` | `wln` | `wln` | valonų kalba | Walloon |
| `WOL` | `wo` | `wol` | `wol` | `wol` | volofų kalba | Wolof |
| `WUU` | `—` | `—` | `—` | `wuu` | vu kinų | Wu Chinese |
| `XAL` | `—` | `xal` | `xal` | `xal` | — | Kalmyk; Oirat |
| `XHO` | `xh` | `xho` | `xho` | `xho` | kosų | Xhosa |
| `XKI` | `—` | `—` | `—` | `xki` | keniečių gestų kalba | Kenyan Sign Language |
| `XML` | `—` | `—` | `—` | `xml` | malajiečių gestų kalba | Malaysian Sign Language |
| `XMN` | `—` | `—` | `—` | `xmn` | manichėjų vidurinė persų | Manichaean Middle Persian |
| `XMS` | `—` | `—` | `—` | `xms` | marokiečių gestų kalba | Moroccan Sign Language |
| `YAA` | `—` | `—` | `—` | `yaa` | jaminavų | Yaminava |
| `YAO` | `—` | `yao` | `yao` | `yao` | — | Yao |
| `YAP` | `—` | `yap` | `yap` | `yap` | — | Yapese |
| `YID` | `yi` | `yid` | `yid` | `yid` | jidiš kalba | Yiddish |
| `YKH` | `—` | `—` | `—` | `ykh` | chamniganų kalba | Khamnigan Mongol |
| `YNB` | `—` | `—` | `—` | `ynb` | jambenų | Yamben |
| `YOR` | `yo` | `yor` | `yor` | `yor` | jorubų | Yoruba |
| `YPK` | `—` | `ypk` | `ypk` | `ypk` | — | Yupik languages |
| `YSL` | `—` | `—` | `—` | `ysl` | jugoslavų gestų kalba | Yugoslavian Sign Language |
| `YUE` | `—` | `—` | `—` | `yue` | Kantono kinų kalba | Yue Chinese |
| `YUQ` | `—` | `—` | `—` | `yuq` | jukių | Yuqui |
| `YUZ` | `—` | `—` | `—` | `yuz` | jurakarių | Yuracare |
| `ZAP` | `—` | `zap` | `zap` | `zap` | — | Zapotec |
| `ZBL` | `—` | `zbl` | `zbl` | `zbl` | — | Blissymbols; Blissymbolics; Bliss |
| `ZEM` | `—` | `—` | `—` | `zem` | zemų | Zeem |
| `ZEN` | `—` | `zen` | `zen` | `zen` | — | Zenaga |
| `ZGH` | `—` | `zgh` | `zgh` | `zgh` | Standartinė Maroko amazigų kalba | Standard Moroccan Tamazight |
| `ZHA` | `za` | `zha` | `zha` | `zha` | — | Zhuang |
| `ZHO` | `zh` | `chi` | `zho` | `zho` | kinų kalba | Chinese |
| `ZIB` | `—` | `—` | `—` | `zib` | zimbabviečių gestų kalba | Zimbabwean Sign Language |
| `ZLM` | `—` | `—` | `—` | `zlm` | malajų bendroji kalba | Malay |
| `ZND` | `—` | `znd` | `znd` | `znd` | — | Zande languages |
| `ZSL` | `—` | `—` | `—` | `zsl` | zambiečių gestų kalba | Zambian Sign Language |
| `ZSM` | `—` | `—` | `—` | `zsm` | standartinė malajų k. | Standard Malay |
| `ZUL` | `zu` | `zul` | `zul` | `zul` | zulų kalba | Zulu |
| `ZUN` | `—` | `zun` | `zun` | `zun` | — | Zuni |
| `ZXX` | `—` | `zxx` | `zxx` | `zxx` | kalbinio turinio nėra | No linguistic content |
| `ZZA` | `—` | `zza` | `zza` | `zza` | zazų | Zaza |

[^std-iso639]: EU Publications Office — Language Authority Table (NAL) (http://publications.europa.eu/resource/authority/language)
[^std-iso639-csv]: DataHub / ISO 639-2 Registration Authority — `language-codes-full.csv`, Public Domain Dedication and License v1.0 (`ODC-PDDL-1.0`) (https://github.com/datasets/language-codes)
