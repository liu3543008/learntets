import requests,re,json
from pylib.sm3_suanfa import *
def get_soat(username,password):
    url="http://10.10.64.47/auth/aaa/oauth/salt"
    hard={
        "Authorization":"Bearer mF_9.B5f-4.1JqM"
    }
    body={
        "username":"admin"
    }
    respond=requests.post(url=url,headers=hard,data=body)
    salt_list=respond.json()
    static_salt=salt_list['static_salt']
    dynamic_salt=salt_list['dynamic_salt']
    password=password
    x = Hash_sm3(('%s%s') % (password, static_salt))
    x = x.upper()
    y = Hash_sm3(('%s%s' % (x, dynamic_salt)))
    y = y.upper()
    url2='http://10.10.64.47/auth/aaa/oauth/token'
    header2={
        'Authorization':'Bearer mF_9.B5f-4.1JqM',

    }
    body2={
        'username':username,
        'password':y,
        'grant_type':'password'
    }
    respond2=requests.post(url=url2,headers=header2,data=body2)
    token_tong=respond2.json()['access_token']
    print(token_tong)
    return token_tong
def ew():
     if ' '==' ':
       print('==')


def getsms():
    header={

    }
def cook4():
    url="https://ing.cnblogs.com/ajax/ing/Publish"
    headers ={
        "content - type": "application / x - www - form - urlencoded",
        "user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "cookis":"_ga=GA1.2.1986254754.1602144476; __gads=ID=2c5625e01f5948e6:T=1602144523:S=ALNI_MaGofR2OkEm4h0IsREFR08x0wlPQA; _gid=GA1.2.934291146.1610849658; __guid=46247039.3257079674934202000.1610851422303.7139; .Cnblogs.AspNetCore.Cookies=CfDJ8EklyHYHyB5Oj4onWtxTnxZeAQ7A-EIV60WDsYqqFTm__87ahlplQiL8G6EZxwYSMpNYDhcr9ql1TLBba1f2dR1teqRvDjoJAuaPzPZX-H0QovBG9xWWduu1OYFeYk1AK-n9gSPlIUjaD4YhvTRYkyRFEJIqNSOM0dnH8sTB4VyJbF_maXYf619JhCLMsjEYFolLtjMMIVpB5AegL1rlbEYMz309d_JQMBU3Wq4lOsALVWQD7K2gFNsKeeVLk5UW-qBugYScQ62z6K3r4E1w3ioZ2L09tZFovuh9ZrxFQBEv_C-tYFG8scDILLEYxGPe2Bn8tEn6qfrVWiZXN9B4VZYIntKKDti_ngGfhfXV31lB3ICgLJdQ35RJlBm0sMPpnNOLf3UPPOWKpHaEbLdhgjFUn-EN3XH2UJC80NsT8V5o84GURUDUTaj4f6flcJeK1Xgjn8AmPtYN5W5Qm32CCbdOXJiIbhbcPn-OBpIj2u_kwzIud-h_jm1045sgEMpE9no4i9Z-pGHUvTbQ3iwEHE81CmboysloUoUGoLthO0rnsoDwCCvPlrpzTSM4U0HiKg; .CNBlogsCookie=1F3E3E814D8BCB23EE70713859C99C8078E898095B1118A5CA00174EB8E9E00AE65AC7CDD240B890988CE561264E9602E8B6CC4B717EED74F51BB34A258F0A833EB9B32CB35DD74A2ECDD2268CAA0C4D115C1E9E; monitor_count=5"
    }
    data={
        "content": "assadsddsad",
        "publicFlag" :"0"
    }
    cook={

        ".CNBlogsCookie":"49DB25091E07FA0742FEA9A2319D07F67793D95CB8D656FF40D9A9F2CCCECA52FE9E1146DF4D99AA607E8697BE6A4A9EC25D15688E9EA91E626D59EB9F1D5A032F3D7266D2B3D88482E666A5023A57BC33610DBC",
        ".Cnblogs.AspNetCore.Cookies":"CfDJ8EklyHYHyB5Oj4onWtxTnxYziknp2nit23L34J4dWDTLwYuU9hdnZquDItWSKbEx0mhv85iE3gvf9oxRovHtVvhO0NhC62ZLARVFh7n_oX5cOCJ5uewtdqF93Wet63n0Hgj_gFP8Nl4YbQ"
    }


    respond=requests.post(url=url,headers=headers,data=data)
    print(respond.json())


if __name__=="__main__":
    get_soat("admin","123456")



