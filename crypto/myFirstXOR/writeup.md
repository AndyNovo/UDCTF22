# My First XOR

### Organizer note - here is the story of this problem:

When the student brought me this problem it was originally that they seeded a random number generator from a random word in rockyou.txt.
So when I playtested I didn't want to go bruteforcing so I just used the flag format to see what I could see.  Immediately it was clear that his key was 
ascii of hexadecimal nibbles made from lowercase letters.  That meant that every other letter of the key was `6` or `7`.  Which meant we could read every 
other character of the flag pretty quickly.  I puzzled my way to the flag and decided we'd change the problem and disregard the rockyou stuff and make it
about the error.

## Solution:

Start by using the flag format to [scout a bit](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')XOR(%7B'option':'Latin1','string':'UDCTF%7B'%7D,'Standard',false)&input=NjM3Mjc1NjI3MTRkNmYwOTY1NmM1ZjBkNjk0NTVlNTU2ODAzMDUwYzQyNGIzYzBh)

You see that `UDCTF{` reveals that the key starts with `666676` which was clearly not the intention of the coder.  Instead of 10 random lowercase letters it is 
20 hexadecimal characters of lowercase ascii.  That means that every two bytes of the key comes from the range `61` to `7a`.  [OK let's put in the 
key with '61' repeating for the next 14 bytes to have a baseline.](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')XOR(%7B'option':'Latin1','string':'66667661616161616161'%7D,'Standard',false)&input=NjM3Mjc1NjI3MTRkNmYwOTY1NmM1ZjBkNjk0NTVlNTU2ODAzMDUwYzQyNGIzYzBh)

We see now `UDCTF{Y8S]i<_thd^23=t}<`.

We know that any of the 6s in the key can be swapped for 7s and there will be underscores.  [So let's look at the alternatives for 6/7:](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')XOR(%7B'option':'Latin1','string':'66667671717171717171'%7D,'Standard',false)&input=NjM3Mjc1NjI3MTRkNmYwOTY1NmM1ZjBkNjk0NTVlNTU2ODAzMDUwYzQyNGIzYzBh)

We see now `UDCTF{X8R]h<^tid_22=t}<`.

OK so that means the flag is `UDCTF{` then `X` or `Y` then `?` then `S` or `R`.  That is likely `XOR_` or  `X0R_`, [let's confirm that works](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')XOR(%7B'option':'Latin1','string':'666676X0R_7171717171'%7D,'Standard',false)&input=NjM3Mjc1NjI3MTRkNmYwOTY1NmM1ZjBkNjk0NTVlNTU2ODAzMDUwYzQyNGIzYzBh).

So yeah, `X0R_` or `XoR_` are the viable options there.  At this point I'm leaning [XOR is the best](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')XOR(%7B'option':'Latin1','string':'666676X0R_is_the_best%7D'%7D,'Standard',false)&input=NjM3Mjc1NjI3MTRkNmYwOTY1NmM1ZjBkNjk0NTVlNTU2ODAzMDUwYzQyNGIzYzBh) 
as the message, so I'll drop that in and see which characters lead to an invalid key.

So `UDCTF{X0R_is_the_best}` would lead to a key of ```66667679736~61607a`.66i``` so characters 12,16,19,20 need tweaks.

Well all of those are common l33t sp34k spots, swap them out and get `UDCTF{X0R_i5_th3_b35t}` which makes a valid key.  I'll try it and be aware I might have to tweak `0` to `o`.
