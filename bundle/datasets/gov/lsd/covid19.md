---
type: Dataset
title: "datasets/gov/lsd/covid19"
description: "Spinta dataset datasets/gov/lsd/covid19 (12 tables)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/covid19"
tags: [gov, lsd, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/covid19.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/covid19.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/lsd/covid19

- **Namespace:** `datasets/gov/lsd/covid19`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/covid19.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/covid19.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/covid19`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [AtvejaiIrMirtys](covid19/AtvejaiIrMirtys.md) | Agreguoti COVID-19 atvejai ir mirtys | `3` | — | — | 13 | Lentelė aprašo užsikrėtimų SARS-CoV-2 virusu (pirminių ir pakartotinių infekcijų) skaičius, taip pat COVID mirčių ("mirtys nuo COVID" ir "mirtys su COVID")... |
| [AtvejaiPagalDarbovietes](covid19/AtvejaiPagalDarbovietes.md) | COVID-19 atvejai pagal darbovietes | `3` | — | — | 13 | Pateikta paskutinių 14 dienų naujų COVID-19 atvejų istorija anonimizuotose įstaigose (su veiklos pobūdžio aprašymu) |
| [DarbovieciuImunizacija](covid19/DarbovieciuImunizacija.md) | Asmenų imunizacija pagal darbovietes | `3` | — | `open` | 10 | Kasdien atnaujinami darbuotojų imunizacijos nuo SARS-CoV-2 duomenys dvidešimtyje tūkstančių Lietuvos įmonių, įstaigų, organizacijų (ekonominės veiklos rūšių... |
| [LaboratorijuRezultataiEvrk](covid19/LaboratorijuRezultataiEvrk.md) | COVID-19 laboratorijų rezultatai pagal EVRK | `3` | — | — | 4 | Covid-19 diagnostinių tyrimų rezultatai, agreguoti pagal datą ir ekonominės veiklos rūšis (EVRK 2) |
| [LigoniniuDuomenys](covid19/LigoniniuDuomenys.md) | COVID-19 ligoninių duomenys | `3` | — | — | 35 | Turimos bei užimtos stacionaro lovos, deguonies tiekimu aprūpintos lovos, intensyvios terapijos ir reanimacijos skyrių lovos, dirbtinės plaučių... |
| [SvieslenciuStatistika](covid19/SvieslenciuStatistika.md) | COVID-19 statistika (švieslentės) | `3` | — | — | 31 | Pateikta iš švieslenčių (dashboards) agreguota informacija kiekvienai dienai pagal savivaldybes nuo pandemijos pradžios Lietuvoje apie atvejus, tyrimus ir... |
| [TyrimaiPadieniui](covid19/TyrimaiPadieniui.md) | COVID-19 tyrimai padieniui pagal laboratorijas | `3` | — | — | 6 | SARS-CoV-2 laboratorinių tyrimų atsakymų agreguoti pagal datą ir laboratoriją duomenys |
| [Vakcinavimas](covid19/Vakcinavimas.md) | COVID-19 vakcinavimas | `3` | — | — | 11 | Neagreguoti vakcinacijos duomenys |
| [NeigaliujuStatistika](covid19/NeigaliujuStatistika.md) | COVID-19 statistika apie asmenis su negalia | `4` | `id` | — | 36 | Pateikiami užsikrėtimų koronavirusu, skiepijimo, bendros imunizacijos, mirčių nuo COVID-19 rodikliai apibūdinantys pandemijos situaciją trijose asmenų... |
| [MokiniuImunizacija](covid19/MokiniuImunizacija.md) | Mokinių vakcinacija ir imunizacija | `3` | — | — | 17 | 12–19 metų amžiaus moksleivių skiepijimas ir imunizacija (nuo SARS-CoV-2) Lietuvos mokyklose pagal amžių Kasdien atnaujinami mokinių imunizacijos nuo... |
| [StudVakcPagalIstaigas](covid19/StudVakcPagalIstaigas.md) | Studentų vakcinacija ir imunizacija pagal aukštąsias mokymosi įstaigas | `3` | — | — | 12 | Studentų vakcinaciją ir bendrą imunizaciją nuo SARS‑CoV-2 pagal aukštąsias mokymosi įstaigas |
| [StudVakcPagalIstaigasIrProgramas](covid19/StudVakcPagalIstaigasIrProgramas.md) | Studentų vakcinacija ir imunizacija pagal įstaigas ir studijų programas | `3` | — | — | 12 | Studentų vakcinaciją ir bendrą imunizaciją nuo SARS‑CoV-2 pagal aukštąsias mokymosi įstaigas ir studijų programas |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/covid19.csv
