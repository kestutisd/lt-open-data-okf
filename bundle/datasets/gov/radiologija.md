---
type: Dataset
title: "Pacientams atlikti radiologiniai tyrimai"
description: "Asmens sveikatos priežiūros įstaigų naudojamose Rentgeno vaizdų archyvavimo informacinėse sistemose yra kaupiami pacientams atliktų radiologinių tyrimų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/radiologija"
tags: [gov, radiologija, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/radiologija/radiologija.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/radiologija/radiologija.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2762/"
    title: "data.gov.lt DCAT-AP — datasets/gov/radiologija"
    author: "team:vda"
    last_modified: "2026-10-26T00:00:00Z"
---

# Pacientams atlikti radiologiniai tyrimai

- **Namespace:** `datasets/gov/radiologija`[^manifest]
- **Manifest CSV:** [datasets/gov/radiologija/radiologija.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/radiologija/radiologija.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/radiologija` (`deployed`)[^manifest]
- **Provider:** `radiologija`[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `25` (25 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2762/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/radiologija/:all/:format/json`[^dcat]
- **Portal Title (`@lt`):** Pacientams atlikti radiologiniai tyrimai[^dcat]
- **Portal Title (`@en`):** Radiological examinations have been performed in patients at the Shadow Clinic[^dcat]
- **Issued (`dct:issued`):** `2024-08-23`[^dcat]
- **Last Modified (`dct:modified`):** `2026-10-26`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2024-08-22` .. `2026-10-29`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Asmens sveikatos priežiūros įstaigų naudojamose Rentgeno vaizdų archyvavimo informacinėse sistemose yra kaupiami pacientams atliktų radiologinių tyrimų duomenys. Priklausomai nuo įstaigos ir jos naudojamos informacinės sistemos duomenų aprėptys laike ir atnaujinimo dažniai gali skirtis, nors dauguma duomenų rinkinių atnaujinami kasdien. Į duomenų rinkinius patenka požymiai, kaip paciento pseudonimizuotas asmens kodas, tyrimo studijos identifikatorius ir data, paciento gimimo metai, lytis, svoris ir ūgis, tyrimo serijos identifikatorius, aprašymas ir modalumas, tirtos kūno dalies duomenys, medicininio atvaizdo identifikatorius, spinduliuotės dozė decigrėjais kvadratiniame centimetre, apšvita arksekundėmis ir fotometrinė interpretacija. Duomenų teikėjas – Asmens sveikatos priežiūros įstaigos. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

MedDream IS used by the Shadow Polyclinic gathers data from radiation tests performed on patients. The coverage of the data collected in time has been in place since 2021, with daily updates. The dataset consists of: patient's pseudonymised personal number, study study identifier and date, patient's birth year, sex, weight and height, test series identifier, description and modality, test portion data, medical image identifier, radiation dose in deciders per square centimetre, exposure in arctic seconds and photometric interpretation.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [ZalgirioKlinika](radiologija/ZalgirioKlinika.md) | VU ligoninės „Žalgirio klinika“ pacientams atlikti radiologiniai tyrimai | `4` | `vda_id` | — | `15` | Vilniaus universiteto ligoninės Žalgirio klinikos „MedDream“ IS kaupia duomenis apie pacientams vykdytus radiologinius tyrimus. |
| [SeskinesPoliklinika](radiologija/SeskinesPoliklinika.md) | Šeškinės poliklinikos pacientams atlikti radiologiniai tyrimai | `4` | `vda_id` | — | `16` | Šeškinės poliklinikos naudojamoje „MedDream“ IS kaupiami pacientams atliktų radiologinių tyrimų duomenys. |
| [AnyksciuRajonoLigonine](radiologija/AnyksciuRajonoLigonine.md) | Anykščių rajono ligoninės pacientams atlikti radiologiniai tyrimai | — | `vda_prime_key` | — | `13` | Anykščių rajono ligoninės naudojamoje „MedDream“ IS kaupiami pacientams atliktų radiologinių tyrimų duomenys. |
| [DruskininkuLigonine](radiologija/DruskininkuLigonine.md) | Druskininkų ligoninės pacientams atlikti radiologiniai tyrimai | — | `vda_prime_key` | — | `13` | Druskininkų ligoninės naudojamoje „MedDream“ IS kaupiami pacientams atliktų radiologinių tyrimų duomenys. |
| [RespublikinePanevezioLigonine](radiologija/RespublikinePanevezioLigonine.md) | Respublikinėje Panevėžio ligoninės pacientams atlikti radiologiniai tyrimai | — | `vda_prime_key` | — | `12` | Informacinėje sistemoje „JiveX“ kaupiami Respublikinės Panevėžio ligoninės pacientams atliktų radiologinių tyrimų duomenys. |
| [NaujosiosVilniosPoliklinika](radiologija/NaujosiosVilniosPoliklinika.md) | Naujosios Vilnios poliklinikos pacientams atlikti radiologiniai tyrimai | — | `vda_prime_key` | — | `14` | Informacinėje sistemoje „MedDream“ nuo 2013 metų kaupiami Naujosios Vilnios poliklinikos pacientams atliktų radiologinių tyrimų duomenys. |
| [IgnalinosRajonoSavivaldybesSveikatosCentras](radiologija/IgnalinosRajonoSavivaldybesSveikatosCentras.md) | Ignalinos rajono savivaldybės sveikatos centro pacientams atlikti radiologiniai tyrimai | — | `vda_prime_key` | — | `14` | Informacinėje sistemoje „MedDream“ nuo 2013 metų kaupiami Ignalinos raj. |
| [UkmergesLigonine](radiologija/UkmergesLigonine.md) | Ukmergės ligoninės pacientams atlikti radiologiniai tyrimai | — | `vda_prime_key` | — | `12` | Informacinėje sistemoje „JiveX“ kaupiami Ukmergės ligoninės pacientams atliktų radiologinių tyrimų duomenys. |
| [VisaginoLigonine](radiologija/VisaginoLigonine.md) | Visagino ligoninės pacientams atlikti radiologiniai tyrimai | — | `vda_prime_key` | — | `12` | Informacinėje sistemoje „JiveX“ kaupiami Visagino ligoninės pacientams atliktų radiologinių tyrimų duomenys. |
| [RokiskioLigonine](radiologija/RokiskioLigonine.md) | Rokiškio ligoninės pacientams atlikti radiologiniai tyrimai | — | `vda_prime_key` | — | `12` | Informacinėje sistemoje „JiveX“ kaupiami Rokiškio ligoninės pacientams atliktų radiologinių tyrimų duomenys. |
| [RespublikineSiauliuLigonine](radiologija/RespublikineSiauliuLigonine.md) | Respublikinės Šiaulių ligoninės pacientams atliktų radiologinių tyrimų duomenys | `4` | `vda_prime_key` | — | `16` | Informacinėje sistemoje „MedDream“ kaupiami Respublikinės Šiaulių ligoninės pacientams atliktų radiologinių tyrimų duomenys. |
| [SilutesLigonine](radiologija/SilutesLigonine.md) | Šilutės ligoninės pacientams atliktų radiologinių tyrimų duomenys | — | `vda_prime_key` | — | `15` | Informacinėje sistemoje „MedDream“ kaupiami Šilutės ligoninės pacientams atliktų radiologinių tyrimų duomenys. |
| [UtenosLigonine](radiologija/UtenosLigonine.md) | Utenos ligoninės pacientams atliktų radiologinių tyrimų duomenys | — | `vda_prime_key` | — | `12` | Informacinėje sistemoje „JiveX“ kaupiami Utenos ligoninės pacientams atliktų radiologinių tyrimų duomenys. |
| [PlungesLigonine](radiologija/PlungesLigonine.md) | Plungės ligoninės pacientams atliktų radiologinių tyrimų duomenys | — | `vda_prime_key` | — | `12` | Informacinėje sistemoje „JiveX“ kaupiami Plungės ligoninės pacientams atliktų radiologinių tyrimų duomenys. |
| [KaisiadoriuSSC](radiologija/KaisiadoriuSSC.md) | Kaišiadorių rajono savivaldybės sveikatos centro pacientams atliktų radiologinių tyrimų duomenys | — | `vda_prime_key` | — | `18` | Informacinėje sistemoje „CEDARA“ kaupiami Kaišiadorių raj. |
| [JurbarkoLigonine](radiologija/JurbarkoLigonine.md) | Jurbarko ligoninės pacientams atliktų radiologinių tyrimų duomenys | — | `vda_prime_key` | — | `18` | Informacinėje sistemoje „CEDARA“ kaupiami Jurbarko ligoninės pacientams atliktų radiologinių tyrimų duomenys. |
| [PasvalioLigonine](radiologija/PasvalioLigonine.md) | Pasvalio ligoninės pacientams atliktų radiologinių tyrimų duomenys | — | `vda_prime_key` | — | `18` | Informacinėje sistemoje „CEDARA“ kaupiami Pasvalio ligoninės pacientams atliktų radiologinių tyrimų duomenys. |
| [RespublikineVilniausUniversitetineLigonine](radiologija/RespublikineVilniausUniversitetineLigonine.md) | Respublikinės Vilniaus universitetinės ligoninės pacientams atliktų radiologinių tyrimų duomenys | — | `vda_prime_key` | — | `19` | Informacinėje sistemoje „MedDream“ kaupiami Respublikinės VU ligoninės pacientams atliktų radiologinių tyrimų duomenys. |
| [RegionineTelsiuLigonine](radiologija/RegionineTelsiuLigonine.md) | Regioninės Telšių ligoninės pacientams atlikti radiologiniai tyrimai | — | `vda_prime_key` | — | `12` | Informacinėje sistemoje „JiveX“ kaupiami Regioninės Telšių ligoninės pacientams atliktų radiologinių tyrimų duomenys. |
| [RegionineMazeikiuLigonine](radiologija/RegionineMazeikiuLigonine.md) | Regioninės Mažeikių ligoninės pacientams atlikti radiologiniai tyrimai | — | `vda_prime_key` | — | `12` | Informacinėje sistemoje „JiveX“ kaupiami Regioninės Mažeikių ligoninės pacientams atliktų radiologinių tyrimų duomenys. |
| [KelmesLigonine](radiologija/KelmesLigonine.md) | Kelmės ligoninės pacientams atlikti radiologiniai tyrimai | — | `vda_prime_key` | — | `12` | Informacinėje sistemoje „JiveX“ kaupiami Kelmės ligoninės pacientams atliktų radiologinių tyrimų duomenys. |
| [SakiuLigonine](radiologija/SakiuLigonine.md) | Šakių ligoninės pacientams atliktų radiologinių tyrimų duomenys | — | `vda_prime_key` | — | `18` | Informacinėje sistemoje „CEDARA“ kaupiami Šakių ligoninės pacientams atliktų radiologinių tyrimų duomenys. |
| [MykoloMarcinkeviciausLigonine](radiologija/MykoloMarcinkeviciausLigonine.md) | Mykolo Marcinkevičiaus ligoninės pacientams atliktų radiologinių tyrimų duomenys | — | `vda_prime_key` | — | `17` | Informacinėje sistemoje „MedDream“ kaupiami VšĮ Mykolo Marcinkevičiaus ligoninės pacientams atliktų radiologinių tyrimų duomenys. |
| [KazluRudosPSPC](radiologija/KazluRudosPSPC.md) | Kazlų Rūdos pirminės sveikatos priežiūros centro pacientams atlikti radiologiniai tyrimai | — | `vda_prime_key` | — | `12` | Informacinėje sistemoje „JiveX“ kaupiami Kazlų Rūdos PSPC pacientams atliktų radiologinių tyrimų duomenys. |
| [VilkaviskioLigonine](radiologija/VilkaviskioLigonine.md) | Vilkaviškio ligoninės pacientams atlikti radiologiniai tyrimai | — | `vda_prime_key` | — | `12` | Informacinėje sistemoje „JiveX“ kaupiami Vilkaviškio ligoninės pacientams atliktų radiologinių tyrimų duomenys. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/radiologija/radiologija.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/radiologija/radiologija.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/radiologija (https://data.gov.lt/datasets/2762/)
