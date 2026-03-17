---
layout: minimal
title: Stata
hero_title: Stata
hero_subtitle: Practical workflows
hero_desc: Notes, templates, and reproducible Stata workflows for empirical research.
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
  <div class="callout-title">Series focus: ASIF / China Industrial Enterprise Database</div>

  <p>
    This series uses the <strong>China Industrial Enterprise Database</strong> (中国工业企业数据库, often called <strong>ASIF</strong>) as a practice dataset.
    To respect licensing restrictions, I work with a <strong>modified version</strong> of the data and, when useful, <strong>Stata’s built-in sample datasets</strong> so examples remain self-contained and easy to follow.
  </p>

  <p>
    The aim is to show practical <strong>Stata workflows</strong>—from cleaning and variable construction to estimation, inference, and replication—while also giving a clear sense of how this database is commonly used in applied research.
  </p>

  <p class="note">
    I am still learning, so I would be very grateful for any corrections or suggestions.
  </p>
</div>

## What this section covers
- **Data workflow:** import/export, reshape, merge, append, panel setup, missing values, winsorization
- **Estimation:** OLS, FE/RE, DiD/event study, IV/2SLS, GMM (when needed)
- **Inference:** clustered SEs, wild bootstrap, robustness checks, reporting
- **Productivity / IO tools:** `prodest`, `reghdfe`, `ivreg2`, `esttab`, `coefplot`
- **Reproducibility:** folder structure, globals, logs, do-files, versioning

## Files
<!-- AUTO-LIST-START -->
- **[Session2__A_Test_of_a_Nonlinear_Combination_of_Coefficients.pdf](Session2__A_Test_of_a_Nonlinear_Combination_of_Coefficients.pdf)**
- **[Session_1__Univariate_and_Joint_Tests_Using_lincom_and_testparm.pdf](Session_1__Univariate_and_Joint_Tests_Using_lincom_and_testparm.pdf)**
<!-- AUTO-LIST-END -->
