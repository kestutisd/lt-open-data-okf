---
type: Reference
title: "Lietuvos valiutos istorija, euro įvedimo kursas (1 EUR = 3,45280 LTL) ir ISO 4217 kodai"
description: "Lietuvos euro įvedimo (2015-01-01) fiksuotas kursas 1 EUR = 3.45280 LTL pagal Reglamentą (ES) Nr. 851/2014, apvalinimo taisyklės (Reg. (EB) Nr. 1103/97), LTL / LTT / SUR laikotarpiai ir 291 kodas."
resource: "https://publications.europa.eu/resource/celex/32014R0851"
tags: [standards, currency, eur, ltl, iso-4217, valiuta, reference]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: std-eur
    resource: "https://publications.europa.eu/resource/celex/32014R0851"
    title: "Council Regulation (EU) No 851/2014 amending Regulation (EC) No 2866/98 as regards the conversion rate to the euro for Lithuania"
    author: "team:eu-publications-office"
    last_modified: "2014-07-23T00:00:00Z"
  - id: std-eur-1103
    resource: "https://publications.europa.eu/resource/celex/31997R1103"
    title: "Council Regulation (EC) No 1103/97 on certain provisions relating to the introduction of the euro (Articles 4–5)"
    author: "team:eu-publications-office"
    last_modified: "1997-06-19T00:00:00Z"
  - id: std-lt-euro-law
    resource: "https://www.e-tar.lt/portal/lt/legalAct/dad7f330cca211e387b1ebf12f4d03f3"
    title: "Lietuvos Respublikos euro įvedimo Lietuvos Respublikoje įstatymas (2014-04-17 Nr. XII-828)"
    author: "team:lr-seimas"
    last_modified: "2014-04-17T00:00:00Z"
  - id: std-eu-currency
    resource: "http://publications.europa.eu/resource/authority/currency"
    title: "EU Publications Office — Currency Authority Table (NAL)"
    author: "team:eu-publications-office"
  - id: std-iso4217-csv
    resource: "https://github.com/datasets/currency-codes"
    title: "DataHub / SIX Group ISO 4217 Maintenance Agency — codes-all.csv (ODC-PDDL-1.0)"
    author: "team:frictionless-datasets"
---

# Lietuvos valiutos istorija ir ISO 4217 valiutų klasifikatorius

Šis informacinis konceptas (`type: Reference`) apibrėžia Lietuvos Respublikos piniginių vienetų chronologiją, neatšaukiamą euro įvedimo kursą, privalomas ES bei nacionalines perskaičiavimo ir apvalinimo taisykles bei **ISO 4217** valiutų kodus daugiamečių finansinių laiko eilučių analizei.[^std-eur][^std-eur-1103][^std-lt-euro-law][^std-eu-currency][^std-iso4217-csv]

## 1. Euro įvedimas Lietuvoje (`2015-01-01`), fiksuotas kursas ir patvirtintas skaičiavimas

Pagal 2014 m. liepos 23 d. **Tarybos reglamentą (ES) Nr. 851/2014** (`CELEX:32014R0851`), nuo **2015-01-01** Lietuvos oficiali valiuta yra **euras (`EUR`)**, pakeitęs **Lietuvos litą (`LTL`)** neatšaukiamai fiksuotu perskaičiavimo kursu:[^std-eur]

> **`1 EUR = 3.45280 LTL`**

- **6 reikšminių skaitmenų perskaičiavimo ir matematinio apvalinimo taisyklė:** Vadovaujantis **Tarybos reglamento (EB) Nr. 1103/97** (`CELEX:31997R1103`) 4–5 straipsniais ir **Lietuvos Respublikos euro įvedimo Lietuvos Respublikoje įstatymo** (Nr. XII-828) nuostatomis, perskaičiavimui privaloma naudoti nesutrumpintą 6 reikšminių skaitmenų kursą (`3.45280`, negalima naudoti apvalinto atvirkštinio koeficiento `0.28962`): lito (`LTL`) suma dalijama iš `3.45280` ir gauta euro (`EUR`) piniginė suma matematiškai apvalinama iki **2 skaitmenų po kablelio** (`ROUND_HALF_UP` — jei trečiasis skaitmuo po kablelio yra `5` ar didesnis, pridedamas vienas euro centas).[^std-eur-1103][^std-lt-euro-law]
- **Patvirtintas OKF v0.3 skaičiavimas (`Attested Computation`):** Konvertuojant istorines `LTL` reikšmes naudokite [Statutory LTL to EUR Currency Conversion](../computations/ltl-to-eur-conversion.md), kuris vykdo tikslų `decimal.Decimal` dalybos ir `ROUND_HALF_UP` apvalinimo algoritmą su deterministiniu kvito tikrintuvu.[^std-eur][^std-eur-1103]

## 2. Istoriniai Lietuvos valiutų laikotarpiai (ISO 4217)

