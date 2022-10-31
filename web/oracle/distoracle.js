const express = require('express')
const bodyParser = require('body-parser')
const AES = require('crypto-js/aes')
const ECBMode = require('crypto-js/mode-ecb')
const PKCS7 = require('crypto-js/pad-pkcs7')

const server = express()
server.use(bodyParser.json())

const raw = 'REDACTED'
const flag = 'U2FsdGVkX19+39o87YO7Zj+D9Og1WLYWUMqboh+IWypf1plXoTmOcBysQuPa8wye'
const key = 'REDACTED'
//length of key is 32 bytes

async function generateMagicAnswer (magic) {
  const hash = AES.encrypt(magic, key, {
    mode: ECBMode,
    padding: PKCS7
  })

  return hash.toString()
}

server.get('/', async function (req, res) {
  res.send(`Welcome to the oracle, see if you can answer your way to the flag. You may ask me anything. </br>
  For example go to /ask/whereistheflag?`)
})

server.get('/flag', async function (req, res) {
  res.send(`Fine, you can have the flag. In the language of the universe of course! </br>
  What? You don't understand that? That sounds like a you problem. </br></br> <strong>${flag}</strong>`)
})

server.get('/ask', async function (req, res) {
  res.send('Hmm it looks like you wanted to ask something but never input it? Remember it needs to be /ask/yourquestion')
})

server.get('/ask/:magic', async function (req, res) {
  const { magic } = req.params

  let index = 0

  for (let i = 0; i < magic.length; i++) {
    index += magic.charCodeAt(i)
  }

  const answer = await generateMagicAnswer(magic)
  res.send(`
    <!DOCTYPE html>
    <body>
      <p>Ah I see, here is your answer... in the natural language of the universe</p>
      <p><strong>${answer}</strong></p>
    </body>
    <script>
      console.error('AES (ECB, PKCS7) Internal Error: Encryption error!')
      console.error('Leaked REDACTED')
    </script>
  `)
})

server.listen(8080)

console.log('Starting server on port 8080')
