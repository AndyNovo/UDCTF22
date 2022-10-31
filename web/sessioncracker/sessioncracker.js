const express = require('express')
const bodyParser = require('body-parser')
const fs = require('fs')

const server = express()
server.use(bodyParser.json())

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

server.use(express.static('public'))

server.listen(8080)

console.log('Starting session cracker on port 8080')
