export function getCookie(name) {
  const value = `; ${document.cookie}`
  const parts = value.split(`; ${name}=`)
  if (parts.length === 2) return parts.pop().split(';').shift()
  return undefined
}

export function setCookie(name, value, options = {}) {
  let updatedCookie = encodeURIComponent(name) + '=' + encodeURIComponent(value)

  for (let optionKey in options) {
    updatedCookie += `; ${optionKey}`
    let optionValue = options[optionKey]
    if (optionValue !== true) {
      updatedCookie += `=${optionValue}`
    }
  }

  document.cookie = updatedCookie
}

export function removeCookie(name, options = {}) {
  setCookie(name, '', {
    'max-age': -1,
    ...options,
  })
}
