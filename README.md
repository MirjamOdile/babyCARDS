# babyCARDS: Binary computer-assisted recognition of (climate change) contrarian speech
*Detecting climate change contrarian language.*

This repository shares multiple binary logistic classifiers to distinguish between climate change **contrarian** and **convinced** written text. It has been trained on a large corpus of documents by known contrarian and convinced actors and organisations. 

# Contents
  * [Classifiers](#classifiers)
    + [Download](#download)
  * [Classifier performance](#classifier-performance)
  * [Data](#data)
    + [Summary](#summary)
    + [Sources](#sources)
      + [Blogs](#blogs)
      + [NGOs](#ngos)
      + [Thinktanks](#thinktanks)
      + [Twitter](#twitter)
      + [Facebook](#facebook)
      + [Newspapers](#newspapers)
  * [Thanks ⭐🌟](#thanks)
<br>

## Classifiers

Four classifiers have been trained, namely

1) **babyCARDS**: a binary logistic classifier on complete documents by various blog/ngo/thinktank posts, twitter and facebook posts and newspaper articles (N = 4,833,107 posts/articles),

2) **climatebabyCARDS**: a binary logistic classifier on a subset on the documents in 1) that mention the keywords *climate* or *global warming* (N = 567,638 posts/articles),

3) **sentenceCARDS**: a binary logistic classifier trained on the documents in 1) at the sentence level, and

4) **socialCARDS**: a binary logistic classifier only trained twitter and facebook posts (N = 4,493,822 posts).
<br>

### Download

The trained classifiers can be downloaded [here](https://drive.google.com/drive/folders/1dNF6gFELorob8KipqlQwrphRrnrxKxRU?usp=sharing).

<br>

## Classifier performance
Classifier performance was assessed on a **held out** testing data set containing only text from "unseen" sources, i.e. organisations, twitter accounts, facebook accounts and newspaper articles that the classifiers have not been trained on, providing an insight into external validity.

<br>

```
Performance babyCARDS:

Validation data:

              precision    recall  f1-score   support

           0       0.87      0.90      0.88    509797
           1       0.91      0.88      0.90    597768

    accuracy                           0.89   1107565
   macro avg       0.89      0.89      0.89   1107565
weighted avg       0.89      0.89      0.89   1107565



Testing data (unseen organisations, twitter accounts, facebook accounts and newspaper articles):

              precision    recall  f1-score   support

           0       0.71      0.90      0.80    180897
           1       0.90      0.70      0.79    221956

    accuracy                           0.79    402853
   macro avg       0.80      0.80      0.79    402853
weighted avg       0.81      0.79      0.79    402853
```
<br>

```
Performance climatebabyCARDS:

Validation data:

              precision    recall  f1-score   support

           0       0.93      0.94      0.94     69659
           1       0.93      0.92      0.92     56967

    accuracy                           0.93    126626
   macro avg       0.93      0.93      0.93    126626
weighted avg       0.93      0.93      0.93    126626



Testing data (unseen organisations, twitter accounts, facebook accounts and newspaper articles):

              precision    recall  f1-score   support

           0       0.71      0.93      0.81     24090
           1       0.95      0.75      0.84     37052

    accuracy                           0.82     61142
   macro avg       0.83      0.84      0.82     61142
weighted avg       0.85      0.82      0.83     61142
```
<br>

```
Performance sentenceCARDS:

Validation data:

              precision    recall  f1-score   support

           0       0.74      0.76      0.75   1437268
           1       0.84      0.83      0.83   2161986

    accuracy                           0.80   3599254
   macro avg       0.79      0.79      0.79   3599254
weighted avg       0.80      0.80      0.80   3599254



Testing data (unseen organisations, twitter accounts, facebook accounts and newspaper articles):

              precision    recall  f1-score   support

           0       0.69      0.79      0.74    757918
           1       0.84      0.75      0.79   1075225

    accuracy                           0.77   1833143
   macro avg       0.76      0.77      0.76   1833143
weighted avg       0.78      0.77      0.77   1833143
```
<br>

```
Performance socialCARDS:

Validation data:

              precision    recall  f1-score   support

           0       0.88      0.90      0.89    484130
           1       0.91      0.89      0.90    547607

    accuracy                           0.90   1031737
   macro avg       0.90      0.90      0.90   1031737
weighted avg       0.90      0.90      0.90   1031737



Testing data (unseen twitter and facebook accounts):

              precision    recall  f1-score   support

           0       0.70      0.90      0.79    166797
           1       0.89      0.67      0.77    200079

    accuracy                           0.78    366876
   macro avg       0.79      0.79      0.78    366876
weighted avg       0.80      0.78      0.78    366876
```

## Data

### Summary

| All posts/articles (N)  |   Convinced |  Contrarian |       **∑** | | Climate related (CR) |  Convinced | Contrarian |      **∑** |
|-------------------------|------------:|------------:|------------:|-|----------------------|-----------:|-----------:|-----------:|
| blog/thinktank/ngo      |      110773 |      219535 |  **330308** | | blog/thinktank/ngo   |      54748 |     112068 | **166816** |
| facebook                |      527951 |      425551 |  **953502** | | facebook             |      44231 |      31055 |  **75286** |
| newspaper               |        5488 |        3489 |    **8977** | | newspaper            |       4886 |       2762 |   **7648** |
| twitter                 |     1573621 |     1966699 | **3540320** | | twitter              |     199641 |     118247 | **317888** |
| **∑**                   | **2217833** | **2615274** | **4833107** | | **∑**                | **303506** | **264132** | **567638** |


### Sources

The following tables summarise the documents used to train the different classifiers. Each table provides document counts per organisation/actor for a different medium (blog, thinktank, ngo, twitter, facebook, newspaper) by side (convinced/contrarian). 

The columns **N** display the total document counts used for babyCARDS, sentenceCARDS and socialCARDS (limited to the twitter and facebook table), whereas the columns **CR** show the climate related document counts used for the climatebabyCARDS classifier.

#### Blogs

| Convinced	(0)	&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; N | &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; CR | Contrarian (1) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; N | &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; CR |
|:-----------------------------|------:|------:|:----------------------------|------:|------:|
| desmogblog.com               |    42 |    39 | anhonestclimatedebate       |   982 |   850 |
| grist.org                    | 51101 | 19150 | australianclimatemadness    |  2526 |  2137 |
| realclimate.org              |   494 |   471 | bishop_hill                 |  5204 |  2852 |
| scienceblogs.com             |  2201 |  1116 | bobtisdale                  |   888 |   711 |
| skepticalscience.com         |  2794 |  2747 | c3headlines                 |  2122 |  1796 |
| yaleclimateconnections.org   |  1614 |  1583 | chiefio                     |  1616 |   575 |
|                              |       |       | cliffmass                   |  1506 |   277 |
|                              |       |       | climate_resistance          |   572 |   549 |
|                              |       |       | climate_skeptic             |   619 |   517 |
|                              |       |       | climateaudit                |  2506 |  1626 |
|                              |       |       | climatechangedispatch       |  3318 |  2991 |
|                              |       |       | climateconversation         |   894 |   743 |
|                              |       |       | climatesanity               |   175 |    97 |
|                              |       |       | co2science                  |  5230 |  3696 |
|                              |       |       | coolerheads                 |  3158 |  1971 |
|                              |       |       | coyoteblog                  |  6294 |   670 |
|                              |       |       | dailybayonet                |  1398 |   679 |
|                              |       |       | drtimball                   |   207 |   203 |
|                              |       |       | galileomovement             |    26 |    21 |
|                              |       |       | gorelied                    |   981 |   691 |
|                              |       |       | gwpf                        |   163 |   163 |
|                              |       |       | hauntingthelibrary          |   174 |   155 |
|                              |       |       | hockeyschtick               |  2582 |  2126 |
|                              |       |       | iceagenow                   |  4004 |  1155 |
|                              |       |       | jonova                      |  1841 |  1445 |
|                              |       |       | judith_curry                |  1333 |  1276 |
|                              |       |       | junkscience                 | 18649 |  7722 |
|                              |       |       | klimatupplysningen          |  4735 |  3400 |
|                              |       |       | manicbeancounter            |   393 |   221 |
|                              |       |       | marohasy                    |  2992 |  1536 |
|                              |       |       | masterresource              |  1847 |  1025 |
|                              |       |       | motls                       |  6023 |  1809 |
|                              |       |       | noconsensus                 |  1312 |   905 |
|                              |       |       | nofrakkingconsensus         |   605 |   281 |
|                              |       |       | notalotofpeopleknowthat     |  1929 |  1097 |
|                              |       |       | notrickszone                |  2351 |  1873 |
|                              |       |       | nzclimatescience            |   256 |   208 |
|                              |       |       | omnologos                   |  2172 |   879 |
|                              |       |       | principia-scientific        |   984 |   654 |
|                              |       |       | rankexploits                |  1267 |   617 |
|                              |       |       | rationaloptimist            |   513 |   176 |
|                              |       |       | real_science                | 11141 |  4909 |
|                              |       |       | realclimatescience          |   271 |   185 |
|                              |       |       | roger_pielke                |  2206 |  2077 |
|                              |       |       | rogerpielkejr               |  1563 |   992 |
|                              |       |       | roy_spencer                 |   595 |   376 |
|                              |       |       | scottish_sceptic            |   728 |   555 |
|                              |       |       | small_dead_animals          | 14373 |   940 |
|                              |       |       | sppi                        |  2525 |  1962 |
|                              |       |       | tallbloke                   |  2455 |  1161 |
|                              |       |       | thelukewarmersway           |   290 |   274 |
|                              |       |       | theresilientearth           |   497 |   433 |
|                              |       |       | tom_nelson                  | 21740 | 17831 |
|                              |       |       | warwickhughes               |   851 |   352 |
|                              |       |       | wmbriggs                    |  2363 |   555 |
|                              |       |       | worldclimatereport          |   515 |   504 |
|                              |       |       | wuwt                        | 12676 |  9550 |


#### NGOs

| Convinced	(0)	&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; N | &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; CR | Contrarian (1) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; N | &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; CR |
|:--------------------------|-----:|-----:|:-----------|--:|---:|
| 350.org                   | 2718 | 2131 |            |   |    |
| c2es.org                  |  106 |  105 |            |   |    |
| ceres.org                 |  231 |  231 |            |   |    |
| climaterealityproject.org |  778 |  748 |            |   |    |
| climatesolutions.org      |  532 |  509 |            |   |    |
| earthjustice.org          | 1614 |  649 |            |   |    |
| edf.org                   |  193 |  186 |            |   |    |
| foe.org                   | 2341 | 1409 |            |   |    |
| greenpeace.org            | 1578 | 1462 |            |   |    |
| iclei.org                 |  543 |  390 |            |   |    |
| nature.org                | 1771 |  593 |            |   |    |
| nrdc.org                  | 9990 | 7170 |            |   |    |
| nwf.org                   | 8643 | 3428 |            |   |    |
| sierraclub.org            | 7253 | 3170 |            |   |    |
| ucsusa.org                | 1967 | 1880 |            |   |    |
| usclimatenetwork.org      |   45 |   45 |            |   |    |
| wri.org                   | 2615 | 1992 |            |   |    |


#### Thinktanks

| Convinced	(0)	&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; N | &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; CR | Contrarian (1) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; N | &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; CR |
|:---------------|-----:|-----:|:------------------------|------:|-----:|
| brookings.edu  | 6976 | 1609 |                 aei.org |  1649 | 1492 |
| cifor.org      |   17 |   17 |                cato.org |    28 |   28 |
| cmcc.it        |  586 |  511 |                 cei.org |  3600 | 3465 |
| die-gdi.de     |  137 |  134 |               cfact.org |  1613 | 1578 |
| iiasa.ac.at    |  407 |  238 |     fraserinstitute.org |  1047 |  212 |
| odi.org        |  722 |  310 |            free-eco.org |   909 |  149 |
| pik-potsdam.de |  529 |  528 |           heartland.org | 31990 | 6027 |
| teriin.org     |  147 |  111 |            heritage.org |   333 |  333 |
| ufz.de         |   88 |   86 |              hoover.org |   532 |  459 |
|                |      |      |              hudson.org |  2853 |  276 |
|                |      |      | manhattan-institute.org |   389 |  364 |
|                |      |      |            marshall.org |   130 |  127 |
|                |      |      |                ncpa.org |   112 |   30 |
|                |      |      |               ncppr.org |  1246 |  586 |
|                |      |      |     pacificresearch.org |   441 |  429 |
|                |      |      |              reason.org |    37 |   28 |
|                |      |      |            sppiblog.org |  1490 | 1454 |


#### Twitter

| Convinced	(0)                     |      N |    CR | Contrarian (1)                               |      N |    CR |
|:----------------------------------|-------:|------:|:---------------------------------------------|-------:|------:|
| Al Gore                           |   2775 |  1143 | ACSH                                         |   1654 |    10 |
| Bill McKibben                     |  26466 |  3684 | AEI                                          |  21920 |    71 |
| Bloomberg Green                   |  24073 |  5464 | Activist Post                                | 152940 |   854 |
| Carbon Brief                      |  45744 | 17182 | Alex Epstein                                 |   8307 |   969 |
| Climate Central                   |  58643 | 21163 | Alexandra Marshall                           |  71575 |  1784 |
| Climate Council                   |  20347 |  9237 | Bjorn Lomborg                                |   6723 |  1886 |
| Climate Power                     |  36997 | 11266 | Breitbart News                               | 143929 |   617 |
| Climate Tracker                   |  10932 |  4436 | CFACT                                        |   7616 |  2685 |
| Dr. Ayana Elizabeth Johnson 🐙    |     27 |     5 | Capital Research                             |   4655 |   118 |
| Dr. Genevieve Guenther            |  35872 |  8479 | Cato Institute                               |  55279 |   548 |
| Dr. Kim Cobb                      |   6352 |  1336 | CatoTheYounger                               |  80847 |  1540 |
| EDF                               |  29661 |  8687 | Climate Realists                             |   3158 |   553 |
| Ed Hawkins                        |   8059 |  1690 | Competitive Enterprise Institute             |  23678 |  1155 |
| Friends of the Earth - since 1971 |  28601 |  3567 | David Rose                                   |   7037 |   486 |
| Gavin Schmidt                     |  18142 |  2227 | Energy Brief                                 |   6820 |   760 |
| Global Action Plan                |  10766 |   703 | Energy Citizens                              |   7198 |    85 |
| Greenpeace UK                     |  34934 |  3126 | Fox News                                     |  60680 |    67 |
| Greta Thunberg                    |   2351 |  1044 | FreedomWorks                                 | 103528 |   613 |
| HuffPost Green                    |    840 |    92 | Friends of Science                           |  64861 | 20694 |
| IPCC                              |   5315 |  3390 | Frontiers of Freedom                         |   1841 |    41 |
| Kate Marvel                       |   5372 |   877 | George Szabo                                 |  56773 |   426 |
| Mark Z. Jacobson                  |  14425 |  1606 | HaveWeAllGoneMad                             |  47747 |   783 |
| Marshall Shepherd                 |  48374 |  4280 | Heritage Foundation                          |  79397 |   814 |
| NASA Climate                      |   3612 |  1329 | Hudson Institute                             |   6602 |    33 |
| Naomi Klein                       |   7588 |   723 | Institute for Energy Research                |  18435 |  1217 |
| Oxfam                             |  87866 |  1234 | Ivo Vegter                                   |  63040 |  1184 |
| Pew Environment                   |  33825 |  1103 | Judith Curry                                 |   7416 |  2842 |
| Planet Green                      |  67541 |   739 | Manhattan Institute                          |  71510 |   856 |
| Prof Michael E. Mann              |  63105 | 15607 | Marc Morano                                  |   6775 |  1970 |
| Prof. Katharine Hayhoe            |  39969 |  7865 | Matt Ridley                                  |  11633 |   439 |
| Project Drawdown                  |   2677 |  1241 | Michael Shellenberger                        |  10527 |   811 |
| Sunrise Movement 🌅               |  12457 |  3438 | Mike Jagger                                  |  49428 |  5202 |
| The Conversation                  |  62156 |  1870 | Mr. Ross                                     |  43943 |  2825 |
| The Ecologist                     |  18589 |  2850 | Naomi Seibt                                  |   1952 |   120 |
| The Guardian                      | 329360 |  2983 | National Center                              |   6545 |   429 |
| The Nature Conservancy            |  27314 |  2916 | Nigella™️                                    |  42135 |   434 |
| The Washington Post               | 133800 |  1136 | ORWELL WAS RIGHT                             |  28495 |  1630 |
| Treehugger.com                    |  51727 |  1951 | PRI                                          |  11008 |    93 |
| UN Climate Change                 |  20713 | 11616 | Patrick Moore                                |  22721 |  4963 |
| UN Environment Programme          |  25598 |  5166 | Reason Foundation                            |   2285 |    21 |
| Union of Concerned Scientists     |  15433 |  2919 | Roger Pielke Jr.                             |   8385 |  1067 |
| WWF Climate & Energy              |   5907 |  3355 | Ryan                                         |   3580 |   336 |
| grist                             |  89316 | 14916 | Stephen McIntyre                             |   2200 |    48 |
|                                   |        |       | Steve Milloy                                 |   9680 |  2942 |
|                                   |        |       | Stop These Things                            |   6321 |    96 |
|                                   |        |       | The Daily Signal                             |  47895 |   497 |
|                                   |        |       | The Fraser Institute                         |  11191 |   249 |
|                                   |        |       | The Heartland Institute                      |  43463 |  7972 |
|                                   |        |       | The Prospector                               |   1056 |    48 |
|                                   |        |       | Toima                                        |  45898 |  2504 |
|                                   |        |       | Tom Nelson                                   |   4811 |  2675 |
|                                   |        |       | Tony Heller                                  | 147380 | 25424 |
|                                   |        |       | Totally Fake 'President' James Delingpole    |  56578 |   785 |
|                                   |        |       | USA RCRessler                                |   8752 |   109 |
|                                   |        |       | Washington Policy                            |   2299 |    40 |
|                                   |        |       | Watts Up With That                           |  29719 |  8983 |
|                                   |        |       | rmack2x                                      |  55015 |  1792 |
|                                   |        |       | velardedaoiz2                                |  58870 |    51 |
|                                   |        |       | 🌹 ELIANA BENADOR 🌹                          |    993 |     1 |


#### Facebook

| Convinced	(0)                 |      N |   CR | Contrarian (1)                                                  |      N |   CR |
|:------------------------------|-------:|-----:|:----------------------------------------------------------------|-------:|-----:|
| Al Gore                       |    967 |  514 | Acton Institute                                                 |   9569 |   68 |
| Bloomberg Green               |  11007 | 2048 | American Council on Science and Health                          |   8028 |   38 |
| Carbon Brief                  |   2136 | 1084 | American Enterprise Institute                                   |   5847 |   27 |
| Climate Central               |  10735 | 4225 | American Policy Center                                          |    234 |    4 |
| Climate Power                 |   8980 | 2278 | Breitbart                                                       | 102038 |  524 |
| Climate Tracker               |   5434 | 2504 | CFACT                                                           |   3484 | 2045 |
| Dr. Marshall Shepherd         |   3308 |  506 | CO2 Coalition                                                   |    974 |  419 |
| Ed Hawkins                    |    163 |   68 | Capital Research Center                                         |   3151 |   95 |
| Environmental Defense Fund    |   4649 | 1601 | Climate Change Dispatch                                         |   6276 | 4694 |
| Friends of the Earth          |   2997 |  690 | Climate Change LIES                                             |   3552 | 1064 |
| Global Action Plan            |    670 |   68 | Climate Change is Crap                                          |   2842 | 1112 |
| Greenpeace UK                 |  10935 | 1318 | Climate Depot                                                   |    289 |  122 |
| Greta Thunberg                |    960 |  655 | Climate change is natural                                       |  24068 | 3833 |
| Grist.org                     |  27765 | 4130 | Competitive Enterprise Institute                                |   5246 |  295 |
| HuffPost                      | 116126 |  349 | Discovery Institute                                             |   2296 |   21 |
| IPCC                          |   2626 | 1264 | Ethan Allen Institute                                           |   2297 |  130 |
| Katharine Hayhoe              |   1309 |  969 | Fdtn. for Research on Economics and the Environment             |     25 |    1 |
| Michael E. Mann               |   7865 | 5419 | Fox News                                                        |  90708 |  336 |
| NASA Climate Change           |   1814 |  786 | FreedomWorks                                                    |  11083 |   73 |
| Naomi Klein                   |   2330 |  240 | Friends of Science                                              |   9874 | 3459 |
| Oxfam Great Britain           |   2263 |  159 | Frontiers of Freedom                                            |   1678 |   82 |
| Planet Green                  |  14678 |  112 | Heartland Institute                                             |   6309 |  970 |
| Project Drawdown              |   1255 |  595 | Hudson Institute                                                |   1176 |    5 |
| Sunrise Movement              |   2040 |  808 | I Love Carbon Dioxide                                           |   1840 |  503 |
| The Climate Council           |   3944 | 1716 | Inconvenient Facts                                              |   1233 |  492 |
| The Conversation              |  18070 |  596 | Independent Institute                                           |  15970 |  197 |
| The Ecologist                 |   7497 |  988 | Is There Global Cooling                                         |   1967 |  458 |
| The Guardian                  | 102723 |  772 | Junk Science                                                    |     27 |    0 |
| The Nature Conservancy        |   3478 |  332 | Manhattan Institute for Policy Research                         |   3934 |   55 |
| The Pew Charitable Trusts     |   3764 |   40 | Master Resource Blog                                            |    206 |   63 |
| TreeHugger                    |  24823 |  440 | National Center for Public Policy Research                      |   3028 |  102 |
| UN Climate Change             |   5498 | 3187 | Pacific Research Institute                                      |   5473 |   59 |
| UN Environment Programme      |   6846 | 1770 | Property & Environment Research Center (PERC)                   |   2715 |   97 |
| Union of Concerned Scientists |   3191 |  735 | Reason Foundation                                               |    695 |    8 |
| WWF Climate & Energy Practice |    752 |  487 | Small Business & Entrepreneurship Council                       |   2573 |    7 |
| Washington Post               | 104353 |  778 | South Carolina Policy Council                                   |    976 |    1 |
|                               |        |      | The Cato Institute                                              |  12989 |  144 |
|                               |        |      | The Daily Signal                                                |  24674 |  221 |
|                               |        |      | The Fraser Institute                                            |   3963 |   68 |
|                               |        |      | The Galileo Movement                                            |   1011 |  258 |
|                               |        |      | The Heritage Foundation                                         |  22406 |  204 |
|                               |        |      | The Rational Optimist                                           |      1 |    0 |
|                               |        |      | Washington Policy Center                                        |   2691 |   60 |
|                               |        |      | World Wide Protest Against the Global Warming SCAM              |    483 |  225 |
|                               |        |      | wattsupwiththat                                                 |  15652 | 8416 |


#### Newspapers

| Convinced	(0)	&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; N | &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; CR | Contrarian (1) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; N | &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; CR |
|:--------------------|-----:|-----:|:------------------|-----:|-----:|
| The Conversation    | 1099 | 1028 | Daily Telegraph   |  746 |  613 |
| The Guardian        | 2192 | 2018 | Herald-Sun        |  467 |  275 |
| The Washington Post | 2197 | 1840 | The Australian    | 2276 | 1874 |


## Thanks

Thanks to Constantine Boussalis, Travis Coan, John Cook and Mohit Gupta for their collaboration and their contributions to the data and code! ⭐🌟 
