class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        tmp = [1]                       #從1開始
        count = 0
        CSL = []
        n -= 1
        
        while( n > 0):
            f = tmp[0]                  #最前面的數字 比較用
            for i in range(len(tmp)):   
                if f == tmp[i]:         #如果下一個數字跟比較用的數字一樣
                    count += 1          #則個數+1
                else:
                    CSL.append(count)   #如果不一樣 就將個數存起來
                    CSL.append(f)       #並把這是哪個數字存起來
                    f = tmp[i]          #將比較用的數字改成目前的數字
                    count = 1           #並將個數+1
                if i == len(tmp) - 1:   #如果已經是最後一個數字了
                    CSL.append(count)   #就將個數根數字存起來
                    CSL.append(tmp[i])
                    count = 0           #並將個數還原為0
            tmp = CSL                   #替換掉上一個數字
            CSL = []                    #將暫時儲存的空間清空
            n -= 1
            
        ans = str(''.join(map(str, tmp)))#轉換答案格式
        return ans