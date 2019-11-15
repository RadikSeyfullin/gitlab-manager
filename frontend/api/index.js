import axios from 'axios'

export default {
    loginIn(method, params, data) {
        if (method === 'post') {
            return ajax('http://127.0.0.1:8000/auth/token/login/', 'post', data)
        } else {
            return ajax('http://127.0.0.1:8000/user/', 'get', {})
        }
    }
}

/**
 * @param url
 * @param method
 * @param params
 * @param data
 * @returns
 */

function ajax(url, method, options) {
    if (options !== undefined) {
        var {params = {}, data = {}} = options
    } else {
        params= data = {}
    }
    console.log(method + " " + url)
    console.log(params)
    console.log(data)
    return new Promise((resolve, reject) => {
        axios({
            url,
            method,
            params,
            data,
            headers: {
                'Content-Type':'application/x-www-form-urlencoded'
            }
        }).then(res => {
            resolve(res)
        }, res => {
            reject(res)
        })
    })
  }
  