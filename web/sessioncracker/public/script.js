import { initializeApp } from 'https://www.gstatic.com/firebasejs/9.10.0/firebase-app.js'
import { getFirestore, getDoc, setDoc, doc } from 'https://www.gstatic.com/firebasejs/9.10.0/firebase-firestore.js'

const firebaseConfig = {
  apiKey: 'AIzaSyDN_2EZMN-1QCJ4V13WYUTV4UKA4Im8lLM',
  authDomain: 'websec-ctfs.firebaseapp.com',
  projectId: 'websec-ctfs',
  storageBucket: 'websec-ctfs.appspot.com',
  messagingSenderId: '617149347368',
  appId: '1:617149347368:web:e34a2bf5fe52fb1b77a71d'
}

// Initialize Firebase

const app = initializeApp(firebaseConfig)

const db = getFirestore(app)

let id = sessionStorage.getItem('id')
const sessionEle = document.getElementById('session')

let data = {}

async function initialize () {
  if (id === null) {
    id = Math.floor(Math.random() * 73439123).toString()
    sessionStorage.setItem('id', id)
    await setDoc(doc(db, 'sessioncracker', id), { supervisor: 'BJtfWvgK7n1cInPAdXNL' })
    sessionEle.innerText = JSON.stringify(data)
  } else {
    const snap = await getDoc(doc(db, 'sessioncracker', id))
    data = snap.data()
    sessionEle.innerText = JSON.stringify(data)
  }
}

initialize()

const key = document.getElementById('key')
const value = document.getElementById('val')

document.getElementById('save').onclick = async () => {
  data[key.value] = value.value
  await setDoc(doc(db, 'sessioncracker', id), data)
  sessionEle.innerText = JSON.stringify(data)
}
