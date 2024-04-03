Lets go!
<img width="1054" alt="Screenshot 2024-04-03 at 19 46 53" src="https://github.com/KriptexCTF/CTF_Tasks/assets/120062405/7732133e-7d75-43c4-8d70-108acedd8a28">
We have two files

  1) strange_text.txt -- our alphabet

  2) bit_sequence.txt

And the names Shannon and Fano

Shannon—Fano coding (English: Shannon–Fano coding) is an algorithm for prefix heterogeneous encoding. Refers to probabilistic compression methods.

Next, we need to understand the algorithm and write a script that creates an encoding table.
To do this, we are given a strange text that we must analyze and write down the frequency of occurrence of each character for the further alphabet:
<img width="715" alt="Screenshot 2024-04-03 at 19 37 36" src="https://github.com/KriptexCTF/CTF_Tasks/assets/120062405/0e7da7ef-6541-4396-a01a-7440fdfc4936">

Let's write a simple python script that will analyze our text:
<img width="1469" alt="Screenshot 2024-04-03 at 19 40 30" src="https://github.com/KriptexCTF/CTF_Tasks/assets/120062405/3e59b3ee-d603-4a1c-8b49-0d85fd5a0e8b">
At the output of the script, we received two arrays A and B. Alphabet a is all the characters that we will use, and alphabet B is the probability of the appearance of these characters



It should look like this:
<img width="1431" alt="Screenshot 2024-04-03 at 19 42 43" src="https://github.com/KriptexCTF/CTF_Tasks/assets/120062405/78b09af0-53a3-4063-aa1e-169150c3eb99">


Next, run the script and compile the encoding table:
<img width="1470" alt="Screenshot 2024-04-03 at 19 43 40" src="https://github.com/KriptexCTF/CTF_Tasks/assets/120062405/92e82ba3-b42c-4c99-ba3d-32be72f66dd1">



We write the decoder and give it our encrypted string:
<img width="1470" alt="Screenshot 2024-04-03 at 19 44 36" src="https://github.com/KriptexCTF/CTF_Tasks/assets/120062405/84accea7-65e9-447b-a9bd-35d58b1586ba">


Solve!
Flag: congratulation_sensei_you_were_able_to_decrypt_the_message_and_get_the_flag
