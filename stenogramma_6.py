# def print_human_name(human):
#     print(human['name'])
#
#
# h1 = {'name': 'Max'}
# h2 = {'name': 'Andrey'}
# h3 = {'full_name': 'Petr'}
# print_human_name(h3)


class Phone:
    def __init__(self, phone_model):
        self._phone_model = phone_model
        self._loading()
        self._serial_number = 54879223

    def call(self):
        print('calling...')

    def _loading(self):
        print(self._phone_model, 'loading...')

    def get_serial_number(self):
        return self._serial_number

    def get_model(self):
        return self._phone_model

# my_phone_1 = Phone('nokia8800')  # создал my_phone_1, экземпляр класса Phone с атрибутами
# my_phone_2 = Phone('nokia1100')  # из конструктора __init__
# print(my_phone_1.phone_model)
# my_phone_1.call()
# print(my_phone_2.phone_model)
# my_phone_2.call()
# print(my_phone_2.get_serial_number())
# print(my_phone_2.get_model())


class SmartPhone(Phone):
    def sms(self):
        print('sms sending')

    def email(self):
        print('email sending')


class IPhone(SmartPhone):
    def __init__(self, phone_model):
        super().__init__(phone_model)
        print('logo is showing')

    def sms(self):
        print('Imessage sending')

    def player(self):
        print('playing')

    def browser(self):
        print('opening is browser')


# iphone_1 = IPhone('iphone 1')
# iphone_1.sms()


class NextGenerationSmartPhone(IPhone):
    def touch_id(self):
        print('touch id is working')

    def pay(self):
        print('pay is working')


class Samsung(NextGenerationSmartPhone):
    def call(self):
        print('звонит по самсунговски')


class Huawei(NextGenerationSmartPhone):
    def call(self):
        print('звонит по хуавеевски')


samsung = Samsung('S10')
huawei = Huawei('P30PRO')


def my_call(phone):
    phone.call()


my_call(samsung)
my_call(huawei)
