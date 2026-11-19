---
type: Dataset
title: "Keleivių srautas Marijampolės viešajame transporte"
description: "Marijampolės viešojo transporto elektroninio bilieto sistemos (TIKIS) bilietų pirkimo ir žymėjimo duomenys nuo 2023 m. liepos mėn."
resource: "https://get.data.gov.lt/datasets/gov/map/keleiviu_srautas"
tags: [gov, map, deployed, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/map/keleiviu_srautas.csv#L3"
    title: "atviriduomenys/manifest — datasets/gov/map/keleiviu_srautas.csv#L3"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/4137/"
    title: "data.gov.lt DCAT-AP — datasets/gov/map/keleiviu_srautas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Keleivių srautas Marijampolės viešajame transporte

- **Namespace:** `datasets/gov/map/keleiviu_srautas`[^manifest]
- **Manifest CSV:** [datasets/gov/map/keleiviu_srautas.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/map/keleiviu_srautas.csv#L3)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/map/keleiviu_srautas` (`deployed`)[^manifest]
- **Provider:** `map` — Marijampolės autobusų parkas *(declared `ns`)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `1` (1 lentelė)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/4137/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/map/keleiviu_srautas`[^dcat]
- **Portal Title (`@lt`):** Marijampolės viešojo transporto elektroniniai bilietai[^dcat]
- **Portal Title (`@en`):** Marijampolė Public Transport Electronic Tickets[^dcat]
- **Issued (`dct:issued`):** `2026-03-09`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `MONTHLY` (`http://publications.europa.eu/resource/authority/frequency/MONTHLY`)[^dcat]
- **Distribution Date Span:** `2026-02-19` .. `2026-10-23`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Marijampolės viešojo transporto elektroninio bilieto sistemos (TIKIS) bilietų pirkimo ir žymėjimo duomenys nuo 2023 m. liepos mėn. 23 d. Stulpelyje „bilieto_tipas“ vartojamos reikšmės: „USE_CARD_SERVICE“ – el. kortelės naudojimas miesto viešajame transporte; „USE_CARD_SERVICE_TRIANGLE“ – el. kortelės naudojimas priemiesčio viešajame transporte; „SELL_TICKET“ – bilieto pirkimas miesto viešajame transporte; „SELL_TICKET_TRIANGLE“ – bilieto pirkimas priemiesčio viešajame transporte. Marijampolės mieste bilieto kaina yra fiksuota viso maršruto metu, o priemiestyje kaina priklauso nuo važiuotų stotelių skaičiaus. Priemiestyje (miesto stotelėse) leidžiama naudoti ir miesto terminuotus bilietus. Stulpelyje „keliones_id“ nurodomas maršruto tvarkaraščio kelionės identifikatorius (atnaujinant tvarkaraščius kuriamas naujas identifikatorius). Bilieto pavadinimai „Vienkartinis bilietas 50% nuol.“ ir „Vienkartinis bilietas“ nuo 2023 m. rugsėjo turi naujus identifikatorius, todėl šiuo pavadinimu bilietai turi po du identifikatorius. Stulpeliuose „pr_stotele“ ir „pab_stotele“ nurodoma keleivio su kintamos kainos bilietu kelionės priemiestiniu viešuoju transportu pradžia ir pabaiga. Stulpelyje „stotele“ nurodyta bilieto pirkimo arba žymėjimo vieta miesto ir priemiesčio viešajame transporte. Stulpelyje „mokejimo_budas“ reikšmė „CARD“ nurodo, kad buvo atsiskaityta el. bilieto kortele, o „EMV“ – bankine kortele. Duomenys atnaujinami kas mėnesį. Duomenų teikėjas – Uždaroji akcinė bendrovė „Marijampolės autobusų parkas“. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [KeleiviuSrautas](keleiviu_srautas/KeleiviuSrautas.md) | Keleivių srautas | `4` | — | — | `17` | Marijampolės miesto viešojo transporto pirkti ir žymėti bilietai transporto priemonėje |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/map/keleiviu_srautas.csv#L3 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/map/keleiviu_srautas.csv#L3)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/map/keleiviu_srautas (https://data.gov.lt/datasets/4137/)
