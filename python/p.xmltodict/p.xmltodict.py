#! -*- coding: utf-8 -*-

import json
import xmltodict

citydict = "FinanceData.xml"

class Account(object):
    """docstring for Account"""
    def __init__(self, account):
        super(Account, self).__init__()
        self.account   = account
        self.aid       = account[u'电子数据编号'].encode('utf-8')
        self.aname     = account[u'电子数据名称'].encode('utf-8')
        self.ayear     = account[u'年度'].encode('utf-8')
        self.adb       = account[u'所在数据库'].encode('utf-8')
        self.atcode    = account[u'行业编码'].encode('utf-8')
        self.atname    = account[u'行业名称'].encode('utf-8')
        self.adesc     = ''
        self.aunitname = account[u'单位名称'].encode('utf-8')
        self.aselect   = account[u'选择'].encode('utf-8')

    def print_account(self):
        for (k, v) in self.account.items():
            print "%s -->" % k.encode('utf-8'), v.encode('utf-8') if isinstance(v, unicode) else ''

    

# print data[u'NewDataSet'][u'Finance']
data = json.loads(json.dumps(xmltodict.parse(open(citydict, 'r').read()), skipkeys=True))
accounts = [] 
for account in data[u'NewDataSet'][u'Finance']:
    accounts.append(Account(account))

for account in accounts:
    account.print_finance()
    print