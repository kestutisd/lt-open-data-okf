---
type: Dataset
title: "Duomenys apie kapavietes savivaldybių kapinėse"
description: "Pateikiami suskaitmenintų Lietuvos savivaldybėms priklausančių kapinių kapaviečių duomenys iš savivaldybių CEMETY ir LIKSGIS informacinių sistemų."
resource: "https://get.data.gov.lt/datasets/gov/kapines/registras/kapavietes"
tags: [gov, kapines, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kapines/kapavietes.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/kapines/kapavietes.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2779/"
    title: "data.gov.lt DCAT-AP — datasets/gov/kapines/registras/kapavietes"
    author: "team:vda"
    last_modified: "2026-04-09T00:00:00Z"
---

# Duomenys apie kapavietes savivaldybių kapinėse

Pateikiami suskaitmenintų Lietuvos savivaldybėms priklausančių kapinių kapaviečių duomenys iš savivaldybių CEMETY ir LIKSGIS informacinių sistemų. Aprašomos kapaviečių charakteristikos: ilgis, plotis, dydis, palaidotų velionių skaičius, kapavietės vietos koordinatės bei papildomo pobūdžio informacija. Turint klausimų apie duomenų rinkinį, prašome kreiptis į Valstybės duomenų valdysenos atvėrimo komandą elektroniniu paštu atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/kapines/registras/kapavietes`[^manifest]
- **Manifest CSV:** [datasets/gov/kapines/kapavietes.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kapines/kapavietes.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kapines/registras/kapavietes` (`deployed`)[^manifest]
- **Provider:** `kapines` — Savivaldybių kapinių registro duomenys *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `50` (50 lentelių)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2779/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/kapines/registras/kapavietes`[^dcat]
- **Portal Title (`@lt`):** Savivaldybių kapinių registro duomenys[^dcat]
- **Portal Title (`@en`):** Data of the Register of Municipal Cemeteries[^dcat]
- **Issued (`dct:issued`):** `2024-09-06`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-09`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2024-09-06` .. `2026-10-05`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje pateikiami suskaitmenintų Lietuvos savivaldybėms priklausančių kapinių kapaviečių ir jose palaidotų velionių duomenys. Nurodomos kapaviečių charakteristikos: ilgis, plotis, dydis, palaidotų velionių skaičius, kapavietės WGS koordinatės, papildomo pobūdžio informacija. Taip pat pateikiamos palaidoto velionio charakteristikos: vardas, pavardė, lytis, gimimo, mirties ir palaidojimo datos, ir su jo kapaviete susiję duomenys (ryšys su kitais kapavietėje palaidotais asmenimis, kapą prižiūrinčiu asmeniu, kapo gylis, vieta bendrame kapinių plane). Duomenų teikėjas – Savivaldybės administracija. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package contains data on the digitalised graves of cemeteries belonging to the municipalities of Lithuania and the deceased buried there. The characteristics of the tombs shall be indicated: length, width, size, number of buried deceased persons, WGS coordinates of the tombs, additional information. The characteristics of the buried deceased shall also include: name, surname, sex, dates of birth, death and burial, and data relating to his tomb (contact with other persons buried in the tomb, person supervising the tomb, depth of the tomb, place in the joint cemetery plan). If you have any questions about the dataset, please contact the State Data Control Opening Team by e-mail atverimas@stat.gov.lt.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [SiauliuMiestas](kapavietes/SiauliuMiestas.md) | Šiaulių miesto savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [PalangosMiestas](kapavietes/PalangosMiestas.md) | Palangos miesto savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [SilutesRajonas](kapavietes/SilutesRajonas.md) | Šilutės rajono savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [KedainiuRajonas](kapavietes/KedainiuRajonas.md) | Kėdainių rajono savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [KlaipedosMiestas](kapavietes/KlaipedosMiestas.md) | Klaipėdos miesto savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [SilalesRajonas](kapavietes/SilalesRajonas.md) | Šilalės rajono savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [PrienuRajonas](kapavietes/PrienuRajonas.md) | Prienų rajono savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [KaunoMiestas](kapavietes/KaunoMiestas.md) | Kauno miesto savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [PlungesRajonas](kapavietes/PlungesRajonas.md) | Plungės rajono savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [KelmesRajonas](kapavietes/KelmesRajonas.md) | Kelmės rajono savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [Rietavas](kapavietes/Rietavas.md) | Rietavo savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [Druskininkai](kapavietes/Druskininkai.md) | Druskininkų savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [Kaisiadorys](kapavietes/Kaisiadorys.md) | Kaišiadorių savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [Elektrenai](kapavietes/Elektrenai.md) | Elektrėnų savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [SkuodoRajonas](kapavietes/SkuodoRajonas.md) | Skuodo rajono savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [MoletuRajonas](kapavietes/MoletuRajonas.md) | Molėtų rajono savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [PanevezioMiestas](kapavietes/PanevezioMiestas.md) | Panevėžio miesto savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [KlaipedosRajonas](kapavietes/KlaipedosRajonas.md) | Klaipėdos rajono savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [UtenosRajonas](kapavietes/UtenosRajonas.md) | Utenos rajono savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [IgnalinosRajonas](kapavietes/IgnalinosRajonas.md) | Ignalinos rajono savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [ZarasuRajonas](kapavietes/ZarasuRajonas.md) | Zarasų rajono savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [JurbarkoRajonas](kapavietes/JurbarkoRajonas.md) | Jurbarko rajono savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [Pagegiai](kapavietes/Pagegiai.md) | Pagėgių savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [PanevezioRajonas](kapavietes/PanevezioRajonas.md) | Panevėžio rajono savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [KazluRuda](kapavietes/KazluRuda.md) | Kazlų Rūdos savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [JonavosRajonas](kapavietes/JonavosRajonas.md) | Jonavos rajono savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [UkmergesRajonas](kapavietes/UkmergesRajonas.md) | Ukmergės rajono savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [MazeikiuRajonas](kapavietes/MazeikiuRajonas.md) | Mažeikių rajono savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [SalcininkuRajonas](kapavietes/SalcininkuRajonas.md) | Šalčininkų rajono savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [BirzuRajonas](kapavietes/BirzuRajonas.md) | Biržų rajono savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [TelsiuRajonas](kapavietes/TelsiuRajonas.md) | Telšių rajono savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [KaunoRajonas](kapavietes/KaunoRajonas.md) | Kauno rajono savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [Marijampole](kapavietes/Marijampole.md) | Marijampolės savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [KupiskioRajonas](kapavietes/KupiskioRajonas.md) | Kupiškio rajono savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [PakruojoRajonas](kapavietes/PakruojoRajonas.md) | Pakruojo rajono savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [Visaginas](kapavietes/Visaginas.md) | Visagino savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [SiauliuRajonas](kapavietes/SiauliuRajonas.md) | Šiaulių rajono savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [PasvalioRajonas](kapavietes/PasvalioRajonas.md) | Pasvalio rajono savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [SvencioniuRajonas](kapavietes/SvencioniuRajonas.md) | Švenčionių rajono savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [RokiskioRajonas](kapavietes/RokiskioRajonas.md) | Rokiškio rajono savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [TauragesRajonas](kapavietes/TauragesRajonas.md) | Tauragės rajono savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [SakiuRajonas](kapavietes/SakiuRajonas.md) | Šakių rajono savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [SirvintuRajonas](kapavietes/SirvintuRajonas.md) | Širvintų rajono savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [VarenosRajonas](kapavietes/VarenosRajonas.md) | Varėnos rajono savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [VilkaviskioRajonas](kapavietes/VilkaviskioRajonas.md) | Vilkaviškio rajono savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [AlytausMiestas](kapavietes/AlytausMiestas.md) | Alytaus miesto savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [JoniskioRajonas](kapavietes/JoniskioRajonas.md) | Joniškio rajono savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [TrakuRajonas](kapavietes/TrakuRajonas.md) | Trakų rajono savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [AkmenesRajonas](kapavietes/AkmenesRajonas.md) | Akmenės rajono savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `17` | — |
| [KretingosRajonas](kapavietes/KretingosRajonas.md) | Kretingos rajono savivaldybės kapinių kapaviečių duomenys | `4` | `vda_id` | — | `18` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/kapines/kapavietes.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kapines/kapavietes.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/kapines/registras/kapavietes (https://data.gov.lt/datasets/2779/)
