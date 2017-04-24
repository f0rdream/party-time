let baseUrl

if (process.env.NODE_ENV === 'development') {
  baseUrl = '//127.0.0.1:8000'
} else {
  baseUrl = '//api.skyparade.org'
}

export default baseUrl
