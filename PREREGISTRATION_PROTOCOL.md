# UDCT v7.14 — Prospective Numerical Phase-Space Consistency Preregistration

**Author:** Won Shik Paik, Independent Researcher  
**Document date:** 10 November 2026
**Zenodo reserved DOI:** 10.5281/zenodo.24095267 (not activated before publication)
**GitHub:** https://github.com/wspaik5/UDCT_v7.14_Preregistration  
**Status:** FINAL UPLOAD CANDIDATE (DOI RESERVED; NOT PUBLISHED) — NOT YET PUBLISHED OR REGISTERED; NO CONFIRMATORY RUNS EXECUTED UNDER THIS PROTOCOL.  
**Study type:** Prospective, finite-grid, model-conditional numerical protocol; no observational inference.

## Abstract
Archived UDCT v7.14 Steps 01–50 and subsequent exploratory audits reported two separate features of a specified isolated spherical simple-QUMOND/Plummer model: (a) cancellation of a leading central asymptotic coefficient at tracer exponent p=1.5; and (b) a finite-energy local Osipkov–Merritt (OM) distribution-function tangency candidate near r_a/a=0.466466787396. Neither is a new prospective discovery. This document specifies a prospective 20-point numerical DF-sign audit, three-valued decision rules, source provenance, and error-control gates. Crucially, the proposed coordinates have not been independently checked against every archived exploratory run for prior exposure. They are a prespecified future grid, **not a verified held-out sample**. No global DF-positivity theorem, novel gravity law, full GQUMOND solution, or direct Hydrus I stellar-likelihood result is claimed.

## 1. Retrospective scientific basis
The original v7.14 Step 01–50 archives include Hydrus I-motivated sensitivity experiments, three-dimensional Hessian diagnostics, Jeans second-moment calculations, and later isolated spherical OM inversion. The later branch uses a different mathematical question than the early 3D Hessian tests. Six exploratory audits and subsequent high-precision quadrature comparisons investigate the finite-window tangency. The existing results are retrospective; no reuse of them as prospective confirmatory evidence is permitted. The Phase I integrated audit checks source identity and file integrity but is not an independent physics replication.

## 2. Fixed physical model and conventions
The gravitating mass is spherical Plummer, with g_N(r)=G M r/(r^2+a^2)^(3/2). In the isolated spherical simple-QUMOND construction, g(r)=g_N(r)/2+sqrt(g_N(r)^2/4+a_0*g_N(r)). Tracer rho_p(r)=rho_0*[1+(r/a)^p]^(-5/p), rho_0=1. OM augmented density rho_Q(r)=[1+(r/r_a)^2]*rho_p(r), beta(r)=r^2/(r^2+r_a^2). Reference constants: G=4.30091e-3 pc (km/s)^2/Msun, M=32730 Msun, a=53.3 pc, a_0=1.2e-10 m/s^2. These are model inputs, not observationally fitted parameter-free predictions. Use Phi(r)-Phi(0) as the outward-increasing potential difference; do not substitute an infinity-zero potential in isolated MOND, where the outer potential grows logarithmically. The dimensionless energy label x=r/a means the spherical turning-point label used by archived inversions, not an observed stellar radius.

## 3. Pre-specified grid and its limitation
The **20 prospective evaluation points** are the Cartesian product p in {1.487, 1.513}, r_a/a in {0.44, 0.48}, and energy label x in {0.30,0.40,0.50,0.60,0.70}. Exact enumeration is in PRESPECIFIED_GRID.csv. This grid is **not claimed to be untouched by prior exploration**: historical exposure is not fully audited. It is deliberately separated from the previously reported p=1.5 tangency and serves a prospective reproducibility/stress-test objective rather than a statistically independent discovery claim. No grid points may be changed after publication without a labeled amendment.

## 4. Analysis and numerical verification plan
Two mathematically equivalent OM inversion formulations should be evaluated, one using the second potential derivative of augmented density with analytic central-endpoint subtraction, and another independently implemented by integration by parts using first derivatives and explicit boundary terms. Both must use the exact same physical model and energy convention. Since these representations share the same underlying inversion kernel, their agreement is a numerical cross-check, not independent physics validation. An implementation using separately written code and independently checked signs/units is required before any certified sign assertion. Preserve the exact Python environment, code hashes, commands, raw integration outputs and diagnostic logs.

