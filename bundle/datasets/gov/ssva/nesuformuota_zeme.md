---
type: Dataset
title: "Nesuformuoti žemės plotai"
description: "Duomenis apie sklypais nesuformuotus žemės plotus bei su jais susijusius prašymus, pateiktus žemės informacinėje sistemoje."
resource: "https://get.data.gov.lt/datasets/gov/ssva/nesuformuota_zeme"
tags: [gov, ssva, deployed, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/nesuformuota_zeme.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/ssva/nesuformuota_zeme.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3879/"
    title: "data.gov.lt DCAT-AP — datasets/gov/ssva/nesuformuota_zeme"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Nesuformuoti žemės plotai

Duomenis apie sklypais nesuformuotus žemės plotus bei su jais susijusius prašymus, pateiktus žemės informacinėje sistemoje.[^manifest]

- **Namespace:** `datasets/gov/ssva/nesuformuota_zeme`[^manifest]
- **Manifest CSV:** [datasets/gov/ssva/nesuformuota_zeme.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/nesuformuota_zeme.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ssva/nesuformuota_zeme` (`deployed`)[^manifest]
- **Provider:** `ssva` — Statybos sektoriaus vystymo agentūra (SSVA) *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `2` (2 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/3879/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/ssva/nesuformuota_zeme`[^dcat]
- **Portal Title (`@lt`):** Nesuformuoti valstybinės žemės plotai ir prašymai dėl jų suformavimo[^dcat]
- **Portal Title (`@en`):** Unformed areas of state-owned land and applications for their formation[^dcat]
- **Issued (`dct:issued`):** `2025-08-12`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `DAILY` (`http://publications.europa.eu/resource/authority/frequency/DAILY`)[^dcat]
- **Distribution Date Span:** `2025-07-28` .. `2026-10-26`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Šis duomenų rinkinys apima informaciją apie valstybinės žemės plotus, kuriems dar nėra suformuotos teisinės ribos, taip pat apie gyventojų ir juridinių asmenų pateiktus prašymus, susijusius su šiais žemės plotais. Rinkinyje pateikiami tiek nesuformuotų plotų geografiniai ir administraciniai duomenys, tiek prašymų eiga ir būsena. Nesuformuotų žemės plotų lentelėje pateikiama informacija apie valstybės nuosavybėje esančius, bet dar Nekilnojamojo turto registre neregistruotus žemės plotus, kurių ribos nėra suformuotos. Kiekvienas įrašas turi unikalų identifikatorių, nurodoma jį administruojanti institucija (dažniausiai Nacionalinė žemės tarnyba arba savivaldybė), savivaldybės ir gyvenvietės kodai, buvimo vietos koordinatės (taškinė ir poligoninė geometrija), neapskaitytos žemės perimetras ir plotas. Geografinė informacija pateikiama keliais formatais: WKT (Well-Known Text) LKS94 koordinačių sistemoje, GeoJSON (tiek WGS84, tiek LKS94 sistemose), taip pat taškiniu formatu EPSG:3346. Svarbu pažymėti, kad duomenys apie nesuformuotus plotus yra kaupiami istoriškai. Jeigu plotas yra tik iš dalies suformuojamas arba keičiasi jo koordinatės, sukuriamas naujas įrašas su atnaujinta informacija, tačiau ankstesnis įrašas nėra ištrinamas. Tokiu būdu galima sekti žemės plotų formavimo eigą ir teritorijų pokyčius laikui bėgant. Antroji lentelė apima informaciją apie prašymus, susijusius su nesuformuotais žemės plotais. Kiekvienam prašymui suteikiamas unikalus identifikatorius, pateikiama sutarties informacija, susijęs nekilnojamojo turto registro objektas (jei yra), paslaugos tipas, nagrinėjimo etapas ir būsena, taip pat prašyme nurodytos teritorijos geografiniai duomenys. Prašymų duomenys apima įvairias žemės naudojimo ar disponavimo formas: žemės pardavimas, žemės perdavimas neatlygintinai naudotis (panaudai), žemės nuoma, žemės įsigijimas valstybės nuosavybėn, sutikimai statyti, servitutų nustatymas, kiti sutikimai, žvejybos teisės suteikimas ar perdavimas, žemės ploto perdavimas nuosavybėn neatlygintinai. Duomenyse kaupiama visa prašymų eiga ir istorija, įskaitant skirtingas būsenas: „draft“ (rengiamas), „submitted“ (pateiktas) ir „canceled“ (atšauktas). Tokia informacija leidžia stebėti prašymų judėjimą per skirtingus nagrinėjimo etapus, analizuoti procesų eigą ir identifikuoti teritorijas, kurios dažniausiai sulaukia prašymų. Duomenų rinkinys atnaujinamas kasdien. Visi duomenys pateikiami atsižvelgiant į teisės aktų keliamus duomenų atvėrimo reikalavimus. Duomenų teikėjas – Statybos sektoriaus vystymo agentūra. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

This dataset shall include information on areas of state-owned land for which legal boundaries have not yet been established, as well as requests submitted by residents and legal persons relating to these areas of land. The package provides both geographical and administrative data for unformed areas and the progress and status of applications. The table of land plots not formed shall contain information on land plots in the ownership of the State but not yet registered in the Real Property Register, the boundaries of which are not formed. Each entry shall have a unique identifier, indicate the authority administering it (usually the National Land Service or the municipality), municipal and settlement codes, location coordinates (point and polygonic geometry), perimeter and area of unaccounted land. Geographical information is provided in several formats: WKT (Well-Known Text) LKS94 coordinate system, GeoJSON (both WGS84 and LKS94 systems), as well as point format EPSG: 3346. It is important to note that data on unformed areas are compiled historically. If an area is only partially formed or its coordinates change, a new entry with updated information is created, but the previous entry is not deleted. In this way, the evolution of land formation and changes in areas over time can be tracked. The second table includes information on requests relating to unformed areas of land. Each request shall be given a unique identifier, contract information, related real estate registry object (if any), type of service, stage and status of examination, as well as geographical details of the area indicated in the application. Application data shall cover the various forms of land use or disposal: sale of land, transfer of land for gratuitous use (use), lease of land, acquisition of land into the ownership of the State, consent to construct, establishment of easements, other consent, granting or transfer of fishing right, transfer of land area into ownership free of charge. The data collects the full course and history of requests, including different states: “draft”, “submitted” (submitted), and “canceled” (canceled). This information allows the movement of applications to be monitored at different stages of the processing process, analysing the progress of the processes and identifying the areas most frequently receiving applications. The dataset is updated daily. All data shall be provided in accordance with the legal requirements for data opening. “Data provider” means the Agency for the Development of the Construction Sector. Contact the atverimas@stat.gov.lt for technical questions or possible errors.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [NesuformuotasPlotas](nesuformuota_zeme/NesuformuotasPlotas.md) | Nesuformuoti žemės plotai | `4` | `vda_prime_key` | — | `13` | Duomenų rinkinys apima informaciją apie valstybės valdomus, bet dar nesuformuotus žemės plotus. |
| [Prasymas](nesuformuota_zeme/Prasymas.md) | Nekilnojamojo turto (nesuformuotų plotų) prašymų duomenys | `4` | `vda_prime_key` | — | `13` | Duomenų rinkinys apima informaciją apie fizinių ar juridinių asmenų prašymus, susijusius su nesuformuotais žemės plotais. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/ssva/nesuformuota_zeme.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ssva/nesuformuota_zeme.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/ssva/nesuformuota_zeme (https://data.gov.lt/datasets/3879/)
