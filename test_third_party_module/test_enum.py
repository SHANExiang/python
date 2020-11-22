from enum import Enum, IntEnum


class Country(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672


class Country2(IntEnum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672


if __name__ == "__main__":
    # print('Member name:', Country.Albania.name)
    # print("Member value:", Country.Albania.value)
    # Member name: Albania
    # Member value: 355

    # for data in Country:
    #     print("{:15} = {}".format(data.name, data.value))
    # output:
    # Afghanistan = 93
    # Albania = 355
    # Algeria = 213
    # Andorra = 376
    # Angola = 244
    # Antarctica = 672

    country_list = list(map(int, Country2))
    # print(country_list)
    # [93, 355, 213, 376, 244, 672]


