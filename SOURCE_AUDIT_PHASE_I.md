# UDCT v7.14 — Integrated Source Audit, Phase I
Date: 2026-11-10
Status: retrospective source audit, NOT preregistration and NOT confirmatory execution.

## Scope and source evidence
Eight source archives were statically inspected (including the three original source bundles, the recent 46-item follow-up collection, and the pre-existing reproducibility and protocol bundles). All nested ZIPs were CRC-tested. A member-by-member SHA-256 inventory and machine-readable comparison findings accompany this report. No new gravity simulation, full step-by-step numerical rerun, or independent mathematical validation was performed.

## Findings
- The two original Steps 01–25 and Steps 26–50 archives are byte-for-byte identical to their embedded `original_archives/Steps_01_25.zip` and `original_archives/Steps_26_50.zip` counterparts in `UDCT_v7.14_Reproducibility_Download.zip`.
- The static archive scan found no corrupt nested ZIPs.
- Identical file content occurs under more than one member path; deduplicate for analysis but retain originals unchanged for provenance.
- The first 25-step archive contains early loose scripts as well as explicitly numbered packages; its entire contents should not be represented as a complete, uniquely timestamped Step 01–25 chronology.

## Scientific interpretation to preserve
1. The isolated spherical simple-QUMOND Plummer construction with tracer rho_p=[1+(r/a)^p]^(-5/p) has a *leading central asymptotic coefficient cancellation* at p=1.5, under the documented model assumptions. The next-order terms matter at equality.
2. The archived Osipkov–Merritt local tangency near r_a/a=0.466466787396 is a model- and finite-energy-window-specific exploratory numerical candidate, not a universal critical radius, global positivity theorem, or an observational discovery.
3. The 3D Hessian diagnostics, spherical Jeans moments, OM phase-space distribution function, and dynamical stability are separate tests. A Hessian calculation does not itself implement GQUMOND's higher-derivative action.
4. Hydrus I-informed modeling is not a direct likelihood fit to individual stellar line-of-sight velocities; the latter requires a separate preregistered observational protocol.
5. Numerical agreement between alternative quadratures with a shared gravitational/inversion kernel is not independent physical confirmation. Differences between quadrature resolutions do not constitute certified error bounds.

## Publication/protocol risks
- Do not label previously scanned p, anisotropy, or energy coordinates as new prospective predictions.
- Freeze potential conventions and boundary terms; the logarithmic isolated-MOND outer potential and the central singular inversion endpoint require explicit treatment.
- A finite energy grid cannot prove global DF positivity.
- Avoid the word parameter-free for a fixed-input mass/scale/acceleration exercise unless a separate precise operational definition is supplied.
- The exact future hold-out domain, independent implementation, numerical error certification method and objective decision rules have not yet been agreed or locked.
- Source manuscript has potentially duplicated/renumbered Future Directions and Conclusions sections in its 15-page composite; check layout and citations before a new public release. Do not silently rewrite published exploratory text.

## Decision
**Phase I archival provenance: PASS. Scientific/confirmatory readiness: CONDITIONAL / NOT YET LOCKED.**
The next deliverable should be a distinct prospective protocol, timestamped before new confirmatory calculations. Reuse of old data must be explicitly labeled exploratory.
