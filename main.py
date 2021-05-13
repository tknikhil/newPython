class SumOfTwoIndicesTarget(object):

  def twoSum(self,num,target):
    required={}
    for i in range(len(num)):
      if target-num[i]  in required:
        return [required[target-num[i]],i]
      else:
        required[num[i]]=i

#Given value 
arr = [1,2,3,6,7,9]
target=SumOfTwoIndicesTarget()
print(target.twoSum(arr,11))

import h