from time import sleep
from requests import session # pip install requests
from random import choices
from string import ascii_letters

def generator_mail(length=8):
    return ''.join(choices(ascii_letters,k=length)) + '@hunght1890.com'

def get_mail(email):
    url = f'http://hunght1890.com/{email}'
    try:
        ss = session()
        response = ss.get(url)
        if response.ok:
            mail_moi_nhat = response.json()[0]
            subject = mail_moi_nhat.get('subject')
            body  = mail_moi_nhat.get('body')
            return True , (subject, body)
        else:
            return False , 'KHÔNG CÓ THƯ'
    except Exception as e:
        return False , str(e)

if __name__ == '__main__':
    email = generator_mail(16)
    print(f'Đã lấy được mail random là: {email}')
    for i in range(60):
        status , message = get_mail(email)
        if status:
            subject , body = message
            try:
                code = (body.split('To verify your email address use this security code: ')[1].split('\n')[0])
                print(f'ĐÃ LẤY ĐC CODE: {code}')
                break
            except:
                print('Không tìm thấy mã xác thực')
        else:
            print(message)
        sleep(1)


# cộng đồng auto c# kteam