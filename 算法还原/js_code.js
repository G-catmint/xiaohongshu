var CrytoJS = require('crypto-js')
const getPayload = require('./enc3des')



function MD5Test(text){
    return CrytoJS.MD5(text).toString()
}


function get_x_s(url,data,cookie) {
    astr = "url="+url+JSON.stringify(data)
    console.log(astr)
    var x1 = CrytoJS.MD5(astr).toString()
        ,x2 = '0|0|0|1|0|0|1|0|0|0|1|0|0|0|0'
        ,x3 = cookie
        ,x4 = 1713338445383
        ,source = 'x1='+x1+';x2='+x2+';x3='+x3+';x4='+x4+';'
        console.log(source)
        ,b = btoa(source)
        ,a = getPayload.encrypt(b)
    console.log(a)
    x_s = '{"signSvn":"51","signType":"x1","appId":"xhs-pc-web","signVersion":"1","payload":"'+a+'"}'
    var X_s = Buffer.from(x_s).toString('base64')
  console.log("XYW_"+X_s)
    return ["XYW_"+X_s,x4]
}




