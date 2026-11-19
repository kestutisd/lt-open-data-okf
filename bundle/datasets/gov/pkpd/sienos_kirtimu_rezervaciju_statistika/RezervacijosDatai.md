---
type: Table
title: "RezervacijosDatai — Krovininių transporto priemonių rezervacijų kirsti Lietuvos Respublikos sieną statistika"
description: "Lentelėje pateikiama krovininių transporto priemonių rezervacijų kirsti Lietuvos Respublikos sieną statistika iš Pasienio kontrolės punktų direkcijos (PKPD) eilių valdymo informacinės sistemos (EVIS)."
resource: "https://get.data.gov.lt/datasets/gov/pkpd/sienos_kirtimu_rezervaciju_statistika/RezervacijosDatai"
tags: [gov, pkpd, rezervacijosdatai, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pkpd/sienos_kirtimu_rezervaciju_statistika.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/pkpd/sienos_kirtimu_rezervaciju_statistika.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3850/"
    title: "data.gov.lt DCAT-AP — datasets/gov/pkpd/sienos_kirtimu_rezervaciju_statistika"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# RezervacijosDatai — Krovininių transporto priemonių rezervacijų kirsti Lietuvos Respublikos sieną statistika

Lentelėje pateikiama krovininių transporto priemonių rezervacijų kirsti Lietuvos Respublikos sieną statistika iš Pasienio kontrolės punktų direkcijos (PKPD) eilių valdymo informacinės sistemos (EVIS). Duomenys kaupiami nuo 2013 metų ir atnaujinami kas mėnesį. Svarbu paminėti, kad lentelėje baigtų rezervacijų skaičiai apima tiek sėkmingai įgyvendintas rezervacijas (kai transporto priemonė pervažiuoja iš laukimo aikštelės į pasienio kontrolės punktą), tiek atšauktas, neįvykdytas rezervacijas. Dėl techninių klausimų ar klaidų galima kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/pkpd/sienos_kirtimu_rezervaciju_statistika/RezervacijosDatai`[^manifest]
- **Dataset:** [Krovininių transporto priemonių rezervacijų kirsti Lietuvos Respublikos sieną statistika](../sienos_kirtimu_rezervaciju_statistika.md) (`datasets/gov/pkpd/sienos_kirtimu_rezervaciju_statistika`)[^manifest]
- **Manifest CSV:** [datasets/gov/pkpd/sienos_kirtimu_rezervaciju_statistika.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pkpd/sienos_kirtimu_rezervaciju_statistika.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/pkpd/sienos_kirtimu_rezervaciju_statistika/RezervacijosDatai` (`deployed`)[^manifest]
- **Provider:** `pkpd` — Pasienio kontrolės punktų direkcija prie Susisiekimo ministerijos *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `iraso_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `punkto_pav` | `string` | — | `4` | `open` | — | Pasienio kontrolės punkto pavadinimas | — |
| `data` | `date` | `D` | `4` | `open` | — | Data, kuriai rezervuotas sienos kirtimas | — |
| `trukme_iki_sienos` | `integer` | — | `4` | `open` | — | Trukmė (minutėmis) iki sienos | — |
| `transporto_priemones_kategorija` | `string` | — | `4` | `open` | — | Transporto priemonės kategorija | — |
| `rezervacijos_ge` | `integer` | `U` | `4` | `open` | — | Baigtų rezervacijų skaičius (gyva eilė) | — |
| `rezervacijos_ir` | `integer` | `U` | `4` | `open` | — | Baigtų rezervacijų skaičius (išankstinė rezervacija) | — |
| `rezervacijos_pe` | `integer` | `U` | `4` | `open` | — | Baigtų rezervacijų skaičius (prioritetinė eilė) | — |
| `rezervacijos_viso` | `integer` | `U` | `4` | `open` | — | Baigtų rezervacijų skaičius (viso) | — |
| `sekmingi_ge` | `integer` | `U` | `4` | `open` | — | Krovininių transporto priemonių, sėkmingai pervažiavusių iš laukimo aikštelės į pasienio punktą, skaičius (gyva eilė) | — |
| `sekmingi_ir` | `integer` | `U` | `4` | `open` | — | Krovininių transporto priemonių, sėkmingai pervažiavusių iš laukimo aikštelės į pasienio punktą, skaičius (išankstinė rezervacija) | — |
| `sekmingi_pe` | `integer` | `U` | `4` | `open` | — | Krovininių transporto priemonių, sėkmingai pervažiavusių iš laukimo aikštelės į pasienio punktą, skaičius (prioritetinė eilė) | — |
| `sekmingi_viso` | `integer` | `U` | `4` | `open` | — | Krovininių transporto priemonių, sėkmingai pervažiavusių iš laukimo aikštelės į pasienio punktą, skaičius (viso) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pkpd/sienos_kirtimu_rezervaciju_statistika.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pkpd/sienos_kirtimu_rezervaciju_statistika.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/pkpd/sienos_kirtimu_rezervaciju_statistika (https://data.gov.lt/datasets/3850/)
