# 需求：要一个类中的方法在不同的版本继承不同的父类，并且重写父类中的方法，
# 现要求在两个版本都可以使用


# 父类1方法validate_policy_for_port参数有3个
class ParentClass1(object):
    def __init__(self):
        pass

    def validate_policy_for_port(self, policy, port):
        print('ParentClass1 validate_policy_for_port...')


# 父类2方法validate_policy_for_port参数有4个
class ParentClass2(object):
    def __init__(self):
        pass

    def validate_policy_for_port(self, context, policy, port):
        print('ParentClass2 validate_policy_for_port...')


# 一个版本中子类1继承自父类1，并重写validate_policy_for_port方法
class SonClass1(ParentClass1):
    # def validate_policy_for_port(self, policy, port):
    #     print('extends the parentClass1 in SonClass1')
    def validate_policy_for_port(self, context=None, policy=None, port=None):
        print('SonClass1, context==%s, policy==%s, port==%s' % (context,
                                                                policy, port))


# 一个版本中，子类2继承自父类2，并重写validate_policy_for_port方法
class SonClass2(ParentClass2):
    def validate_policy_for_port(self, context=None, policy=None, port=None):
        print('SonClass2, context==%s, policy==%s, port==%s' % (context,
                                                                policy, port))


son1 = SonClass1()
son1.validate_policy_for_port(policy='22', port='port')
# SonClass1, context==None, policy==22, port==port

son2 = SonClass2()
son2.validate_policy_for_port(context='context', policy=23, port='port')
# SonClass2, context==context, policy==23, port==port
# 可以使用这种方法，但是调用时必须要使用关键字参数作为入参，不满足需求
