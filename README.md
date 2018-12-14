# sentimentanalysis
Created by :
- Misael Jonathan
- Aldo Bima Syahputra

TAHAP PENGERJAAN
===================================================================
Note : 
Langkah menjalankan melalui local :
1) download semua requirements "pip -m install requirements.txt"
2) Jalankan "py app.py" untuk menjalankan flask app
3) Akses localhost:5000 untuk melihat website

===================================================================

1) melakukan fetching tweets sebanyak 100.000 (dilakukan sekala berkala) dengan cara menjalankan script tweets/jokowi.py dan tweets/prabowo.py. Hasil akan disimpan di tweets/tweets_prab_raw.txt dan tweets/tweets_prab_raw.txt 

2) kemudian melakukan preprocessing data raw tersebut dengan menjalankan clean.pl (harus diedit file mana yang ingin diclea pada code). Akan disimpan pada tweets/tweets_cleaned_jkw.txt dan tweets/tweets_cleaned_prab.txt

3) melakukan fetching tweets dari user2 tertentu untuk mengumpulkan kata2 leksikon (secara manual dan tidak banyak) Kemudain digabung dengan leksikon yang kami dapat dari https://github.com/yasirutomo/php-sentianalysis-id dan https://github.com/masdevid/ID-OpinionWords. leksikon disimpan pada file Analisis/negative_gabung.txt dan Analisis/positive_gabung.txt. Kemudian ada juga daftar negating words.

4) Setelah itu akan dilakukan pengecekan polarity dari daftar tweets yang sudah diclean dengan menjalankan Analisis/analysis.py (harus diesit dalamnya utk mengatur nama file in and out) akan disimpan di Analisis/result_jkw.txt dan Analisis/result_prab.txt

5) Kemudian dari data tersebut kami olah datanya menjadi chart

<<<<<<< HEAD
Cara Penggunaan :
1) heeee
=======
>>>>>>> 3de1833ea061e26122f2c4dde3de9ac27d7a4c83