Numerical error accounting must cover inner potential quadrature, outer OM quadrature, outer-tail truncation, central endpoint treatment, differentiation/interpolation and floating-point rounding. Prior 55-digit arithmetic and 40/80/160-by-64/128/256 quadrature scans are **exploratory diagnostics, not certified enclosures**. A validated numerical enclosure must be supplied before labeling a sign certified. If that cannot be established, classify the result as inconclusive. This preregistration does not assert that a validated numerical enclosure implementation already exists.

## 5. Controls and locked decisions
Control C1: compare the Newtonian Plummer isotropic Jeans radial second moment at r=a against the analytic reference G*M/(6*sqrt(2)*a), with relative discrepancy <= 1e-4. This checks units and integration plumbing, not OM inversion correctness. Control C2: for each evaluation coordinate, compare the two OM inversion representations; their numerical discrepancy must be <= 1e-6 times max(1,abs(f_A),abs(f_B)) in archived normalization. C2 is an operational screening tolerance, **not** a certified error bound. Control C3: verify that the augmented-density expression reduces to the isotropic tracer as r_a tends to infinity at fixed r. Report all failures. The main sign decision requires controls C1–C3 and justified bounds:

* **Certified negative at a sampled point:** validated upper bound U<0 and controls pass.
* **Certified nonnegative at all sampled points:** validated lower bound L>=0 for each of 20 points and controls pass. This does not imply continuum or global positivity.
* **Inconclusive:** interval overlaps zero, validated bounds unavailable, controls fail, or implementations disagree. Uncertified negative point estimates cannot be called a certified failure.

The primary report must enumerate all 20 points, including inconclusive and failed controls. There is no requirement to force a positive or negative conclusion. Any unplanned scan is exploratory and reported separately.

## 6. Sequence and publication lock
1. Publish this protocol, PROTOCOL.json, grid CSV, provenance manifest and the source-code status before new protocol-driven tests.
2. Verify the independent inversion derivation and complete a documented numerical error-enclosure implementation; amendments are allowed only if timestamped and identified, never silently retrofitted.
3. Run controls and the 20-point grid; archive every result, error interval and execution log.
4. Release a distinct **Post-registration** result package, including failures and deviations.

**Publication caveat:** Because the independent implementation and rigorous enclosure are not yet delivered, the present package preregisters the decision logic and grid but is not an executable certified-sign test. If published as is, describe it as a *prospective protocol with implementation gates*, not as a fully locked validated numerical analysis pipeline.

## 7. Scientific scope and exclusions
The central p=1.5 coefficient cancellation is a local asymptotic observation and does not establish the finite-energy OM tangency; the latter is a local numerical feature, not a universal critical anisotropy radius. Negative DF excludes only a specified model/tracer/anisotropy ansatz under the stated assumptions, not MOND or QUMOND generally. Hessian eigenvalues, Jeans second moments, DF positivity and dynamical stability are different tests. No 3D external-field solution, full GQUMOND higher-derivative action, or novel modified-gravity law is tested here.

Hydrus I informed aspects of the broader program but the current tests do not fit the complete individual-star line-of-sight velocity data. Such a fit would require a separate preregistration covering membership, selection, foregrounds, binaries, uncertainties and likelihood comparisons.

## 8. References
1. Bekenstein, J. & Milgrom, M. (1984), Astrophysical Journal 286, 7–14, doi:10.1086/162570.
2. Milgrom, M. (2010), MNRAS 403, 886–895, doi:10.1111/j.1365-2966.2009.16184.x.
3. Milgrom, M. (2023), Physical Review D 108, 084005, doi:10.1103/PhysRevD.108.084005.
4. Merritt, D. (1985), MNRAS 214, 25P–28P.
5. Binney, J. & Tremaine, S. (2008), Galactic Dynamics, 2nd ed.
6. Koposov, S. E. et al. (2018), MNRAS 479, 5343–5361, doi:10.1093/mnras/sty1772.
7. Paik, W. S. (2026), UDCT v7.14 Exploratory QUMOND Hessian and Phase-Space Consistency Tests (Steps 01–50), archived original materials.
8. Paik, W. S. (2026), UDCT v7.14 Exploratory Findings: The p=1.5 Boundary in QUMOND, archived audits 01–06.
