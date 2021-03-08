from ddt import ddt,file_data
@ddt
class Addtest:
  @file_data('D:\TongMetaTest\data.yaml')
  def tt1(self,**kwargs):
     print(**kwargs['user'])


