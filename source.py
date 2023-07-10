class StudProf:
    def __init__(self,total):
        self.final=total
    def stats2(self):
        print(f'Your final score is {self.final}, if you got 40% above from all practise assignments you\'ll get extra 10 marks and for extra activity another 10.')
    def python(self,Q1,Q3,P1,P2,GA):
        Q1=int(Q1);Q3=int(Q3);P1=int(P1);P2=int(P2);GA=int(GA)
        T=0.1*GA+0.1*Q1+max(0.5*Q3+0.2*max(P1,P2),0.4*Q3+0.3*max(P1,P2)+0.1*min(P1,P2))
        print(f'Your final score is {T}, if you got 40% above from all practise assignments and ppas you\'ll get extra 10 marks.')
    def other(self):
        print(f'Your final score is {self.final}, if you got 40% above from all practise assignments you\'ll get extra 10 marks.')
courses=[['0 CT','1 Math1','2 Stats1','3 English1'],['0 Python','1 Math2','2 Stats2', '3 English2']]
class SubCal:
    def __init__(self,q1,q2,q3,ga):
        self.q1=int(q1)
        self.q2=int(q2)
        self.q3=int(q3)
        self.ga=int(ga)
    def meth1(self):
        return int(self.q1*0.2+self.q2*0.3+self.q3*0.4+self.ga*0.1)
    def meth2(self):
        return int(max(self.q1,self.q2)*0.2+self.q3*0.6+self.ga*0.1)

# Urj_Stats=SubCal(24,70,65,100)
# meth1=Urj_Stats.meth1()
# meth2=Urj_Stats.meth2()
# print(meth1+10,meth2+10)
        
