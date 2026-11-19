---
type: Dataset
title: "Vidaus vandenų e-navigacinių žemėlapių informacija"
description: "Šiame viename rinkinyje pateikiama vidaus vandenų kelių e-navigacinių žemėlapių informacija."
resource: "https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai"
tags: [gov, vvkd, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/vvkd/e_zemelapiai.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1983/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vvkd/e_zemelapiai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Vidaus vandenų e-navigacinių žemėlapių informacija

Šiame viename rinkinyje pateikiama vidaus vandenų kelių e-navigacinių žemėlapių informacija. Rinkinyje galima rasti gylų, ženklų, trasų, objektų ir kita geoerdvinė bei papildoma informacija.[^manifest]

- **Namespace:** `datasets/gov/vvkd/e_zemelapiai`[^manifest]
- **Manifest CSV:** [datasets/gov/vvkd/e_zemelapiai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai` (`deployed`)[^manifest]
- **Provider:** `vvkd` — AB Vidaus vandens kelių direkcija *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `20` (20 lentelių)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/1983/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vvkd/e_zemelapiai`[^dcat]
- **Portal Title (`@lt`):** E-navigacinių žemėlapių informacija[^dcat]
- **Portal Title (`@en`):** E-navigation map information[^dcat]
- **Issued (`dct:issued`):** `2022-08-01`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2024-03-28` .. `2026-09-14`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Šiame plačios apimties rinkinyje pateikiama vidaus vandens kelių e-navigacinių žemėlapių duomenys. Rinkinyje galima rasti gylių, ženklų, trasų, objektų ir kitos geoerdvinės informacijos. Farvaterių garantinių savybių ir ribų duomenys, gyliai, pločiai, posūkio spinduliai ir panašiai pateikiami šiame įsakyme: https://e-seimas.lrs.lt/portal/legalAct/lt/TAD/TAIS.359274/asr Lietuvoje vidaus vandenyse vadovaujamasi Europos vidaus vandens laivybos taisyklėmis. Taisyklės prieinamos šios nuorodos pagalba: https://unece.org/transport/publications/cevni-european-code-inland-waterways-rev6 Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^dcat]

### Portal Description (`@en`)

Depths of inland waterways, markings, bridges, airlines, ports, piers, slips, fuel tanks are presented https://vvkd.lt/vandenu-keliai/interaktyvus-navigaciniai-zemelapiai/[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [BunaNauja](e_zemelapiai/BunaNauja.md) | Naujų bunų geoerdviniai duomenys | `4` | `fid` | — | `4` | Šiame sluoksnyje pateikiamos Nemune esančios bunos. |
| [GylisBuja](e_zemelapiai/GylisBuja.md) | Bujų geoerdviniai duomenys | `4` | `fid` | — | `7` | Šiame sluoksnyje pateikiami Bujų duomenys Nemune. |
| [GylisDruskininkaiNevezisVilnius](e_zemelapiai/GylisDruskininkaiNevezisVilnius.md) | Gylių duomenys | `4` | `fid` | — | `8` | Šiame sluoksnyje pateikiami gylių duomenis Nemune Druskininkuose, Neryje Vilniuje ir Nevėžyje. |
| [GylisKaunasKursiuMarios](e_zemelapiai/GylisKaunasKursiuMarios.md) | Gylių duomenys | `4` | `fid` | — | `8` | Šiame sluoksnyje pateikiami gylių duomenys Nemune nuo Birštono iki Kauno, Nemune nuo Kauno iki Kuršių marių, Kuršių mariose, Klaipėdos kanale, Minijoje nuo... |
| [GylisLankytinaVieta](e_zemelapiai/GylisLankytinaVieta.md) | Lankytinų vietų geoerdviniai duomenys | `4` | `objectid` | — | `3` | Šiame sluoksnyje pateikiamos vidaus vandenų keliuose esančios lankytinos vietos (uostai, prieplaukos ir pan. |
| [JettyOrPier](e_zemelapiai/JettyOrPier.md) | Duomenys apie prieplaukas | `4` | `fid` | — | `7` | Šiame sluoksnyje pateikiami duomenys apie prieplaukas Nemune nuo Baltarusijos pasienio iki Kauno. |
| [KaunasAugustowWFL1AugustowKanalSluz](e_zemelapiai/KaunasAugustowWFL1AugustowKanalSluz.md) | Augustavo kanalo geoerdviniai duomenys | `4` | `objectid` | — | `4` | Šiame sluoksnyje pateikiami Augustavo kanalo šliuzų geoerdviniai duomenys. |
| [KaunasAugustowWFL1JettyOrPiers](e_zemelapiai/KaunasAugustowWFL1JettyOrPiers.md) | Prieplaukos | `4` | `objectid` | — | `4` | Šiame sluoksnyje pateikiamos Nemuno upėje nuo Baltarusijos iki Kauno esančios prieplaukos |
| [KaunasAugustowWFL1WaterwayKaunasAugustow](e_zemelapiai/KaunasAugustowWFL1WaterwayKaunasAugustow.md) | Vandens kelio Kaunas Augustavas geoerdviniai duomenys | `4` | `objectid` | — | `6` | Šiame sluoksnyje pateikiami Vandens kelio Kaunas Augustavas geoerdviniai duomenys. |
| [Lock](e_zemelapiai/Lock.md) | Šliuzų vietos | `4` | `fid` | — | `5` | Šiame sluoksnyje pateikiami Augustavo kanalo šliuzai atkarpoje nuo Augustavo (Lenkija) iki Nemuno (Baltarusija). |
| [NekeltiBangu5](e_zemelapiai/NekeltiBangu5.md) | Ženklo "Nekelti bangų" galiojimo zonos | `4` | `fid` | — | `6` | Šiame sluoksnyje pateikiamos ženklo "Nekelti bangų" galiojimo zonos Minijoje Mingės kaime ir Sakūčiuose. |
| [PasienioRuozas](e_zemelapiai/PasienioRuozas.md) | Pasienio ruožo leidimų duomenys | `4` | `fid` | — | `8` | Šiame sluoksnyje pateikiami pasienio ruožo leidimų duomenys Kuršių mariose Lietuva – Rusija pasienyje. |
| [RusijosFederacija](e_zemelapiai/RusijosFederacija.md) | Rusijos Federacijos riba | `4` | `fid` | — | `6` | Šiame sluoksnyje pateikiama pasienio ruožo Lietuva – Rusija zona ties Nemunu. |
| [SenaBunaIrJosLiekana](e_zemelapiai/SenaBunaIrJosLiekana.md) | Senų būnu ir jų liekanų geoerdviniai duomenys | `4` | `fid` | — | `4` | Šiame sluoksnyje pateikiami senų būnu ir jų liekanų geoerdviniai duomenys Nemune atkarpoje nuo Jurbarko iki Nemuno žiočių. |
| [Sliuzas](e_zemelapiai/Sliuzas.md) | Vandens kelių šliužų duomenys | `4` | `fid` | — | `6` | Šiame sluoksnyje pateikiami vandens kelių šliužų duomenys |
| [SvarbiInformacija](e_zemelapiai/SvarbiInformacija.md) | Svarbios informacijos duomenys | `4` | `fid` | — | `4` | Šiame sluoksnyje pateikiami svarbios informacijos duomenys, informaciniai pranešimai ir pan. |
| [TuristineTrasa](e_zemelapiai/TuristineTrasa.md) | Turistinės trasos duomenys | `4` | `fid` | — | `5` | Šiame sluoksnyje pateikiami turistinės trasos geoerdviniai duomenys Nemune nuo Druskininkų iki Birštono. |
| [WaterwayKaunasAugustow](e_zemelapiai/WaterwayKaunasAugustow.md) | Vandens kelio Kaunas - Augustavas geoerdviniai duomenys | `4` | `fid` | — | `8` | Šiame sluoksnyje pateikiami vandens kelio Kaunas - Augustavas geoerdviniai duomenys. |
| [Zenklas](e_zemelapiai/Zenklas.md) | Vandens kelių ženklų informaciniai duomenys | `4` | `fid` | — | `7` | Šiame sluoksnyje pateikiami vidaus vandenų kelių ženklų geoerdviniai duomenys, pavadinimai, tipai ir pan. |
| [ZenklasVilnius](e_zemelapiai/ZenklasVilnius.md) | Vandens kelių ženklų informaciniai duomenys | `4` | `fid` | — | `6` | Šiame sluoksnyje pateikiami vidaus vandenų kelių ženklų geoerdviniai duomenys, pavadinimai, tipai ir pan. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vvkd/e_zemelapiai.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vvkd/e_zemelapiai.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vvkd/e_zemelapiai (https://data.gov.lt/datasets/1983/)
