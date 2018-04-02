import requests,json

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
response = requests.get('http://www.zhixue.com/zhixuebao/zhixuebao/feesReport/getStuSingleReportDataForPK/?'
                        'examId=%s' % examid,headers=headers)
html = response.text
grades = json.loads(html)
singleDatas = grades['singleData']
for singleData in singleDatas:
    print(singleData['subjectName'])
    print("得分",singleData['score'])
    print("班级平均分", singleData['classRank']['avgScore'])
    print("班级最高分", singleData['classRank']['highScore'])
    print("班级排名", singleData['classRank']['rank'])
    print("年级平均分", singleData['gradeRank']['avgScore'])
    print("年级最高分", singleData['gradeRank']['highScore'])
    print()