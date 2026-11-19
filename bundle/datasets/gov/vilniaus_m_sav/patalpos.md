---
type: Dataset
title: "Vilniaus miesto savivaldybės nuomojamų patalpų sutarčių duomenys"
description: "Rinkinyje skelbiami Vilniaus miesto savivaldybės nuomojamų patalpų duomenys iš „Active Vilnius“ nuomos sistemos."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/patalpos"
tags: [gov, vilniaus_m_sav, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/patalpos.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/patalpos.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3859/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/patalpos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Vilniaus miesto savivaldybės nuomojamų patalpų sutarčių duomenys

Rinkinyje skelbiami Vilniaus miesto savivaldybės nuomojamų patalpų duomenys iš „Active Vilnius“ nuomos sistemos. Platformoje kaupiama informacija apie nuomojamus aktyvaus laisvalaikio objektus: sporto ir aktų sales, kabinetus, žaidimo ir sporto aikšteles bei kita. Šias laisvalaikio zonas nuomoti gali fiziniai bei juridiniai asmenys. Rinkinyje pateikiami duomenys apie nuomojamas patalpas, nuomotojus, esamus ir buvusius nuomininkus bei išrašytas sąskaitas-faktūras už naudojimąsi paslaugomis. Nuomos įkainiai ir mokėtinos sumos sąskaitose už suteiktas paslaugas nėra skelbiami, tačiau viešinamas reitingas, kur mokėtinos sumos išrikiuojamos eilės tvarka nuo didžiausios iki mažiausios. Sutarčių ir sąskaitų duomenys skelbiami nuo 2020m. liepos mėnesio iki šių dienų. Duomenų teikėjas: Vilniaus miesto savivaldybės administracija. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Namespace:** `datasets/gov/vilniaus_m_sav/patalpos`[^manifest]
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/patalpos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/patalpos.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/patalpos` (`deployed`)[^manifest]
- **Provider:** `vilniaus_m_sav` — Vilniaus miesto savivaldybė *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `3` (3 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3859/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/patalpos`[^dcat]
- **Portal Title (`@lt`):** Vilniaus miesto savivaldybės nuomojamų patalpų sutarčių duomenys[^dcat]
- **Portal Title (`@en`):** Data on rental premises contracts of Vilnius City Municipality[^dcat]
- **Issued (`dct:issued`):** `2025-07-14`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2026-04-02` .. `2026-10-02`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Rinkinyje skelbiami Vilniaus miesto savivaldybės nuomojamų patalpų duomenys iš „Active Vilnius“ nuomos sistemos. Platformoje kaupiama informacija apie nuomojamus aktyvaus laisvalaikio objektus: sporto ir aktų sales, kabinetus, žaidimo ir sporto aikšteles ir kitus objektus. Šias laisvalaikio zonas nuomotis gali fiziniai bei juridiniai asmenys. Rinkinyje pateikiami duomenys apie nuomojamas patalpas, nuomotojus, esamus ir buvusius nuomininkus bei išrašytas sąskaitas faktūras už naudojimąsi paslaugomis. Nuomos įkainiai ir mokėtinos sumos už suteiktas paslaugas sąskaitose nėra skelbiami, tačiau viešinamas reitingas, kur mokėtinos sumos išrikiuojamos eilės tvarka nuo didžiausios iki mažiausios. Sutarčių ir sąskaitų duomenys skelbiami nuo 2020 m. liepos mėnesio. Duomenų teikėjas – Vilniaus miesto savivaldybės administracija. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

The package publishes the data of rented premises of Vilnius City Municipality from the “Active Vilnius” rental system. The platform collects information about rented active leisure facilities: sports and act halls, offices, playgrounds and sports grounds and other objects. These leisure areas may be leased by natural and legal persons. The package includes data on rented premises, tenants, current and former tenants and invoiced for the use of services. Rent rates and amounts payable for services rendered are not published in the accounts, but the ranking where the amounts payable are ranked in order from the highest to the lowest. Contract and account data have been published since July 2020. Data provider – Vilnius City Municipality Administration. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Patalpa](patalpos/Patalpa.md) | Vilniaus miesto savivaldybės nuomojamos patalpos | `4` | `patalpos_id` | — | `17` | — |
| [Sutartis](patalpos/Sutartis.md) | Vilniaus miesto savivaldybės patalpų nuomų sutartys | `4` | `sutarties_id` | — | `15` | — |
| [Saskaita](patalpos/Saskaita.md) | Vilniaus miesto savivaldybės sąskaitos patalpų nuomininkams už suteiktas paslaugas | `4` | `saskaitos_id` | — | `10` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/patalpos.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/patalpos.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vilniaus_m_sav/patalpos (https://data.gov.lt/datasets/3859/)
