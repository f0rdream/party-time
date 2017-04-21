let storeMap = new Map()

storeMap.set('username', '')
storeMap.set('isLogin', false)

function setMap (key, value) {
  storeMap.set(key, value)
}
function getMap (key) {
  return storeMap.has(key) ? storeMap.get(key) : window.console.log('Undefined key!')
}

export { setMap, getMap }
