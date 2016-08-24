import pymongo

client = pymongo.MongoClient('localhost',27017)
walden = client['walden']
sheet_line = walden['sheet_line']


#path = 'walden.txt'
#with open(path,'r') as f:
#    lines = f.readlines()
#    for index,line  in enumerate(lines):
#        data ={
#            'index' : index,
#            'line': line,
#            'words': len(line.split())
#        }
#        sheet_line.insert_one(data)
#        print('ok')
#$lt/$lte/$gt/$gte/$ne 等价于</<=/>/>=/!=  l 的意思是less，g的意思是greater

for item in sheet_line.find({'words':{'$lt':5}}):
    print(item)