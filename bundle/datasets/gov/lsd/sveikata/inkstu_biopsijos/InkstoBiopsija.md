---
type: Table
title: "InkstoBiopsija — Inkstų biopsijų duomenys"
description: "\"Asmenys, kuriems atlikta inkstų biopsija, gimimo data, lytis, biopsijos gavimo data, lėtinės inkstų ligos, 5 stadijos pirmo įrašo data, indikatoriai, ar pacientui nustatytos gretutinės ligos, inkstų ligų rizikos veiksniai – cukrinis diabetas ir arterinė hipertenzija..."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/inkstu_biopsijos/InkstoBiopsija"
tags: [gov, lsd, inkstobiopsija, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/inkstu_biopsijos.csv#L32"
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/inkstu_biopsijos.csv#L32"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/4573/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/inkstu_biopsijos"
    author: "team:vda"
    last_modified: "2026-03-17T00:00:00Z"
---

# InkstoBiopsija — Inkstų biopsijų duomenys

"Asmenys, kuriems atlikta inkstų biopsija, gimimo data, lytis, biopsijos gavimo data, lėtinės inkstų ligos, 5 stadijos pirmo įrašo data, indikatoriai, ar pacientui nustatytos gretutinės ligos, inkstų ligų rizikos veiksniai – cukrinis diabetas ir arterinė hipertenzija, paciento mirties data ir pagrindinė mirties priežastis. Visos datos yra pateikiamos mėnesio tikslumu."[^manifest]

- **Model:** `datasets/gov/lsd/sveikata/inkstu_biopsijos/InkstoBiopsija`[^manifest]
- **Dataset:** ["Pacientų, kuriems atlikta inkstų biopsija, duomenys"](../inkstu_biopsijos.md) (`datasets/gov/lsd/sveikata/inkstu_biopsijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sveikata/inkstu_biopsijos.csv#L32](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/inkstu_biopsijos.csv#L32)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/inkstu_biopsijos/InkstoBiopsija` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-03-17`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalios eilutės identifikatorius | "Valstybės duomenų agentūros sugeneruotas unikalios eilutės identifikatorius, kurį sudaro stulpeliai - asmens_kodas, biopsijos_data, biopsijos_kategorija, cukr_diabet, arter_hipert" |
| `asmens_kodas` | `string` | — | `4` | `open` | — | Asmens kodas | — |
| `gimimo_data` | `date` | `M` | `4` | `open` | — | Gimimo data (mėnesio tikslumu) | — |
| `lytis` | `string` | — | `4` | `open` | — | Lytis | — |
| `biopsijos_data` | `date` | `M` | `4` | `open` | — | Biopsijos gavimo data (mėnesio tikslumu) | — |
| `biopsijos_kategorija` | `string` | — | `4` | `open` | — | Inkstų biopsijos diagnostinė kategorija | — |
| `pirma_inkst_lig_diag` | `date` | `M` | `4` | `open` | — | Pirma inkstų ligos diagnozė | "Lėtinės inkstų ligos, 5 stadijos (N18.5 TLK-10-AM) kodo pirmo įrašymo data (mėnesio tikslumu)" |
| `cukr_diabet` | `boolean` | — | `4` | `open` | — | Cukrinis diabetas | "Indikatorius, ar asmeniui yra kada nors įrašyta cukrinio diabeto diagnozė (E10-E14 TLK-10-AM)" |
| `arter_hipert` | `boolean` | — | `4` | `open` | — | Arterinė hipertenzija | "Indikatorius, ar asmeniui yra kada nors įrašyta arterinės hipertenzijos diagnozė (I10-I15 TLK-10-AM)" |
| `mirties_data` | `date` | `M` | `4` | `open` | — | Mirties data (mėnesio tikslumu) | — |
| `mirties_priez` | `string` | — | `4` | `open` | — | Mirties priežastis | Mirties atvejų ir jų priežasčių valstybės registre pagal Pasaulio sveikatos organizacijos taisykles išrinkta oficialiojoje statistikoje naudojama pagrindinė mirties priežastis |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"vyras"` | — | — | Vyras | — |
| `lytis` | `"moteris"` | — | — | Moteris | — |
| `lytis` | `"nežinoma"` | — | — | Nežinoma | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/inkstu_biopsijos.csv#L32 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/inkstu_biopsijos.csv#L32)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/sveikata/inkstu_biopsijos (https://data.gov.lt/datasets/4573/)
