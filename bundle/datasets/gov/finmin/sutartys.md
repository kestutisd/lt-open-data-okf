---
type: Dataset
title: "2014-2020 m. ES fondų projektų įgyvendinimo duomenys"
description: "Skelbiama detali informacija apie 2014-2020 metų Europos Sąjungos fondų investicinių projektų įgyvendinimą (projektų sutartys, stebėsenos rodikliai, sutarčių projektų biudžetas, sutarčių priemonės, finansavimo formos, uždaviniai, veiklos, projekto mokėjimo prašymai, projekto..."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys"
tags: [gov, finmin, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L2"
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L2"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2161/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# 2014-2020 m. ES fondų projektų įgyvendinimo duomenys

- **Namespace:** `datasets/gov/finmin/sutartys`[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L2)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Access:** `—` *(determined by table/property access levels)*[^manifest]
- **Tables:** `33` (33 lentelės)[^manifest]

# Portal Metadata (DCAT-AP)

- **DCAT Dataset URI:** `https://data.gov.lt/datasets/2161/`[^dcat]
- **Publisher (`dct:publisher`):** Valstybės duomenų agentūra[^dcat]
- **Matched Spinta Endpoint:** `https://get.data.gov.lt/datasets/gov/finmin/sutartys`[^dcat]
- **Portal Title (`@lt`):** 2014-2020 m. Europos Sąjungos fondų projektų įgyvendinimo duomenys[^dcat]
- **Portal Title (`@en`):** Data on implementation of EU funds projects for period 2014-2020[^dcat]
- **Issued (`dct:issued`):** `2023-06-27`[^dcat]
- **Last Modified (`dct:modified`):** `2026-04-07`[^dcat]
- **Update Cadence (`dct:accrualPeriodicity`):** `NEVER` (`http://publications.europa.eu/resource/authority/frequency/NEVER`)[^dcat]
- **Distribution Date Span:** `2023-06-26` .. `2026-10-01`[^dcat]
- **License (`dct:license`):** `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

### Portal Description (`@lt`)

Skelbiama detali informacija apie 2014-2020 metų Europos Sąjungos fondų investicinių projektų įgyvendinimą (projektų sutartys, stebėsenos rodikliai, sutarčių projektų biudžetas, sutarčių priemonės, finansavimo formos, uždaviniai, veiklos, projekto mokėjimo prašymai, projekto pirkimo planai, ataskaitos po finansavimo pabaigos ir kt.). Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^dcat]

### Portal Description (`@en`)

Detailed information on the implementation of investment projects of European Union funds for 2014-2020 is published (contracts of the projects, monitoring indicators, budget of the contract projects, contract measures, financing forms, objectives, activities, project payment requests, refunds, project procurement plans, reports after the end of funding, etc.).[^dcat]

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Contract](sutartys/Contract.md) | Projekto sutartis | `4` | `project` | — | `47` | — |
| [ConPartner](sutartys/ConPartner.md) | Sutarties partneriai | `4` | `con_partner_id` | — | `6` | — |
| [ConIndicator](sutartys/ConIndicator.md) | Sutarties produkto ir rezultato stebėsenos rodikliai | `4` | `con_indicator_id` | — | `4` | — |
| [ConFinSource](sutartys/ConFinSource.md) | Sutarties projekto tinkamų finansuoti išlaidų finansavimo šaltiniai | `4` | `con_fin_source_id` | — | `6` | — |
| [ConBudget](sutartys/ConBudget.md) | Sutarties projekto biudžetas | `4` | `con_budget_id` | — | `11` | — |
| [ConBudgetParent](sutartys/ConBudgetParent.md) | Sutarties projekto biudžetas ("tėviniai" objektai) | `4` | `con_budget_id` | — | `8` | — |
| [ConMeasure](sutartys/ConMeasure.md) | Sutarties priemonės | `4` | `con_measure_id` | — | `16` | — |
| [ConTask](sutartys/ConTask.md) | Sutarties uždaviniai | `4` | `con_task_id` | — | `4` | — |
| [ConPhIndicator](sutartys/ConPhIndicator.md) | Sutarties uždavinio veiklos fiziniai rodikliai | `4` | `con_ph_indicator_id` | — | `5` | — |
| [Payment](sutartys/Payment.md) | Projekto mokėjimo prašymas | `4` | `payment_id` | — | `26` | — |
| [PayPart23](sutartys/PayPart23.md) | Projekto mokėjimo prašymo dalis Nr. 2 arba Nr. 3 | `4` | `pay_part23_id` | — | `16` | — |
| [PayAppAm](sutartys/PayAppAm.md) | Projekto mokėjimo prašymo dalies Nr. 2 / Nr. 3 paraiškos asignavimo valdytojui informacija | `4` | `pay_app_am_id` | — | `8` | — |
| [PayInformMeasure](sutartys/PayInformMeasure.md) | Projekto mokėjimo prašymo dalies Nr. 4. informavimo priemonės | `4` | `pay_inform_measure_id` | — | `4` | — |
| [PayOtherInfo](sutartys/PayOtherInfo.md) | Projekto mokėjimo prašymo dalies Nr. 4. kita informacija | `4` | `pay_other_info_id` | — | `4` | — |
| [PayIndicator](sutartys/PayIndicator.md) | Projekto mokėjimo prašymo dalies Nr. 1 produkto ir rezultato stebėsenos rodikliai | `4` | `pay_indicator_id` | — | `9` | — |
| [PayActivity](sutartys/PayActivity.md) | Projekto mokėjimo prašymo dalies Nr. 1 veiklos | `4` | `pay_activity_id` | — | `5` | — |
| [PayFinalBeneficiary](sutartys/PayFinalBeneficiary.md) | Projekto mokėjimo prašymo dalies Nr. 1 galutinių naudos gavėjų sąrašas | `4` | `pay_final_beneficiary_id` | — | `9` | — |
| [PayDataCorrection](sutartys/PayDataCorrection.md) | Projekto mokėjimo prašymo dalies Nr. 1 duomenų koregavimų sąrašas | `4` | `pay_data_correction_id` | — | `9` | — |
| [Repayment](sutartys/Repayment.md) | Projekto grąžintinos lėšos | `4` | `repayment_id` | — | `23` | — |
| [RepaymentExpend](sutartys/RepaymentExpend.md) | Projekto grąžintinų lėšų netinkamos išlaidos | `4` | `repayment_expend_id` | — | `10` | — |
| [RepaymentPart](sutartys/RepaymentPart.md) | Projekto grąžintinų lėšų dalys | `4` | `repayment_part_id` | — | `7` | — |
| [PaySchedule](sutartys/PaySchedule.md) | Projekto mokėjimo prašymo teikimo grafikas | `4` | `pay_schedule_id` | — | `14` | — |
| [PlanPayment](sutartys/PlanPayment.md) | Projekto mokėjimo prašymo teikimo grafiko planuojamas mokėjimo prašymas | `4` | `plan_payment_id` | — | `6` | — |
| [PlanIndicator](sutartys/PlanIndicator.md) | Projekto mokėjimo prašymo teikimo grafiko planuojamo mokėjimo prašymo stebėsenos rodikliai, įtraukti į veiklos peržiūros planą | `4` | `plan_indicator_id` | — | `8` | — |
| [PurchasePlan](sutartys/PurchasePlan.md) | Projekto pirkimo planas | `4` | `purchase_plan_id` | — | `8` | — |
| [Purchase](sutartys/Purchase.md) | Projekto pirkimo plano pirkimas | `4` | `purchase_id` | — | `21` | — |
| [PurchaseContract](sutartys/PurchaseContract.md) | Projekto pirkimo plano pirkimo sutartis | `4` | `purchase_contract_id` | — | `15` | — |
| [PurchaseRevise](sutartys/PurchaseRevise.md) | Projekto pirkimo plano pirkimo patikra | `4` | `purchase_revise_id` | — | `12` | — |
| [PurchaseReviseContract](sutartys/PurchaseReviseContract.md) | Projekto pirkimo plano pirkimo patikros sutartis | `4` | `purchase_revise_contract_id` | — | `4` | — |
| [PurchasePlanCorrection](sutartys/PurchasePlanCorrection.md) | Projekto pirkimų plano keitimai | `4` | `purchase_plan_corr_id` | — | `13` | — |
| [PurchasePlanCorrectionPurchase](sutartys/PurchasePlanCorrectionPurchase.md) | Pataisytas projekto pirkimo plano pirkimas | `4` | `purchase_corr_id` | — | `20` | — |
| [AdjustmentAction](sutartys/AdjustmentAction.md) | Projekto institucijos koregavimo veiksmų dalys | — | `action_id` | — | `13` | — |
| [FinishReport](sutartys/FinishReport.md) | Ataskaitos po finansavimo pabaigos | — | `report_id` | — | `9` | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `manifest` | `https://atviriduomenys.readthedocs.io/` |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L2 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L2)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys (https://data.gov.lt/datasets/2161/)
