All we have is a photo task.png

<img width="820" alt="Screenshot 2024-04-09 at 12 34 52" src="https://github.com/KriptexCTF/CTF_Tasks/assets/120062405/77513a36-6c3d-4bbe-ad12-ce99a41fe11c">

The tooltip says what the flag is at the bottom, but it's not there

The idea of ​​the task is that physically the photo contains more data than we see, to solve the problem we need to change the IHDR chunk

Open hexedit and change the height of the photo to see more information

<img width="922" alt="Screenshot 2024-04-09 at 12 38 05" src="https://github.com/KriptexCTF/CTF_Tasks/assets/120062405/eb911cc9-d69a-4a47-bf36-e4a86578477b">

We need bytes at positions 0x17 and 0x18, they are responsible for the height.
In our case, the height of the photo is 0x370 == 880 in the decimal system.
Let's change 880 to 1300 == 0x514

<img width="922" alt="Screenshot 2024-04-09 at 12 41 14" src="https://github.com/KriptexCTF/CTF_Tasks/assets/120062405/65777d72-d92f-47e7-ac90-7022a0766c41">

The last step will be to calculate the crc of the chunk, for this the crc32 algorithm is used

In the crc32 algorithm we must put bytes with the name of the chunk and data before the start of crc. In my case crc starts at 0x1D


We use the site https://crccalc.com to calculate our crc

<img width="877" alt="Screenshot 2024-04-09 at 12 44 46" src="https://github.com/KriptexCTF/CTF_Tasks/assets/120062405/fabe7a65-80ad-4eed-854f-5abfbaa0aa45">

Now let's write the resulting crc into png and save it
<img width="922" alt="Screenshot 2024-04-09 at 12 47 01" src="https://github.com/KriptexCTF/CTF_Tasks/assets/120062405/81eeeb8f-a975-44ba-a759-d4860f7434f2">

As a result, we took away this photo where our flag is visible
<img width="820" alt="Screenshot 2024-04-09 at 12 48 13" src="https://github.com/KriptexCTF/CTF_Tasks/assets/120062405/2cf5808f-9e37-4be1-a8c5-19b3e95d279c">

Flag is: CryptexCTF{ju$t_l00k_bEl0w_Y0u}
