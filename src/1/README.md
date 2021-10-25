Bonus Calculator
================
 
## Wymagania
 
### Indywidualny bonus dla sprzedawcy
 
Zadanie polega na zaimplementowaniu funkcjonalności do zapisu rejestru sprzedaży w celu wyliczenia bonusu jaki otrzyma sprzedawca w danym miesiącu.
Każdy sprzedawca ma ustalony plan sprzedażowy. Od sprzedaży która przekroczy plan dostaje bonus, wyliczony na podstawie prowizji, pomniejszony o podatek: 
 
*Konfiguracja*
 
|Plan sprzedażowy (Quota)|   Prowizja (Commission)|   Podatek (Tax) | 
|-----|----------------------|-------------------------|
| 11 000 |    5%        |                        19%|
 
*Przykład wyliczenia bonusu*
 
|Suma sprzedaży  |Plan sprzedażowy (Quota)|    Prowizja (Commission) |       Podatek (Tax)  | Bonus|
|----------|-----|----------------------|-------------------------|---|
|12 000    | 11 000 |    10%        |                        10%|                90.0|
|12 000    | 15 000 |    10% |                        10%|                0.0|
|12 000    | 12 000|    10% |                    10%|                0.0|
 
*Przykład rejestru sprzedaży zakładając plan sprzedażowy = 15 000*:
 
|data|Sprzedaż|    Suma sprzedaży w danym miesiącu| Wyliczona podstawa do naliczenia bonusu w danym miesiącu|	 
|---|-----|----------|------------|
|25.03.2020| 1 000 | 1 000    | 0 |
|01.04.2020| 5 000 | 5 000    | 0        |
|10.04.2020| 6 000 | 11 000    | 0        |
|15.05.2020| 6 000 | 17 000    | 2 000        |
|03.06.2020| 20 000 | 20 000    | 5 000        |
  
 