| ISO 4217 kodas | Skaitinis kodas | Valiutos pavadinimas (LT / EN) | Galiojimo laikotarpis Lietuvoje | Pastabos ir perskaičiavimas |
| --- | --- | --- | --- | --- |
| `SUR` | `810` | SSRS rublis / USSR Rouble | iki `1992-09-30` (ES NAL: `1991-12-31`) | Sovietinis rublis; Lietuvoje išimtas iš apyvartos nuo `1992-10-01` (ES NAL bendra SSRS pabaigos data `1991-12-31`).[^std-eu-currency][^std-iso4217-csv] |
| `LTT` | `440` | Lietuvos talonas / Lithuanian Talonas | `1991-08-05` – `1993-06-24` | Laikinasis piniginis vienetas (nuo `1992-10-01` vienintelė teisėta mokėjimo priemonė iki lito įvedimo; keistas santykiu `1 LTL = 100 LTT`).[^std-iso4217-csv] |
| `LTL` | `440` | Lietuvos litas / Lithuanian Litas | `1993-06-25` – `2014-12-31` | Nacionalinė valiuta; nuo `2002-02-02` susieta su euru santykiu `1 EUR = 3.45280 LTL`.[^std-eur][^std-lt-euro-law] |
| `EUR` | `978` | Euras / Euro | nuo `2015-01-01` | Oficiali Lietuvos Respublikos valiuta (`1 EUR = 3.45280 LTL`).[^std-eur] |

## 3. Kritinė daugiamečių finansinių duomenų agregavimo taisyklė

> **Įspėjimas agentams ir analitikams:** Atvirų duomenų lentelėse, kuriose laiko eilutės prasideda iki **2015-01-01** (pvz., viešųjų pirkimų sutarčių vertės, biudžeto išlaidos, mokesčiai, įstatinis kapitalas ar žalos sumos be atskiro valiutos stulpelio arba su tuščiu `Ref`), būtina patikrinti, ar istorinės (iki `2014-12-31`) reikšmės šaltinyje jau perskaičiuotos į `EUR`, ar paliktos nominaliais `LTL` (arba `LTT`/`SUR`). Tiesioginis neperskaičiuotų `LTL` ir `EUR` eilučių sumavimas (`SUM`) iškreipia iki 2015 m. sumas `3.45280` karto — konvertavimui naudokite [Statutory LTL to EUR Currency Conversion](../computations/ltl-to-eur-conversion.md).[^std-eur][^std-eur-1103][^std-lt-euro-law]

## 4. ES leidinių biuro ir ISO 4217 valiutų kodų sąrašas (291 kodas)

> **Pastaba dėl šaltinių:** Valiutų pavadinimai (LT/EN) ir galiojimo datos pateikiami iš ES leidinių biuro `currency` autoritetinės lentelės (`http://publications.europa.eu/resource/authority/currency`), o skaitiniai ISO 4217 kodai sujungti iš atvirojo `https://github.com/datasets/currency-codes` rinkinio (`ODC-PDDL-1.0`, sudaryto pagal SIX Group ISO 4217 agentūros lenteles).[^std-eu-currency][^std-iso4217-csv]

