import requests, json, xlrd, xlwt, re, time


def search(testid):
    print(38470000+testid)
    num = 4444000020022890126 + testid
    response = session.get('http://www.zhixue.com/zhixuebao/zhixuebao/personal/studentPkData/?'
                           'examId=%s&pkId=%d' % (examid, num), verify=False)
    html = response.text
    students = json.loads(html)
    student = students[1]
    grades = student['subjectList']
    userid = student['userId']
    print("userId",userid)
    for grade in grades:
        score = grade['score']
        subjectID = code[grade['subjectName']]
        yield score, subjectID


code = {
    "语文": 1,
    "数学": 2,
    "英语": 3,
    "物理": 4,
    "化学": 5,
    "生物": 6,
    "历史": 7,
    "政治": 8,
    "地理": 9,
    "总分": 10,
}
fp = open('user.txt')
loginName = fp.readline()
loginId = int(loginName[:-1]) + 4444000019984420126
password = fp.readline()
fp.close()
fp = open('examid.txt')
examid = fp.readline()
fp.close()
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
data1 = {
    'loginName': loginName[:-1],
    'password': password,
    'code': '',
}
session = requests.Session()
session.post('http://www.zhixue.com/weakPwdLogin/?from=web_login', headers=headers, data=data1)
data2 = {
    'service': 'http://www.zhixue.com:80/ssoservice.jsp',
    'callback': 'jQuery191014993402568720549_1525350577230',
    '_': '1525350577231',
}
r = session.get('http://sso.zhixue.com/sso_alpha//login', params=data2, headers=headers)
lt = re.search('"lt" : "(.*?)"',r.text).group(1)
execution = re.search('"execution" : "(.*?)"',r.text).group(1)
data3 = {
    'service': 'http://www.zhixue.com:80/ssoservice.jsp',
    'callback': 'jQuery191014993402568720549_1525350577230',
    'username': loginId,
    'password': password,
    'sourceappname': 'tkyh,tkyh',
    'key': 'id',
    '_eventId': 'submit',
    'lt': lt,
    'execution': execution,
}
r = session.get('http://sso.zhixue.com/sso_alpha//login', params=data3, headers=headers)
st = re.search('"st": "(.*?)"',r.text).group(1)
data4 = {
    'action':'login',
    'username':loginId,
    'password':password,
    'ticket':st,
}
r = session.post('http://www.zhixue.com/ssoservice.jsp', headers=headers, data=data4)
print(session.cookies)

time.sleep(10)

studentsWorkbook = xlrd.open_workbook('students.xls')
studentsSheet = studentsWorkbook.sheet_by_index(0)
newWorkbook = xlwt.Workbook()
newSheet = newWorkbook.add_sheet('Sheet')
newSheet.write(0, 0, "姓名")
newSheet.write(0, 1, "语文")
newSheet.write(0, 2, "数学")
newSheet.write(0, 3, "英语")
newSheet.write(0, 4, "物理")
newSheet.write(0, 5, "化学")
newSheet.write(0, 6, "生物")
newSheet.write(0, 7, "历史")
newSheet.write(0, 8, "政治")
newSheet.write(0, 9, "地理")
newSheet.write(0, 10, '总分')
for i in range(50):
    number = int(studentsSheet.cell(i,0).value)
    name = studentsSheet.cell(i,1).value
    try:
        newSheet.write(i+1, 0, name)
        for grade2, ID in search(number):
            newSheet.write(i+1, ID, grade2)
    except:
        print(name, "fail!")
newWorkbook.save('grades.xls')
