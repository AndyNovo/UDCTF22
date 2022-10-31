const express = require('express')
const bodyParser = require('body-parser')
const fs = require('fs')
const AES = require('crypto-js/aes')
const ECBMode = require('crypto-js/mode-ecb')
const PKCS7 = require('crypto-js/pad-pkcs7')

const server = express()
server.use(bodyParser.json())

const flag = 'UDCTF{y05_g0t_1t_j0st_1n_t1m3!}'

server.get('/', async function (req, res) {
  try {
    fs.readFile('./public/index.html', (error, data) => {
      if (error) {
        throw error
      }
      res.send(data.toString())
    })
  } catch (err) {

  }
})

function getDegree (hours, minutes) {
  const sum = minutes + (hours * 60)
  const degrees = Math.floor((sum * 0.5) % 360)

  return degrees
}

function handsOfTime (hours, minutes) {
  console.log(`${hours}:${minutes}`)

  const degrees = getDegree(hours, minutes)

  console.log(degrees)

  return degrees.toString()
}

server.post('/key', async function (req, res) {
  try {
    const { timestamp } = req.body

    const now = new Date(timestamp)

    const rawKey = handsOfTime(now.getHours(), now.getMinutes())

    const encrypted = AES.encrypt(flag.concat(flag), rawKey, {
      mode: ECBMode,
      padding: PKCS7
    })

    res.status(200).json({ key: encrypted.toString() })
  } catch (err) {
    console.error(err)
    res.sendStatus(500)
  }
})

server.get('/test', async function (req, res) {
  try {
    fs.readFile('./public/hint.html', (error, data) => {
      if (error) {
        throw error
      }
      res.send(data.toString())
    })
  } catch (err) {

  }
})

server.use(express.static('public'))

server.listen(8080)

console.log('Starting server on port 8080')
