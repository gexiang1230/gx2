#coding:utf-8
#12.29   http://docs.xlwings.org/en/stable/syntax_overview.html
import xlwings as xw
class SimImport(object,simPath):
    def downInfo(self):
      self.wb = xw.Book(simPath)

      self.sht=self.wb.sheets['Sheet1']

      self.sht.range('A3').value='FOO'
if __name__=='__main__':
    s=SimImport()
    s.downInfo()


# r'C:\Excel\a.xlsx'