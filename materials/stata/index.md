---
layout: minimal
title: Stata
hero_title: Stata
hero_subtitle: Practical workflows
hero_desc: Notes, templates, and reproducible workflows for using Stata in empirical research.
hide_name: true

---

<style>
.callout{
  margin: 16px 0 22px 0;
  padding: 14px 16px;
  border: 1px solid rgba(0,0,0,.12);
  border-left: 4px solid #b08a2e;
  border-radius: 10px;
  background: #fff;
}
.callout-title{
  font-weight: 800;
  margin-bottom: 6px;
}
.callout p{ margin: 8px 0; }
.callout .note{ opacity: .88; }
</style>

<div class="callout">
  <div class="callout-title">Series focus: ASIF / China Industrial Enterprise Database (practice dataset)</div>

  <p>
    In this series, I use the <strong>China Industrial Enterprise Database</strong> (中国工业企业数据库; often abbreviated as
    <strong>ASIF/China Industrial Enterprise Database</strong>) as a practice dataset. To respect data licensing and copyright restrictions,
    I work with a <strong>modified and adapted version</strong> of the data, and—when helpful—use <strong>Stata’s built-in sample datasets</strong>
    to keep demonstrations self-contained and easy to follow.
  </p>

  <p>
    The goal is twofold: (i) to illustrate end-to-end <strong>Stata econometric workflows</strong> (cleaning, construction, estimation, inference,
    and replication hygiene), and (ii) to provide a clear, practical sense of how the China Industrial Enterprise Database is typically used in applied research.
  </p>

  <p class="note">
    My current knowledge is still limited, so if you notice any mistakes or unclear parts, please let me know—I would be grateful for your feedback and will revise accordingly.
  </p>
</div>

## What this section covers
- **Data workflow:** import/export, reshape, merge, append, panel setup, missing values, winsorization
- **Estimation:** OLS/FE/RE, DiD/event study, IV/2SLS, GMM (as needed)
- **Inference:** clustered SEs, wild bootstrap, robustness checks, reporting
- **Productivity / IO tools (as needed):** `prodest`, `reghdfe`, `ivreg2`, `esttab`, `coefplot`
- **Reproducibility:** folder structure, globals, logs, do-files, versioning

## Files
<!-- AUTO-LIST-START -->
- **[Session2__A_Test_of_a_Nonlinear_Combination_of_Coefficients.pdf](Session2__A_Test_of_a_Nonlinear_Combination_of_Coefficients.pdf)**
- **[Session_1__Univariate_and_Joint_Tests_Using_lincom_and_testparm.pdf](Session_1__Univariate_and_Joint_Tests_Using_lincom_and_testparm.pdf)**
<!-- AUTO-LIST-END -->
