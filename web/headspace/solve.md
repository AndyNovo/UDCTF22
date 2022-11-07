# writeup

first of all we got that we have to use flag.org as referer
so 
```curl -H "Referer: flag.org" https://bluehens-headspace.chals.io/```

response: Access Denied! You are not using a valid agent. Currently you are using: curl/7.80.0
Valid Agents: stealthmodeactive

let's change our agent with -A option in curl

```curl -A "stealthmodeactive" -H "Referer: flag.org" https://bluehens-headspace.chals.io/```

response: Hmmm you seem to be using the wrong protocol. This server could use a PATCH...

ok we need to change the method to PATCH. in curl we do it with -X option

```curl -X PATCH -A "stealthmodeactive" -H "Referer: flag.org" https://bluehens-headspace.chals.io/```

response: Nice! Hopefully you learned a thing or two about HTTP headers :) UDCTF{0uts1d3_t4h_m1nd}

and we got the flag.
