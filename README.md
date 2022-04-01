# CeneoScraper

## Struktura opinii w serwisie [Ceneo.pl](https://www.ceneo.pl/)

|Składowa|Selektor|Nazwa zmiennej|Typ zmiennej|
|--------|--------|--------------|------------|
|opinia|div.js_product-review|||
|identyfikator opinii|div.js_product-review\["data-entry-id"\]|||
|autor opinii|span.user-post__author-name|||
|rekomendacja|span.user-post__author-recomendation > em|||
|liczba gwiazdek|span.user-post__score-count|||
|treść opinii|div.user-post__text|||
|lista zalet|div.review-feature__title--positives ~ div.review-feature__item|||
|lista wad|div.review-feature__title--negatives ~ div.review-feature__item|||
|dla ilu osób przydatna|span[id^="votes-yes"]|||
|dla ilu osób nieprzydatna|span[id^="votes-no"]|||
|data wystawienia opinii|span.user-post__published > time:nth-child(1) ["datetime"]|||
|data zakupuuser-post__published|span.user-post__published > time:nth-child(2) ["datetime"]|||