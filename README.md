# Dienasgramata

###
Mans projekta darbs priekšmetā "Lietotājprogrammatūras automatizēšanas rīki" ir universitātes darbu dienasgrāmata. Šajā programmā ir iespējams pievienot uzdevumus, atzīmēt tos kā pabeigtus un šie visi uzdevumi tiks saglabāti failā, kur tie ir sakārtoti secībā pēc uzdevumiem, kuri nav atzīmēti kā pabeigti un, kuru iesniegšanas datums ir visdrīzākais.


Veidojot šo programmu es iemācījos kā izmantot vārdnīcas un kā veidot jaunas funkcijas. Lai šo programmas kodu padaritu īsāku, es izveidoju funkcijas:
     1. pievieno_uzd() -  Šī funkcija no lietotāja prasa jautājumus, kas ir saistīta ar uzdevuma pievienošanu, tas ir, mācību priekšmets, apraksts un nodošanas termins, un šīs ievades pievieno sarakstam un šī uzdevuma sākuma vērtība tiek uzstadita kā "Incomplete"
     2. pabeigts_uzd() - Šī funckija ir paredzēta, lai atzimetu kādu uzdevumu kā pabeigtu. Lietotājam tiek uzdots norādīt kārtas numuru, kuru uzdevumu atzīmēt kā pabeigtu. Tiek veikta pārbaude, vai ievadītais skaitlis ir saraksta robežās. Ja ievadītais numurs ir derīgs, tas tiek iznemts no saraksta task_list un status tiek atzimets kā "Complete".
     3. read_csv_file() - Šī funkcija lasa informāciju no CSV faila. No saraksta iegūst vērtības, kas tiek sagalbātas mainīgajos "Subject", "Description" un "due_date"
     4. write_csv_file() - Šī funkcija ir paredzēta, lai rakstītu informāciju CSV failā, izmantojot task_list sarakstu. Šajā funkcijā arī ir iekļauta faila sakārtošana pēc datumiem un ieraksta to csv failā. 
     5.write_sorted_csv_file() - Šī funkcija izpildas tāpat kā iepriekšējā, taču šeit citā csv failā tiek ievadītas vērtibas, kas ne tikai ir sarakstitas pareizā secībā, bet arī tajā uzrādas tikai tie uzdevumi, kas nav pabeigti.
     6. display_menu() - Šī ir interaktīvais "sākumekrāns", kas parādas programmas sākumā, kur tiek attēlotas izvēles, ko lietotājs var izdarīt. 

Pati programmas daļa ir interaktīvā daļa, kur no lietotāja tiek prasītas ievades. No sākuma tiek izsaukta funkcija, kas nolasa informaciju no saraksta. Tiek izvedots While cikls, kur programma turpina izpildi, kamer netiek ievadits cipars 3 ("Tas iziet no programmas"). Tiek izsaukta funckija "display_menu", kur lietotājam jaievada skaitlis 1-3, kur 1 ir pievienot uzd, 2 ir atzimet uzdevumu kā pabeigtu un 3 ir iziet no programmas. Atkarībā no izvēles, tiek izsaukta funkcija atbilstoši lietotāja izvēlei. Izvēloties iziet no programmas, ievaditie dati tiek sakārtoti un ievaditi "dienasgramata.csv"
