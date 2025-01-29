**This code is solemly developed using personal colab resources **


## Features Custom PII detector using Presidio 

* Considers a config-driven approach for the dynamic selection of key parameters
* Generic list for Exclusion of entities while detecting PII 
* Supports exclusion of a list of financial entities while detecting the PII information
* Supports selection and non-selection of anonymization while formulating the results

```
Config structure
"targetlist" : ["314b", "AML", "SAR", "FIU", "SSN", "KYC", "EFE", "call out", "Fedline", "FINRA", "finra", "31", "BSA", "CTR", "SAR", "FinCEN"],
"score_threshold": 0.2, 
"language":"en",
"doanonymize": false
```

References:

1) Caroline Valetkevitch, Reuters, Nasdaq leads Wall St higher; tech shares recover from Monday's sell-off https://finance.yahoo.com/news/p-nasdaq-futures-regain-ground-103024570.html

2) Laura Bratton, Yahoo Finance, Nvidia stock begins recovery after DeepSeek AI frenzy prompted near $600 billion loss, https://finance.yahoo.com/news/asia-shares-mixed-us-tech-035042922.html

3) Kenneth Niemeyer,Yahoo Finance, Coinbase CEO Brian Armstrong says there are 1 million new cryptocurrencies created every week, https://finance.yahoo.com/news/coinbase-ceo-brian-armstrong-says-214529402.html

4) Ines Ferré , Yahoo Finance, AI-exposed power stocks rebound after DeepSeek release casts 'uncertainty' over industry, https://finance.yahoo.com/news/ai-exposed-power-stocks-rebound-after-deepseek-release-casts-uncertainty-over-industry-194013211.html

5) finra.org,Continuing Risk: ACH Fraud ,2025 FINRA Annual Regulatory Oversight Report, https://www.finra.org/rules-guidance/guidance/reports/2025-finra-annual-regulatory-oversight-report/aml

6) finra.org,Finra AML guidance, https://www.finra.org/rules-guidance/key-topics/aml#guidance
