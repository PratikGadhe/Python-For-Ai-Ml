class Account :
    def __init__(self,Acct_num,Acct_pass):
        self.acct_num=Acct_num
        self.__acc_pass=Acct_pass #this becomes private

    def reset_pass(self):
        return self.__acc_pass

acc1=Account(123445,"pvg")
print(acc1.acct_num)
print(acc1.reset_pass())
