# -*- coding:utf-8 -*-
import random
import time
Weighted = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
check_code = {0:'1',1:'0',2:'X',3:'9',4:'8',5:'7',6:'6',7:'5',8:'4',9:'3',10:'2'}
# now_date = time.time()
# print(now_date)
# 日期
# 18位身份
head = random.choice(['11','12','13','14','15','21','22','23','31','32','33','34','35','36','37',
               '41','42','43','44','45','46','50','51','52','53','54','61','62','63','64','65',
               '71','81','82'])
y = ''.join(random.sample('0123456789',8))
m = str(random.randint(1,12))
m = m.zfill(2)
d = str(random.randint(1,31))
d = d.zfill(2)
end = ''.join(random.sample('0123456789',3))
index = 0
sum = 0
for i in (head+y+m+d+end):
	sum += (int(i)*Weighted[index])
	index += 1
the_end = check_code[sum%11]
print(head,y,m,d,end,the_end)
print(head+y+m+d+end+the_end)
