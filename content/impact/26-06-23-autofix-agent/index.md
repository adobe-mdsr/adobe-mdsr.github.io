---
title: "Accelerating Web Experience Optimization with AI Agents"
date: 2026-06-23
image:
  placement: 3
  focal_point: "Center"
  preview_only: false

authors:
- Somesh Singh
- Yaman Kumar Singla

youtube_id: "rVV-5D55K_o"

publishDate: "2026-06-23T00:00:00Z"
---
[Core Web Vitals](https://business.adobe.com/uk/blog/basics/web-vitals-explained) -- loading speed, visual stability, and responsiveness -- shape how people experience a website: whether they stay or bounce, and how prominently pages surface in search. A Deloitte study found that a 100ms improvement in load speed lifts conversion rates by 8-10%, yet only about half of mobile sites pass all three thresholds. That gap leaves real revenue and engagement on the table.

Closing it has always been developer work: audit the page, trace the bottleneck through the code, ship a careful fix. The work is slow, expensive, and hard to prioritize against the feature backlog. AI coding agents looked like an obvious shortcut, but web performance turns out to be an unusually hard target -- improving one metric often quietly breaks another. To find out how far today's agents actually get, we built a benchmark and tested them on thousands of real websites. Without structured supervision, they fall short: the weakest setups made performance worse on up to 90% of the sites they touched.

## Adobe Experience Manager Sites Optimizer

[Adobe Experience Manager Sites Optimizer](https://business.adobe.com/blog/introducing-adobe-eerience-manager-sites-optimizer) closes the gap with purpose-built AI agents that continuously scan live pages and source code to find Core Web Vitals bottlenecks. A dedicated analysis stage cross-references real-user monitoring data, lab audits, network waterfalls, and static code review to trace each symptom back to its root cause. The [Auto Optimization](https://experienceleague.adobe.com/en/docs/events/adobe-developers-live-recordings/2025/code-optimization) capability then writes fixes that are ready to ship, delivered straight into your workflow through GitHub and Jira.

The safeguard is validation. Sites Optimizer checks every fix against all three Core Web Vitals before it goes out -- if a change helps LCP but regresses CLS or INP, it doesn't ship. In our benchmark, Sites Optimizer improved web experiences on up to 71% of websites with zero regressions. Brands including The Hershey Company, BambooHR, PGA TOUR, and Wilson are already seeing measurable gains.

{{< youtube rVV-5D55K_o >}}
*Inside the Engine: Code Optimization with Adobe Experience Manager Sites Optimizer -- the end-to-end Auto Optimization workflow, from detection to deployment, at Adobe Developers Live 2025.*

## Measuring what agents can really do: the SWE-WEB benchmark

We introduce *SWE-WEB*, the first benchmark that measures how well can LLMs & coding agents improve the websites 5.5B people use every day. SWE-WEB spans 10,689 deployable website repositories, 73,000 webpages, and 15 programming languages, capturing 1,992 websites also being captured in Google CrUX field data. SWE-WEB spans blogs, business and marketing sites, media and creative galleries, e-commerce, documentation across static HTML, Hugo, Jekyll, React, Vue, Next.js, Angular, and WordPress, with a median of 121K lines of code per repository. Its Core Web Vitals distribution tracks the top 10 million sites in CrUX.

We evaluated 19 agent-model configurations -- four coding agents paired with leading closed and open-source LLMs, including a Qwen3.5 scaling sweep from 9B to 397B -- across 200 stratified sites. The best configuration improved at least one Core Web Vital with no regressions on only **40.4% of sites**, while weak setups degraded as many as 90%. Adobe Sites Optimizer Autofix improves over 60% of the sites with fewer than 10% regressions, beating state-of-the-art agents by a wide margin.

Learn more about Sites Optimizer and the benchmark:
- [Adobe Experience Manager Sites Optimizer](https://business.adobe.com/products/experience-manager/sites/optimizer.html)
- [Auto Optimization at Adobe Developers Live 2025](https://experienceleague.adobe.com/en/docs/events/adobe-developers-live-recordings/2025/code-optimization)
- [SWE-WEB benchmark and harness](https://github.com/behavior-in-the-wild/web-experience-benchmark)
