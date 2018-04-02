import requests,json,xlrd,xlwt


def search(testid):
    print(38470000+testid)
    num = 4444000020022890126 + testid
    response = requests.get('http://www.zhixue.com/zhixuebao/zhixuebao/personal/studentPkData/?'
                            'examId=%s&pkId=%d' % (examid,num), headers=headers)
    html = response.text
    students = json.loads(html)
    student = students[1]
    grades = student['subjectList']
    userid = student['userId']
    print("userId",userid)
    for grade in grades:
        score = grade['score']
        subjectID = code[grade['subjectName']]
        yield score,subjectID


code = {
    "语文":1,
    "数学":2,
    "英语":3,
    "物理":4,
    "化学":5,
    "生物":6,
    "历史":7,
    "政治":8,
    "地理":9,
    "总分":10,
}
fp = open('cookie.txt')
cookie = fp.readline()
fp.close()
fp = open('examid.txt')
examid = fp.readline()
fp.close()
headers = {
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                     "Chrome/65.0.3325.146 Safari/537.36",
        'Cookie':cookie
}
studentsWorkbook = xlrd.open_workbook('students.xls')
studentsSheet = studentsWorkbook.sheet_by_index(0)
newWorkbook = xlwt.Workbook()
newSheet = newWorkbook.add_sheet('Sheet')
newSheet.write(0,0,"姓名")
newSheet.write(0,1,"语文")
newSheet.write(0,2,"数学")
newSheet.write(0,3,"英语")
newSheet.write(0,4,"物理")
newSheet.write(0,5,"化学")
newSheet.write(0,6,"生物")
newSheet.write(0,7,"历史")
newSheet.write(0,8,"政治")
newSheet.write(0,9,"地理")
newSheet.write(0,10,'总分')
for i in range(50):
    number = int(studentsSheet.cell(i,0).value)
    name = studentsSheet.cell(i,1).value
    try:
        newSheet.write(i+1, 0, name)
        for grade,ID in search(number):
            newSheet.write(i+1,ID,grade)
    except:
        print(name,"fail!")
newWorkbook.save('grades.xls')