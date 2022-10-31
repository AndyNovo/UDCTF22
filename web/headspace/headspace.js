const express = require('express')
const bodyParser = require('body-parser')
const fs = require('fs')

const server = express()
server.use(bodyParser.json())

const flag = 'UDCTF{0uts1d3_t4h_m1nd}'

server.get('/', async function (req, res) {
  const agent = req.header('User-Agent')
  const referer = req.header('Referer')

  if (referer !== 'flag.org') {
    res.send('Access Denied! You don\'t appear to be coming from the site \'flag.org\'\n')
  } else if (agent !== 'stealthmodeactive') {
    res.send(`Access Denied! You are not using a valid agent. Currently you are using: ${agent}\n
    Valid Agents: stealthmodeactive`)
  } else {
    res.send('Hmmm you seem to be using the wrong protocol. This server could use a PATCH...\n')
  }
})

server.patch('/', async function (req, res) {
  res.send(`Nice! Hopefully you learned a thing or two about HTTP headers :) ${flag} \n`)
})

server.listen(8080)

console.log('Starting server on port 8080')
