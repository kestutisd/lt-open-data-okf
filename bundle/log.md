# Directory Update Log

## 2026-11-19
* **Update**: Migrated the bundle to OKF v0.3 (`okf_version: "0.3"`), rendering `1104` pure Spinta DSA + DCAT-AP `Dataset` concepts and `2307` `Table` concepts with the 8-column `# Schema` layout and `team:vssa` / `team:vda` source credibility signals.
* **Creation**: Added [Statutory LTL to EUR Currency Conversion](computations/ltl-to-eur-conversion.md) (`type: Attested Computation`) with deterministic Python executor (`/references/executors/ltl_to_eur.py`) and receipt attester (`/references/attesters/ltl_to_eur_attester.py`), alongside Spinta DSA architecture and cross-register join references under [references/](references/index.md).

## 2026-11-17
* **Update**: Integrated deterministic `data.gov.lt` DCAT-AP portal catalog metadata (`dct:issued`, `dct:modified`, `dct:accrualPeriodicity`, `dct:license`, `dct:publisher`), Saugykla `get_data_gov_lt.in` deployment verification, and EU/ISO statutory classifications (`ISO 639`, `CPV/BVPŽ`, `EVRK 2 / EVRK 2.1`, `ISO 4217`).

## 2026-11-11
* **Initialization**: Bootstrapped deterministic schema ingestion from `atviriduomenys/manifest` commit `ec54998dcea52a0d26dc1c172eacec438d47e727` (`2026-11-11T14:39:20Z`) with PII/comment scrubbing and `0` `human:` verifications (`trust_tier = "unverified"`).