| Kodas | ISO 4217 skaitinis | Pavadinimas (LT) | Title (EN) | Pradžios data | Pabaigos data |
| --- | --- | --- | --- | --- | --- |
| `ADF` | `—` | — | Andorran franc | `1990-01-01` | `1999-01-01` |
| `ADP` | `020` | Andoros peseta | Andorran peseta | `1990-01-01` | `1999-01-01` |
| `AED` | `784` | JAE dirhamas | UAE dirham | `1990-01-01` | `active` |
| `AFA` | `004` | Afganis | Afghani | `1925-01-01` | `2002-12-31` |
| `AFN` | `971` | Afganis | Afghani | `2003-01-01` | `active` |
| `ALK` | `008` | Lekas | Lek | `1926-01-01` | `1992-12-31` |
| `ALL` | `008` | Lekas | Lek | `1993-01-01` | `active` |
| `AMD` | `051` | Dramas | Dram | `1993-11-22` | `active` |
| `ANG` | `532` | Olandijos Antilų guldenas | Netherlands Antillean guilder | `1990-01-01` | `2025-07-01` |
| `AOA` | `973` | Kvanza | Kwanza | `2000-01-01` | `active` |
| `AON` | `024` | Naujoji Angolos kvanza | New Angolan kwanza | `1990-01-01` | `1999-12-31` |
| `AOR` | `982` | Angolos kwanza rejustado | Angolan kwanza readjustado | `1996-01-01` | `1999-12-31` |
| `ARA` | `032` | Argentinos australis | Argentine austral | `1985-06-15` | `1991-12-31` |
| `ARL` | `—` | — | Argentine peso ley | `1970-01-01` | `1983-05-05` |
| `ARM` | `—` | Argentinos nacionalinė valiuta pesas | Argentine peso moneda nacional | `1952-07-25` | `1969-12-31` |
| `ARP` | `032` | Argentinos pesas | Argentine peso argentino | `1983-05-06` | `1985-06-14` |
| `ARS` | `032` | Argentinos pesas | Argentine peso | `1992-01-01` | `active` |
| `ARY` | `032` | Argentinos pesas ley | Argentine peso ley | `1970-01-01` | `1983-05-05` |
| `ATS` | `040` | Austrijos šilingas | Austrian schilling | `1952-07-25` | `1999-01-01` |
| `AUD` | `036` | Australijos doleris | Australian dollar | `1990-01-01` | `active` |
| `AWG` | `533` | Arubos guldenas | Aruban guilder | `1986-01-01` | `active` |
| `AZM` | `031` | Azerbaidžano manatas | Azerbaijani manat | `1992-08-15` | `2005-12-31` |
| `AZN` | `944` | Azerbaidžano manatas | Azerbaijan manat | `2006-01-01` | `active` |
| `BAM` | `977` | Konvertuojamoji markė | Convertible mark | `1995-01-01` | `active` |
| `BBD` | `052` | Barbadoso doleris | Barbados dollar | `1990-01-01` | `active` |
| `BDT` | `050` | Taka | Taka | `1990-01-01` | `active` |
| `BEF` | `056` | Belgijos frankas | Belgian franc | `1952-07-25` | `1999-01-01` |
| `BGJ` | `100` | Levas | Lev | `1947-01-01` | `1951-12-31` |
| `BGK` | `100` | Levas | Lev | `1952-01-01` | `1961-12-31` |
| `BGL` | `100` | Levas | Lev | `1962-01-01` | `1999-07-04` |
| `BGN` | `975` | Levas | Lev | `1999-07-05` | `2026-01-01` |
| `BHD` | `048` | Bahreino dinaras | Bahraini dinar | `1990-01-01` | `active` |
| `BIF` | `108` | Burundžio frankas | Burundi franc | `1990-01-01` | `active` |
| `BMD` | `060` | Bermudos doleris | Bermuda dollar | `1990-01-01` | `active` |
| `BND` | `096` | Brunėjaus doleris | Brunei dollar | `1990-01-01` | `active` |
| `BOB` | `068` | Bolivianas | Boliviano | `1987-01-01` | `active` |
| `BOP` | `068` | Bolivijos pesas | Bolivian peso | `1963-01-01` | `1986-12-31` |
| `BOV` | `984` | Mvdol | Mvdol | `1987-01-01` | `active` |
| `BRB` | `076` | Kruzeiro novas | Cruzeiro novo | `1967-01-01` | `1985-12-31` |
| `BRC` | `076` | Kruzadas | Cruzado | `1986-01-01` | `1989-01-14` |
| `BRE` | `076` | Kruzeiras | Cruzeiro | `1990-03-16` | `1993-07-31` |
| `BRL` | `986` | Realas | Real | `1994-01-01` | `active` |
| `BRN` | `076` | Kruzado novas | Cruzado novo | `1989-01-15` | `1990-03-15` |
| `BRR` | `987` | Kruzeiro realas | Cruzeiro real | `1993-08-01` | `1993-12-31` |
| `BRZ` | `—` | Kruzeiras | Cruzeiro | `1952-07-25` | `1967-12-31` |
| `BSD` | `044` | Bahamų doleris | Bahamian dollar | `1990-01-01` | `active` |
| `BTN` | `064` | Ngultrumas | Ngultrum | `1990-01-01` | `active` |
| `BWP` | `072` | Pula | Pula | `1990-01-01` | `active` |
| `BYN` | `933` | Baltarusijos rublis | Belarusian rouble | `2016-07-01` | `active` |
| `BYR` | `974` | Baltarusijos rublis | Belarusian rouble | `1992-05-01` | `2016-12-31` |
| `BZD` | `084` | Belizo doleris | Belize dollar | `1990-01-01` | `active` |
| `CAD` | `124` | Kanados doleris | Canadian dollar | `1950-01-01` | `active` |
| `CDF` | `976` | Kongo frankas | Congolese franc | `1998-01-01` | `active` |
| `CHE` | `947` | WIR euras | WIR Euro | `2001-01-01` | `active` |
| `CHF` | `756` | Šveicarijos frankas | Swiss franc | `1990-01-01` | `active` |
| `CHW` | `948` | WIR frankas | WIR Franc | `1934-01-01` | `active` |
| `CLE` | `—` | Čilės eskudas | Chilean escudo | `1960-01-01` | `1975-09-29` |
| `CLF` | `990` | Unidad de Fomento | Unidad de Fomento | `1967-01-20` | `active` |
| `CLP` | `152` | Čilės pesas | Chilean peso | `1975-09-30` | `active` |
| `CNY` | `156` | Ženminbi juanis | Renminbi-yuan | `1990-01-01` | `active` |
| `COP` | `170` | Kolumbijos pesas | Colombian peso | `1990-01-01` | `active` |
| `COU` | `970` | Unidad de Valor Real | Unidad de Valor Real | `2000-01-01` | `active` |
| `CRC` | `188` | Kosta Rikos kolonas | Costa Rican colon | `1990-01-01` | `active` |
| `CSJ` | `203` | Čekoslovakijos krona | Czechoslovak koruna | `1945-01-01` | `1953-12-31` |
| `CSK` | `200` | Čekoslovakijos krona | Czechoslovak koruna | `1954-01-01` | `1993-02-07` |
| `CUC` | `931` | Konvertuojamasis pesas | Convertible peso | `1990-01-01` | `2021-06-30` |
| `CUP` | `192` | Kubos pesas | Cuban peso | `1990-01-01` | `active` |
| `CVE` | `132` | Žaliojo Kyšulio eskudas | Cabo Verde escudo | `1990-01-01` | `active` |
| `CYP` | `196` | Kipro svaras | Cypriot pound | `1952-07-25` | `2007-12-31` |
| `CZK` | `203` | Čekijos krona | Czech koruna | `1993-02-08` | `active` |
| `DDM` | `278` | Rytų Vokietijos markė | East-German Mark | `1948-06-21` | `1990-07-01` |
| `DEM` | `276` | Vokietijos markė | German mark | `1952-07-25` | `2001-12-31` |
| `DJF` | `262` | Džibučio frankas | Djibouti franc | `1990-01-01` | `active` |
| `DKK` | `208` | Danijos krona | Danish krone | `1990-01-01` | `active` |
| `DOP` | `214` | Dominikos pesas | Dominican peso | `1990-01-01` | `active` |
| `DZD` | `012` | Alžyro dinaras | Algerian dinar | `1990-01-01` | `active` |
| `ECS` | `218` | Ekvadoro sukrė | Ecuadorian sucre | `1952-07-25` | `2000-12-31` |
| `EEK` | `233` | Estijos krona | Estonian kroon | `1992-06-20` | `2010-12-31` |
| `EGP` | `818` | Egipto svaras | Egyptian pound | `1990-01-01` | `active` |
| `ERN` | `232` | Nakfa | Nakfa | `1997-11-08` | `active` |
| `ESP` | `724` | Peseta | Peseta | `1952-07-25` | `1998-12-31` |
| `ETB` | `230` | Biras | Birr | `1990-01-01` | `active` |
| `EUR` | `978` | Euras | Euro | `1999-01-01` | `active` |
| `FIM` | `246` | Suomijos markė | Finnish markka | `1952-07-25` | `1999-01-01` |
| `FJD` | `242` | Fidžio doleris | Fiji dollar | `1990-01-01` | `active` |
| `FKP` | `238` | Folklando Salų svaras | Falkland Islands pound | `1990-01-01` | `active` |
| `FRF` | `250` | Prancūzijos frankas | French franc | `1960-01-01` | `1999-01-01` |
| `GBP` | `826` | Svaras sterlingų | Pound sterling | `1990-01-01` | `active` |
| `GEL` | `981` | Laris | Lari | `1994-04-05` | `active` |
| `GHC` | `288` | Sedis | Cedi | `1967-01-01` | `2006-06-30` |
| `GHS` | `936` | Ganos sedis | Ghana cedi | `2007-07-01` | `active` |
| `GIP` | `292` | Gibraltaro svaras | Gibraltar pound | `1990-01-01` | `active` |
| `GMD` | `270` | Dalasis | Dalasi | `1990-01-01` | `active` |
| `GNE` | `324` | Sylis | Syli | `1971-12-01` | `1985-12-31` |
| `GNF` | `324` | Gvinėjos frankas | Guinean franc | `1986-01-01` | `active` |
| `GQE` | `226` | Ekvelė | Ekwele | `1975-01-01` | `1985-12-31` |
| `GRD` | `300` | Drachma | Drachma | `1964-01-01` | `2000-12-31` |
| `GTQ` | `320` | Ketcalis | Quetzal | `1990-01-01` | `active` |
| `GWP` | `624` | Bisau Gvinėjos pesas | Guinea-Bissau peso | `1975-01-01` | `1997-12-31` |
| `GYD` | `328` | Gajanos doleris | Guyana dollar | `1990-01-01` | `active` |
| `HKD` | `344` | Honkongo doleris | Hong Kong dollar | `1990-01-01` | `active` |
| `HNL` | `340` | Lempira | Lempira | `1990-01-01` | `active` |
| `HRK` | `191` | Kuna | Kuna | `1994-05-30` | `2023-01-14` |
| `HTG` | `332` | Gurdas | Gourde | `1990-01-01` | `active` |
| `HUF` | `348` | Forintas | Forint | `1949-08-18` | `active` |
| `IDR` | `360` | Rupija | Rupiah | `1990-01-01` | `active` |
| `IEP` | `372` | Airijos svaras | Irish pound | `1952-07-25` | `1999-01-01` |
| `ILP` | `376` | Izraelio lira | Israeli lira | `1948-01-01` | `1980-02-23` |
| `ILR` | `376` | Šekelis | Shekel | `1980-02-24` | `1985-12-31` |
| `ILS` | `376` | Šekelis | Shekel | `1986-01-01` | `active` |
| `INR` | `356` | Indijos rupija | Indian rupee | `1990-01-01` | `active` |
| `IQD` | `368` | Irako dinaras | Iraqi dinar | `1990-01-01` | `active` |
| `IRR` | `364` | Irano rialas | Iranian rial | `1990-01-01` | `active` |
| `ISJ` | `352` | Islandijos senoji krona | Icelandic old króna | `1918-01-01` | `1981-12-31` |
| `ISK` | `352` | Islandijos krona | Iceland króna | `1982-01-01` | `active` |
| `ITL` | `380` | Italijos lira | Italian lira | `1952-07-25` | `1999-01-01` |
| `JMD` | `388` | Jamaikos doleris | Jamaica dollar | `1990-01-01` | `active` |
| `JOD` | `400` | Jordanijos dinaras | Jordanian dinar | `1990-01-01` | `active` |
| `JPY` | `392` | Jena | Yen | `1990-01-01` | `active` |
| `KES` | `404` | Kenijos šilingas | Kenyan shilling | `1990-01-01` | `active` |
| `KGS` | `417` | Somas | Som | `1993-05-10` | `active` |
| `KHR` | `116` | Rielis | Riel | `1990-01-01` | `active` |
| `KMF` | `174` | Komorų frankas | Comorian franc | `1990-01-01` | `active` |
| `KPW` | `408` | Šiaurės Korėjos vonas | North Korean won | `1990-01-01` | `active` |
| `KRW` | `410` | Pietų Korėjos vonas | South Korean won | `1990-01-01` | `active` |
| `KWD` | `414` | Kuveito dinaras | Kuwaiti dinar | `1990-01-01` | `active` |
| `KYD` | `136` | Kaimanų Salų doleris | Cayman Islands dollar | `1990-01-01` | `active` |
| `KZT` | `398` | Tengė | Tenge | `1993-11-15` | `active` |
| `LAJ` | `418` | Kipas | Kip | `1976-01-01` | `1979-12-16` |
| `LAK` | `418` | Kipas | Kip | `1979-12-17` | `active` |
| `LBP` | `422` | Libano svaras | Lebanese pound | `1990-01-01` | `active` |
| `LKR` | `144` | Šri Lankos rupija | Sri Lankan rupee | `1990-01-01` | `active` |
| `LRD` | `430` | Liberijos doleris | Liberian dollar | `1990-01-01` | `active` |
| `LSL` | `426` | Lotis | Loti | `1990-01-01` | `active` |
| `LTL` | `440` | Litas | Litas | `1993-06-25` | `2014-12-31` |
| `LTT` | `440` | Lietuvos talonas | Lithuanian talonas | `1991-08-05` | `1993-06-24` |
| `LUF` | `442` | Liuksemburgo frankas | Luxembourg franc | `1952-07-25` | `1999-01-01` |
| `LVL` | `428` | Latas | Lats | `1993-01-01` | `2013-12-31` |
| `LYD` | `434` | Libijos dinaras | Libyan dinar | `1990-01-01` | `active` |
| `MAD` | `504` | Maroko dirhamas | Moroccan dirham | `1960-01-01` | `active` |
| `MCF` | `—` | — | Monegasque franc | `1960-01-01` | `1999-01-01` |
| `MDL` | `498` | Moldovos lėja | Moldovan leu | `1993-11-29` | `active` |
| `MGA` | `969` | Ariaris | Ariary | `2005-01-01` | `active` |
| `MGF` | `450` | Malagasių frankas | Malagasy franc | `1963-07-01` | `2004-12-31` |
| `MKD` | `807` | Denaras | Denar | `1994-01-01` | `active` |
| `MKN` | `—` | — | Denar A/93 | `1990-01-01` | `1993-12-31` |
| `MLF` | `466` | Malio frankas | Mali franc | `1962-01-01` | `1984-11-30` |
| `MMK` | `104` | Kiatas | Kyat | `1990-01-01` | `active` |
| `MNT` | `496` | Tugrikas | Tugrik | `1990-01-01` | `active` |
| `MOP` | `446` | Pataka | Pataca | `1952-06-16` | `active` |
| `MRO` | `478` | Ugija | Ouguiya | `1990-01-01` | `2018-06-30` |
| `MRU` | `929` | Ugija | Ouguiya | `2018-01-01` | `active` |
| `MTL` | `470` | Maltos lira | Maltese lira | `1972-01-01` | `2007-12-31` |
| `MTP` | `470` | Maltos svaras | Maltese pound | `1952-07-25` | `1971-12-31` |
| `MUR` | `480` | Mauricijaus rupija | Mauritian rupee | `1990-01-01` | `active` |
| `MVQ` | `462` | Maldyvų rupija | Maldive rupee | `1961-02-01` | `1983-01-21` |
| `MVR` | `462` | Rufija | Rufiyaa | `1983-01-22` | `active` |
| `MWK` | `454` | Malavio kvača | Malawian kwacha | `1990-01-01` | `active` |
| `MXN` | `484` | Meksikos pesas | Mexican peso | `1994-01-01` | `active` |
| `MXP` | `484` | Meksikos pesas | Mexican peso | `1990-01-01` | `1993-12-31` |
| `MXV` | `979` | Meksikos Unidad de Inversion | Mexican Unidad de Inversion | `1995-01-01` | `active` |
| `MYR` | `458` | Ringitas | Ringgit | `1990-01-01` | `active` |
| `MZM` | `508` | Metikalis | Metical | `1980-01-01` | `2006-06-30` |
| `MZN` | `943` | Metikalis | Metical | `2006-07-01` | `active` |
| `NAD` | `516` | Namibijos doleris | Namibian dollar | `1991-04-30` | `active` |
| `NFD` | `—` | Niufaundlando doleris | Newfoundland dollar | `1865-01-01` | `1949-12-31` |
| `NGN` | `566` | Naira | Naira | `1990-01-01` | `active` |
| `NIO` | `558` | Kordobos oras | Córdoba oro | `1990-01-01` | `active` |
| `NLG` | `528` | Nyderlandų guldenas | Netherlands guilder | `1952-07-25` | `1998-12-31` |
| `NOK` | `578` | Norvegijos krona | Norwegian krone | `1990-01-01` | `active` |
| `NPR` | `524` | Nepalo rupija | Nepalese rupee | `1990-01-01` | `active` |
| `NZD` | `554` | Naujosios Zelandijos doleris | New Zealand dollar | `1990-01-01` | `active` |
| `OMR` | `512` | Omano rialas | Omani rial | `1990-01-01` | `active` |
| `PAB` | `590` | Balboja | Balboa | `1990-01-01` | `active` |
| `PEH` | `604` | Solis | Sol | `1952-07-25` | `1985-01-31` |
| `PEI` | `604` | Inti | Inti | `1985-02-01` | `1991-12-31` |
| `PEN` | `604` | Solis | Sol | `1992-01-01` | `active` |
| `PGK` | `598` | Kina | Kina | `1990-01-01` | `active` |
| `PHP` | `608` | Filipinų pesas | Philippine peso | `1990-01-01` | `active` |
| `PKR` | `586` | Pakistano rupija | Pakistani rupee | `1990-01-01` | `active` |
| `PLN` | `985` | Zlotas | Zloty | `1995-01-01` | `active` |
| `PLZ` | `616` | Zlotas | Zloty | `1950-01-01` | `1994-12-31` |
| `PTE` | `620` | Portugalijos eskudas | Portuguese escudo | `1911-05-22` | `1999-01-01` |
| `PYG` | `600` | Gvaranis | Guaraní | `1990-01-01` | `active` |
| `QAR` | `634` | Kataro rialas | Qatari rial | `1990-01-01` | `active` |
| `ROL` | `642` | Rumunijos lėja | Romanian leu | `1952-01-28` | `2005-06-30` |
| `RON` | `946` | Rumunijos lėja | Romanian leu | `2005-07-01` | `active` |
| `RSD` | `941` | Serbijos dinaras | Serbian dinar | `2003-07-03` | `active` |
| `RUB` | `643` | Rusijos rublis | Russian rouble | `1998-01-01` | `active` |
| `RUR` | `810` | Rusijos rublis | Russian rouble | `1992-01-01` | `1997-12-31` |
| `RWF` | `646` | Ruandos frankas | Rwandese franc | `1990-01-01` | `active` |
| `SAR` | `682` | Saudo Arabijos rialas | Saudi riyal | `1990-01-01` | `active` |
| `SBD` | `090` | Saliamono Salų doleris | Solomon Islands dollar | `1990-01-01` | `active` |
| `SCR` | `690` | Seišelių rupija | Seychelles rupee | `1990-01-01` | `active` |
| `SDD` | `736` | Sudano dinaras | Sudanese dinar | `1992-06-08` | `2007-01-10` |
| `SDG` | `938` | Sudano svaras | Sudanese pound | `2008-01-01` | `active` |
| `SEK` | `752` | Švedijos krona | Swedish krona | `1990-01-01` | `active` |
| `SGD` | `702` | Singapūro doleris | Singapore dollar | `1990-01-01` | `active` |
| `SHP` | `654` | Šv. Elenos svaras | Saint Helena pound | `1990-01-01` | `active` |
| `SIT` | `705` | Tolaras | Slovenian tolar | `1991-10-08` | `2007-01-01` |
| `SKK` | `703` | Slovakijos krona | Slovak koruna | `1993-02-08` | `2009-01-01` |
| `SLE` | `925` | Leonė | Leone | `2022-07-01` | `active` |
| `SLL` | `694` | Leonė | Leone | `1990-01-01` | `2023-03-31` |
| `SML` | `—` | — | San Marinese lira | `1952-07-25` | `1999-01-01` |
| `SOS` | `706` | Somalio šilingas | Somali shilling | `1995-01-01` | `active` |
| `SQS` | `—` | Somalilando šilingas | Somaliland shilling | `1994-01-01` | `1994-01-02` |
| `SRD` | `968` | Surinamo doleris | Surinamese dollar | `2005-01-01` | `active` |
| `SRG` | `740` | Suriname guldenas | Suriname guilder | `1990-01-01` | `2004-12-31` |
| `SSP` | `728` | Pietų Sudano svaras | South Sudanese pound | `2011-07-18` | `active` |
| `STD` | `678` | Dobra | Dobra | `1990-01-01` | `2018-06-30` |
| `STN` | `930` | Dobra | Dobra | `2018-01-01` | `active` |
| `SUR` | `810` | Sovietų Sąjungos rublis | Soviet Union rouble | `1961-01-01` | `1991-12-31` |
| `SVC` | `222` | Salvadoro kolonas | Salvadorian colón | `1919-01-01` | `active` |
| `SYP` | `760` | Sirijos svaras | Syrian pound | `1990-01-01` | `active` |
| `SZL` | `748` | Lilangenis | Lilangeni | `1990-01-01` | `active` |
| `THB` | `764` | Batas | Baht | `1990-01-01` | `active` |
| `TJR` | `762` | Tadžikistano rublis | Tajikistani rouble | `1995-05-10` | `2000-10-29` |
| `TJS` | `972` | Somonis | Somoni | `2000-10-30` | `active` |
| `TMM` | `795` | Turkmėnistano manatas | Turkmen manat | `1993-10-27` | `2008-12-31` |
| `TMT` | `934` | Turkmėnistano manatas | Turkmen manat | `2009-01-01` | `active` |
| `TND` | `788` | Tuniso dinaras | Tunisian dinar | `1990-01-01` | `active` |
| `TOP` | `776` | Panga | Pa’anga | `1990-01-01` | `active` |
| `TPE` | `626` | Portugalijos Timoro eskudas | Portuguese Timorese escudo | `1959-01-01` | `1976-12-31` |
| `TRL` | `792` | Turkijos lira | Turkish lira | `1990-01-01` | `2005-12-31` |
| `TRY` | `949` | Turkijos lira | Turkish lira | `2006-01-01` | `active` |
| `TTD` | `780` | Trinidado ir Tobago doleris | Trinidad and Tobago dollar | `1990-01-01` | `active` |
| `TVD` | `—` | — | Tuvaluan dollar | `1976-01-01` | `1976-01-02` |
| `TWD` | `901` | Naujasis Taivano doleris | New Taiwan dollar | `1990-01-01` | `active` |
| `TZS` | `834` | Tanzanijos šilingas | Tanzanian shilling | `1990-01-01` | `active` |
| `UAH` | `980` | Grivina | Hryvnia | `1996-09-02` | `active` |
| `UAK` | `804` | Karbovanecas | Karbovanets | `1992-01-10` | `1996-09-01` |
| `UGS` | `800` | Ugandos šilingas | Uganda shilling | `1966-01-01` | `1987-05-31` |
| `UGX` | `800` | Ugandos šilingas | Uganda shilling | `1987-06-01` | `active` |
| `USD` | `840` | JAV doleris | US dollar | `1990-01-01` | `active` |
| `USN` | `997` | JAV doleris | US dollar | `1990-01-01` | `active` |
| `USS` | `998` | JAV doleris | US dollar | `1990-01-01` | `2014-03-01` |
| `UYI` | `940` | Urugvajaus Peso en Unidades Indexadas | Uruguay Peso en Unidades Indexadas | `2002-06-01` | `active` |
| `UYN` | `858` | Senasis Urugvajaus pesas | Uruguay old peso | `1990-01-01` | `1993-03-01` |
| `UYU` | `858` | Urugvajaus pesas | Uruguayan peso | `1993-03-02` | `active` |
| `UYW` | `927` | Unidad Previsional | Unidad Previsional | `2002-06-01` | `active` |
| `UZS` | `860` | Sumas | Sum | `1994-07-01` | `active` |
| `VAL` | `—` | — | Vatican lira | `1952-07-25` | `1999-01-01` |
| `VEB` | `862` | Fuerte bolivaras | Bolívar fuerte | `1990-01-01` | `2007-12-31` |
| `VED` | `926` | Skaitmeninis bolivaras | Bolívar digital | `2021-10-01` | `active` |
| `VEF` | `937` | Bolivaras | Bolívar | `2008-01-01` | `2018-08-20` |
| `VES` | `928` | Bolivaras soberanas | Bolívar soberano | `2018-08-20` | `active` |
| `VNC` | `704` | Senasis dongas | Old dong | `1978-05-03` | `1978-12-31` |
| `VND` | `704` | Dongas | Dong | `1979-01-01` | `active` |
| `VUV` | `548` | Vatu | Vatu | `1990-01-01` | `active` |
| `WST` | `882` | Tala | Tala | `1990-01-01` | `active` |
| `XAF` | `950` | CFA frankas (BEAC) | CFA franc (BEAC) | `1990-01-01` | `active` |
| `XAG` | `961` | Sidabras | Silver | `1978-01-01` | `active` |
| `XAU` | `959` | Auksas | Gold | `1978-01-01` | `active` |
| `XBA` | `955` | Obligacijų rinkų apskaitos vienetas: Europos valiutų sudėtinis vienetas (EURCO) | Bond Markets Unit European Composite Unit (EURCO) | `1973-01-01` | `active` |
| `XBB` | `956` | Obligacijų rinkų apskaitos vienetas: Europos pinigų sąjungos vienetas (E.M.U.-6) | Bond Markets Unit European Monetary Unit (E.M.U.-6) | `1973-01-01` | `active` |
| `XBC` | `957` | Obligacijų rinkų apskaitos vienetas: Europos sąskaitų 9 vienetas (E.U.A.-9) | Bond Markets Unit European Unit of Account 9 (E.U.A.-9) | `1973-01-01` | `active` |
| `XBD` | `958` | Obligacijų rinkų apskaitos vienetas: Europos sąskaitų 17 vienetas (E.U.A.-17) | Bond Markets Unit European Unit of Account 17 (E.U.A.-17) | `1999-01-01` | `active` |
| `XBT` | `—` | Bitkoinas | Bitcoin | `2009-01-09` | `active` |
| `XCD` | `951` | Rytų Karibų doleris | East Caribbean dollar | `1965-01-01` | `active` |
| `XCG` | `532` | Karibų guldenas | Caribbean guilder | `2025-03-31` | `active` |
| `XDR` | `960` | SST (specialiosios skolinimosi teisės) | SDR (Special Drawing Right) | `1974-07-01` | `active` |
| `XEU` | `954` | Europos valiutos vienetas | European Currency Unit | `1979-03-13` | `1999-01-01` |
| `XOF` | `952` | CFA frankas (BCEAO) | CFA Franc (BCEAO) | `1962-01-01` | `active` |
| `XPD` | `964` | Paladis | Palladium | `1978-01-01` | `active` |
| `XPF` | `953` | CFP frankas | CFP franc | `1990-01-01` | `active` |
| `XPT` | `962` | Platina | Platinum | `1978-01-01` | `active` |
| `XSU` | `994` | Sucre | Sucre | `2010-01-01` | `active` |
| `XTS` | `963` | Kodas skirtas testavimo tikslams | Code reserved for testing purposes | `1987-01-01` | `active` |
| `XUA` | `965` | APB apskaitos vienetas | ADB Unit of Account | `2011-04-07` | `active` |
| `XXX` | `999` | Valiutos nėra | No currency | `1987-01-01` | `active` |
| `YDD` | `720` | Pietų Jemeno dinaras | South Yemeni dinar | `1990-01-01` | `1996-06-11` |
| `YER` | `886` | Jemeno rialas | Yemeni rial | `1996-06-12` | `active` |
| `YUD` | `890` | Jugoslavijos dinaras | Yugoslav dinar | `1966-01-01` | `1989-12-31` |
| `YUF` | `—` | Jugoslavijos dinaras | Yugoslav dinar | `1944-01-01` | `1965-12-31` |
| `YUG` | `—` | — | Yugoslav dinar | `1994-01-01` | `1994-01-23` |
| `YUM` | `891` | Jugoslavijos dinaras | Yugoslav dinar | `1994-01-24` | `2003-07-02` |
| `YUN` | `890` | Jugoslavijos dinaras | Yugoslav dinar | `1990-01-01` | `1992-06-30` |
| `YUO` | `—` | — | Yugoslav dinar | `1993-10-01` | `1993-12-31` |
| `YUR` | `—` | — | Yugoslav dinar | `1992-07-01` | `1993-09-30` |
| `YUS` | `—` | Jugoslavijos dinaras | Yugoslav dinar | `1941-01-01` | `1943-12-31` |
| `ZAR` | `710` | Randas | Rand | `1990-01-01` | `active` |
| `ZMK` | `894` | Zambijos kvača | Zambian kwacha | `1990-01-01` | `2012-12-31` |
| `ZMW` | `967` | Zambijos kvača | Zambian kwacha | `2013-01-01` | `active` |
| `ZRN` | `180` | Naujasis Zairo zairas | Zaïrean new zaïre | `1993-01-01` | `1997-12-31` |
| `ZRZ` | `180` | Zairo zairas | Zaïrean zaïre | `1967-01-01` | `1992-12-31` |
| `ZWC` | `716` | Rodezijos doleris | Rhodesian dollar | `1970-02-17` | `1980-04-17` |
| `ZWD` | `716` | Zimbabvės doleris | Zimbabwe dollar | `1980-04-18` | `2006-07-31` |
| `ZWG` | `924` | Zimbabvės auksas | Zimbabwe Gold | `2024-06-25` | `active` |
| `ZWL` | `932` | Zimbabvės doleris | Zimbabwe dollar | `2009-02-03` | `2024-08-31` |
| `ZWN` | `942` | Zimbabvės doleris | Zimbabwe dollar | `2006-08-01` | `2008-07-31` |
| `ZWR` | `935` | Zimbabvės doleris | Zimbabwe dollar | `2008-08-01` | `2009-02-02` |

[^std-eur]: Council Regulation (EU) No 851/2014 amending Regulation (EC) No 2866/98 as regards the conversion rate to the euro for Lithuania (https://publications.europa.eu/resource/celex/32014R0851)
[^std-eur-1103]: Council Regulation (EC) No 1103/97 on certain provisions relating to the introduction of the euro, Articles 4–5 (https://publications.europa.eu/resource/celex/31997R1103)
[^std-lt-euro-law]: Lietuvos Respublikos euro įvedimo Lietuvos Respublikoje įstatymas, 2014-04-17 Nr. XII-828 (https://www.e-tar.lt/portal/lt/legalAct/dad7f330cca211e387b1ebf12f4d03f3)
[^std-eu-currency]: EU Publications Office — Currency Authority Table (NAL) (http://publications.europa.eu/resource/authority/currency)
[^std-iso4217-csv]: DataHub / SIX Group ISO 4217 Maintenance Agency — `codes-all.csv`, Public Domain Dedication and License v1.0 (`ODC-PDDL-1.0`) (https://github.com/datasets/currency-codes)
