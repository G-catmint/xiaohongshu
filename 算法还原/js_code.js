var CrytoJS = require('crypto-js')
const getPayload = require('./enc3des')



function MD5Test(text){
    return CrytoJS.MD5(text).toString()
}


function get_x_s(url,data,cookie,time) {
    astr = "url="+url+JSON.stringify(data)
    console.log(astr)
    var x1 = MD5Test(astr) //d对url和参数进行标准md5加密
        ,x2 = '0|0|0|1|0|0|1|0|0|0|1|0|0|0|0'
        ,x3 = cookie
        ,x4 = time
        ,source = 'x1='+x1+';x2='+x2+';x3='+x3+';x4='+x4+';'
        console.log(source)
        ,b = new Buffer(source).toString('base64')
        ,a = getPayload.encrypt(b)
    x_s = '{"signSvn":"51","signType":"x1","appId":"xhs-pc-web","signVersion":"1","payload":"'+a+'"}'
    var X_s = Buffer.from(x_s).toString('base64')
    return X_s
}

function main() {
    var url = '/api/sns/web/v1/homefeed'
    ,data= {"cursor_score":"","num":18,"refresh_type":1,"note_index":0,"unread_begin_note_id":"","unread_end_note_id":"","unread_note_count":0,"category":"homefeed_recommend","search_key":"","need_num":8,"image_formats":["jpg","webp","avif"],"need_filter_image":false}
    ,cookie_a1 = "18ee63a8bd9ogfei3h31hl8op3kuwtbcsdk4ypm2750000537725"
    return get_x_s(url, data, cookie_a1);
}

console.log(main());

