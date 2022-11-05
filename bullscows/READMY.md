# Project Bullscows(django)

![Django](https://img.shields.io/badge/Django-v4.0.1-blue)![SQLite](https://img.shields.io/badge/SQLiteStudio-v3.3.3-yellow)

This is project for personal fun. Browser logical game, where 
the player is guessing 4-digits number. To play, you need to
register or log in. No email, no verifications.

Because of html issues, I didn't created field with check-try
digits. With normal front-end Game model should be added one more 
field, which contains current number of good-guessed digits (4:2).
Instead, I combined string with player try and string with 
check-numbers. Ok, its not a good idea. I will fix it, when 
getting better in front-end.


Game screenshot:
[![bullscows2.png](https://i.postimg.cc/ZKzYKpLp/bullscows2.png)](https://postimg.cc/F1GXTf8H)