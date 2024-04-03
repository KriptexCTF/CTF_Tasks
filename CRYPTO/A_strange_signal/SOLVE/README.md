Shannon—Fano coding (English: Shannon–Fano coding) is an algorithm for prefix heterogeneous encoding. Refers to probabilistic compression methods.

Next, we need to figure out the algorithm and write a script that creates an encoding table
To do this, we are given a hint on the probabilities:
the _ symbol has a probability of 0.09
the remaining characters are equally likely, therefore
(1 - 0.09)/26 = 0.35

It should turn out like this:
<img width="1432" alt="Screenshot 2024-04-03 at 15 51 28" src="https://github.com/KriptexCTF/CTF_Tasks/assets/120062405/6f77e9a9-5dc1-4726-80c0-a0785e34521a">

Next, run the script and compile the encoding table:
<img width="1470" alt="Screenshot 2024-04-03 at 17 57 46" src="https://github.com/KriptexCTF/CTF_Tasks/assets/120062405/59dd56b6-4ddf-47b0-8718-9c0c40f71d72">


We write the decoder and give it our encrypted string:
<img width="1470" alt="Screenshot 2024-04-03 at 17 59 17" src="https://github.com/KriptexCTF/CTF_Tasks/assets/120062405/ec54b872-4802-4dd9-ba67-0878360b68ae">


Solve!
Flag: congratulation_sensei_you_were_able_to_decrypt_the_message_and_get_the_flag
