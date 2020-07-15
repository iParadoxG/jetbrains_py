from math import log, ceil, floor
import sys, getopt
class lengthError(Exception):
    pass
class diffError(Exception):
    pass
class annuityError(Exception):
    pass
class creditCalculator():
    type = ""
    principal = 0
    periods = 0
    interest = 0
    payment = 0
    def __init__(self, argu):
        try:
            if len(argu)<4:
                raise lengthError
            opts, args = getopt.getopt(argu, "", ["type=", "principal=", "periods=", "interest=", "payment="])
            for opt, arg in opts:
                if opt == '--type':
                    self.type = arg
                elif opt == '--principal':
                    self.principal = int(arg)
                elif opt == '--periods':
                    self.periods = int(arg)
                elif opt == '--interest':
                    self.interest = float(arg) / 1200
                elif opt == '--payment':
                    self.payment = int(arg)
        except getopt.GetoptError:
            print('Incorrect parameters')
            sys.exit(2)
        except lengthError:
            print('Incorrect parameters')
            sys.exit(2)

        try:
            if self.type == 'diff':
                if (self.principal > 0 and self.periods > 0 and self.interest > 0 and not self.payment > 0):
                    self.calcDiff(self.principal, self.periods, self.interest)
                else:
                    raise diffError
            elif self.type == 'annuity':
                if (self.principal > 0 and self.periods > 0 and self.interest > 0):
                    self.annPay(self.principal, self.periods, self.interest)
                elif (self.payment > 0 and self.periods > 0 and self.interest > 0):
                    self.annPrin(self.payment, self.periods, self.interest)
                elif (self.principal > 0 and self.payment > 0 and self.interest > 0):
                    self.annPer(self.principal, self.payment, self.interest)
                else:
                    raise annuityError
        except diffError:
            print('Incorrect parameters')
            sys.exit(2)
        except annuityError:
            print('Incorrect parameters')
            sys.exit(2)

    def calcDiff(self, principal, periods, interest):
        diff_acc = 0
        for m in range(1,periods + 1):
            diff = ceil((principal/periods) + (interest * (principal - ((principal * (m - 1)/periods)))))
            diff_acc += diff
            print(f'Month {m}: paid out {diff}')
        print(f'\nOverpayment = {diff_acc - principal}')

    def annPer(self, principal, payment, interest):
        periods = ceil(log((payment / (payment - interest * principal)), (interest + 1)))
        if periods % 12 > 0:
            print(f'You need {periods // 12} years and {periods % 12} months to repay this credit!')
        else:
            print(f'You need {periods // 12} years to repay this credit!')
        print(f'Overpayment = {(payment * periods) - principal}')

    def annPay(self, principal, periods, interest):
        payment = ceil(principal * (interest * ((1 + interest) ** periods) / (((1 + interest) ** periods) - 1)))
        print(f'Your annuity payment = {payment}!')
        print(f'Overpayment = {(payment * periods) - principal}')

    def annPrin(self, payment, periods, interest):
        principal = floor(payment / (interest * ((1 + interest) ** periods) / (((1 + interest) ** periods) - 1)))
        print(f'Your credit principal = {principal}!')
        print(f'Overpayment = {(payment * periods) - principal}')

cc1 = creditCalculator(sys.argv[1:])
