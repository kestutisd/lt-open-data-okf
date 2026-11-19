---
type: Table
title: "HidrografijaLinija — Sluoksnyje saugoma informacija apie upių, upelių, kanalų ir melioracijos griovių ašines linijas"
description: "Specifikacija - https://e-tar.lt/portal/lt/legalAct/c53d28609d7811eea5a28c81c82193a8"
resource: "https://get.data.gov.lt/datasets/gov/giscentras/grpk/HidrografijaLinija"
tags: [gov, giscentras, hidrografijalinija, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/giscentras/grpk.csv#L104"
    title: "atviriduomenys/manifest — datasets/gov/giscentras/grpk.csv#L104"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1302/"
    title: "data.gov.lt DCAT-AP — datasets/gov/giscentras/grpk"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# HidrografijaLinija — Sluoksnyje saugoma informacija apie upių, upelių, kanalų ir melioracijos griovių ašines linijas

**Dataset Context:** Specifikacija - https://e-tar.lt/portal/lt/legalAct/c53d28609d7811eea5a28c81c82193a8[^manifest]

- **Model:** `datasets/gov/giscentras/grpk/HidrografijaLinija`[^manifest]
- **Dataset:** [Georeferencinio pagrindo kadastro erdviniai duomenys](../grpk.md) (`datasets/gov/giscentras/grpk`)[^manifest]
- **Manifest CSV:** [datasets/gov/giscentras/grpk.csv#L104](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/giscentras/grpk.csv#L104)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/giscentras/grpk/HidrografijaLinija` (`deployed`)[^manifest]
- **Provider:** `giscentras` — VĮ Žemės ūkio duomenų centras (buv. VĮ „GIS-Centras“) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `top_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `top_id` | `string` | — | `4` | `open` | — | Objekto identifikavimo kodas (reikšmė yra privaloma) | — |
| `gkodas` | `string` | — | `4` | `open` | — | Erdvinio objekto kodas (reikšmė yra privaloma) | — |
| `meta` | `string` | — | `4` | `open` | — | Raktas į GRPK rinkinio sluoksnio metaduomenų lenteles | — |
| `red_priezastis` | `string` | — | `4` | `open` | — | Objekto duomenų ir informacijos sukūrimo ar paskutinio pakeitimo priežastis (reikšmė yra privaloma įvedus naują ar patikslinus esamo objekto duomenis ir informaciją) | — |
| `red_saltinis` | `string` | — | `4` | `open` | — | Objekto duomenims sukurti, nustatyti ar pakeisti naudotas duomenų šaltinis. Galimos reikšmės | — |
| `suk_data` | `datetime` | `L` | `4` | `open` | — | Objekto įregistravimo (sukūrimo) data (reikšmė yra privaloma) | — |
| `red_data` | `datetime` | `L` | `4` | `open` | — | Objekto duomenų ir informacijos keitimo data (reikšmė yra privaloma patikslinus esamo objekto duomenis ir informaciją) | — |
| `graktas` | `string` | — | `4` | `open` | — | Vandentakio kodas pagal Lietuvos Respublikos upių klasifikatorių. | — |
| `tipas` | `integer` | — | `4` | `open` | — | Vandentakio tipas (įvedama skaitinė reikšmė) | — |
| `vardas` | `string` | — | `4` | `open` | — | Hidrografijos objekto pavadinimas | — |
| `plotis` | `number` | `m` | `4` | `open` | — | Hidrografijos objekto plotis ar hidrotechninio statinio plotis metrais | — |
| `plotis_v` | `number` | `m` | `4` | `open` | — | Vidutinis vandens lygio hidrotechniniame statinyje plotis metrais | — |
| `laivyb` | `string` | — | `4` | `open` | — | Laivybinė upė/kanalas | — |
| `shape_length` | `number` | `m` | `4` | `open` | — | Objekto perimetro ilgis | — |
| `shape` | `geometry(multilinestring, 3346)` | — | `4` | `open` | — | Objekto geometrijos tipas | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `gkodas` | `"hc1"` | — | — | Upių ašinės linijos – per vidurį išilgai upių, platesnių nei 12 m, einančios menamos linijos | — |
| `gkodas` | `"fhc1"` | — | — | Fiktyvios upių linijos – upių, platesnių nei 12 m, einančių per ežerus ir tvenkinius, ir atitinkamų diukerių menamos linijos | — |
| `gkodas` | `"hc3"` | — | — | Hidrotechninių statinių ašinės linijos – per vidurį išilgai hidrotechninių statinių, platesnių nei 12 m, einančios menamos linijos | — |
| `gkodas` | `"fhc3"` | — | — | Fiktyvios hidrotechninių statinių linijos – hidrotechninių statinių, einančių per ežerus, tvenkinius, kūdras, ir atitinkamų diukerių menamos linijos | — |
| `gkodas` | `"hc31"` | — | — | Siauresnių kaip 2 m natūralios tėkmės upių ir hidrotechninių statinių ašinės linijos – per vidurį išilgai siauresnių kaip 2 m natūralios tėkmės upių ir hidrotechninių statinių einančios menamos linijos | — |
| `gkodas` | `"hc32"` | — | — | 3–5 m pločio natūralios tėkmės upių ir hidrotechninių statinių ašinės linijos – per vidurį išilgai 3–5 m pločio natūralios tėkmės upių ir hidrotechninių statinių einančios menamos linijos | — |
| `gkodas` | `"hc33"` | — | — | 6–12 m pločio natūralios tėkmės upių ir hidrotechninių statinių ašinės linijos – per vidurį išilgai 6–12 m pločio natūralios tėkmės upių ir hidrotechninių statinių einančios menamos linijos | — |
| `gkodas` | `"op0"` | — | — | Vamzdinių vandens pralaidų ašinės linijos – per vidurį išilgai vamzdinių vandens pralaidų (paprastai esančių po keliais) einančios menamos linijos | — |
| `gkodas` | `"hc1op0"` | — | — | Vamzdinių vandens pralaidų ašinės linijos – per vidurį išilgai vamzdinių vandens pralaidų (paprastai esančių po keliais) einančios menamos linijos | — |
| `gkodas` | `"hc31op0"` | — | — | Vamzdinių vandens pralaidų ašinės linijos – per vidurį išilgai vamzdinių vandens pralaidų (paprastai esančių po keliais) einančios menamos linijos | — |
| `gkodas` | `"hc32op0"` | — | — | Vamzdinių vandens pralaidų ašinės linijos – per vidurį išilgai vamzdinių vandens pralaidų (paprastai esančių po keliais) einančios menamos linijos | — |
| `gkodas` | `"hc33op0"` | — | — | Vamzdinių vandens pralaidų ašinės linijos – per vidurį išilgai vamzdinių vandens pralaidų (paprastai esančių po keliais) einančios menamos linijos | — |
| `gkodas` | `"hc3op0"` | — | — | Vamzdinių vandens pralaidų ašinės linijos – per vidurį išilgai vamzdinių vandens pralaidų (paprastai esančių po keliais) einančios menamos linijos | — |
| `gkodas` | `"op01"` | — | — | Kanalizuotų upių, tekančių vamzdinėmis vandens pralaidomis, ašinės linijos – per vidurį išilgai kanalizuotų upių, kurių vanduo teka vamzdinėmis pralaidomis, einančios menamos linijos | — |
| `tipas` | `1` | — | — | upė (natūrali vandens tėkmė, srovė, tekanti sausumos paviršiumi savo pačios išgraužta vaga) | — |
| `tipas` | `2` | — | — | kanalas (dirbtinis paviršinis vandens telkinys su nuolatine vandens tėkme, įrengiamas grunte iškasant ar įrengiant atvirą vagą, kurios pradžia ir pabaiga jungiasi su kitu paviršiniu vandens telkiniu (upe, ežeru, Kuršių mariomis arba tvenkiniu), skirtas vandeniui tiekti drėkinimo, hidroenergetikos, vandentiekos ir kitoms reikmėms, naudoti laivybai ir pan. Sureguliuotos upės nelaikomos kanalais | — |
| `tipas` | `3` | — | — | griovys (hidrotechninis statinys, įrengiamas iškasant atvirą vagą grunte ir skirtas pertekliniam vandeniui nuleisti. Sureguliuotos upės nelaikomos grioviais) | — |
| `tipas` | `-9999` | — | — | kai netinka nė viena iš reikšmių | — |
| `laivyb` | `"L"` | — | — | laivybinė (požymis priskiriamas pagal VĮ Vidaus vandens kelių direkcijos pateiktą informaciją) | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vardas` | `update(property: "vardas@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/giscentras/grpk.csv#L104 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/giscentras/grpk.csv#L104)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/giscentras/grpk (https://data.gov.lt/datasets/1302/)
