const keyText = document.getElementById('key')

function sleep (ms) {
  return new Promise(resolve => setTimeout(resolve, ms))
}

async function getKey () {
  try {
    const req = await fetch(`${window.location.href}key`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        timestamp: Date.now()
      })
    })

    const { key } = await req.json()

    return key
  } catch (err) {
    console.error(err)
    return ''
  }
}

function updatePage (key) {
  keyText.innerText = key
}

async function main () {
  while (true) {
    const key = await getKey()
    console.log(key) // Keep a history of past keys
    updatePage(key)
    await sleep(120000)
  }
}

main()

// ${window.location.href}/test
