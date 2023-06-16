from bisect import bisect


class TaxRates:
    def __init__(self, state, income):
        self.state = state
        self.income = income
        self.federal = (
            [
                "Federal",
                [20550, 83550, 178150, 340100, 431900, 647850],
                [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37],
                [2055, 9615, 30427, 69295, 98671, 174253.5],
            ],
        )
        self.states = [
            "Alabama",
            "Alaska",
            "Arizona",
            "Arkansas",
            "California",
            "Colorado",
            "Connecticut",
            "Delaware",
            "District of Columbia",
            "Florida",
            "Georgia",
            "Hawaii",
            "Idaho",
            "Illinois",
            "Indiana",
            "Iowa",
            "Kansas",
            "Kentucky",
            "Louisiana",
            "Maine",
            "Maryland",
            "Massachusetts",
            "Michigan",
            "Minnesota",
            "Mississippi",
            "Missouri",
            "Montana",
            "Nebraska",
            "Nevada",
            "New Hampshire",
            "New Jersey",
            "New Mexico",
            "New York",
            "North Carolina",
            "North Dakota",
            "Ohio",
            "Oklahoma",
            "Oregon",
            "Pennsylvania",
            "Rhode Island",
            "South Carolina",
            "South Dakota",
            "Tennessee",
            "Texas",
            "Utah",
            "Vermont",
            "Virginia",
            "Washington",
            "Wisconsin",
            "Wyoming",
        ]
        self.taxRates = [
            ["Alabama", [1000, 6000], [0.02, 0.04, 0.05], [20, 220]],
            ["Alaska", [0], [0], [0]],
            [
                "Arizona",
                [55615, 111229, 333684],
                [0.0259, 0.0334, 0.0417, 0.045],
                [1440.4285, 3297.9361, 12574.3096],
            ],
            ["Arkansas", [4300, 8500], [0.02, 0.04, 0.055], [86, 1766]],
            [
                "California",
                [18650, 44214, 69784, 96870, 122428, 625372, 750442, 1000000, 1250738],
                [0.01, 0.02, 0.04, 0.06, 0.08, 0.093, 0.103, 0.113, 0.123, 0.0133],
                [
                    186.5,
                    697.78,
                    1720.58,
                    3345.74,
                    5390.38,
                    52164.17,
                    65046.38,
                    93246.44,
                    124087.21,
                ],
            ],
            ["Colorado", [0], [0.0455], [0]],
            [
                "Connecticut",
                [20000, 100000, 200000, 400000, 500000, 1000000],
                [0.03, 0.05, 0.055, 0.06, 0.065, 0.069],
                [600, 4600, 10100, 22100, 28600, 63100],
            ],
            [
                "Delaware",
                [2000, 5000, 10000, 20000, 25000, 60000],
                [0.022, 0.039, 0.048, 0.052, 0.0555, 0.065],
                [44, 161, 401, 921, 1198.5, 3508.5],
            ],
            [
                "District of Columbia",
                [10000, 40000, 60000, 250000, 500000, 1000000],
                [0.04, 0.06, 0.065, 0.085, 0.0925, 0.0975, 0.1075],
                [400, 2200, 3500, 19650, 42775, 91525],
            ],
            ["Florida", [0], [0], [0]],
            [
                "Georgia",
                [1000, 3000, 5000, 7000, 10000],
                [0.01, 0.02, 0.03, 0.04, 0.05, 0.0575],
                [10, 50, 110, 190, 340],
            ],
            [
                "Hawaii",
                [
                    4800,
                    9600,
                    19200,
                    28800,
                    38400,
                    48000,
                    72000,
                    96000,
                    300000,
                    350000,
                    400000,
                ],
                [
                    0.014,
                    0.032,
                    0.055,
                    0.064,
                    0.068,
                    0.072,
                    0.076,
                    0.079,
                    0.0825,
                    0.09,
                    0.1,
                    0.11,
                ],
                [
                    67.2,
                    220.8,
                    748.8,
                    1363.2,
                    2016,
                    2707.2,
                    4531.2,
                    6427.2,
                    23257.2,
                    27757.2,
                    32757.2,
                ],
            ],
            [
                "Idaho",
                [3176, 9526, 15878],
                [0.01, 0.03, 0.045, 0.06],
                [31.76, 222.26, 508.1],
            ],
            ["Illinois", [0], [0.0495], [0]],
            ["Indiana", [0], [0.0323], [0]],
            [
                "Iowa",
                [1743, 3486, 6972, 15687, 26145, 34860, 52290, 78435],
                [
                    0.0033,
                    0.0067,
                    0.0225,
                    0.0414,
                    0.0563,
                    0.0596,
                    0.0625,
                    0.0744,
                    0.0853,
                ],
                [
                    5.7519,
                    17.43,
                    95.865,
                    456.666,
                    1045.4514,
                    1564.8654,
                    2654.2404,
                    4599.4284,
                ],
            ],
            ["Kansas", [30000, 60000], [0.031, 0.0525, 0.057], [930, 2505]],
            ["Kentucky", [0], [0.05], [0]],
            ["Louisiana", [25000, 100000], [0.0185, 0.035], [462.5, 3087.5]],
            ["Maine", [46000, 108900], [0.058, 0.0675, 0.0715], [2668, 6913.75]],
            [
                "Maryland",
                [1000, 2000, 3000, 150000, 175000, 225000, 300000],
                [0.02, 0.03, 0.04, 0.0475, 0.05, 0.0525, 0.055, 0.0575],
                [20, 50, 90, 7072.5, 8322.5, 10947.5, 15072.5],
            ],
            ["Massachusetts", [0], [0.05], [0]],
            ["Michigan", [0], [0.0425], [0]],
            [
                "Minnesota",
                [41050, 163060, 284810],
                [0.0535, 0.068, 0.0785, 0.0985],
                [2196.175, 10492.855, 20050.23],
            ],
            ["Mississippi", [5000, 10000], [0.04, 0.05], [200, 450]],
            [
                "Missouri",
                [108, 1088, 2176, 3264, 4352, 5440, 6528, 7616, 8704],
                [0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05, 0.054],
                [1.62, 21.22, 48.42, 81.06, 119.14, 162.66, 211.62, 266.02, 324.772],
            ],
            [
                "Montana",
                [3100, 5500, 8400, 11400, 14600, 18800],
                [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.0675],
                [31, 79, 166, 286, 446, 698],
            ],
            [
                "Nebraska",
                [6860, 41190, 66360],
                [0.0246, 0.0351, 0.0501, 0.0684],
                [168.756, 1373.739, 2634.756],
            ],
            ["Nevada", [0], [0], [0]],
            ["New Hampshire", [0], [0], [0]],
            [
                "New Jersey",
                [20000, 50000, 70000, 80000, 150000, 500000, 1000000],
                [0.014, 0.0175, 0.0245, 0.035, 0.0525, 0.0637, 0.0897, 0.1075],
                [280, 805, 1295, 1645, 5320, 27615, 72465],
            ],
            [
                "New Mexico",
                [8000, 16000, 24000, 315000],
                [0.017, 0.032, 0.047, 0.049, 0.059],
                [136, 392, 768, 15027],
            ],
            [
                "New York",
                [17150, 23600, 27900, 161550, 323200, 2155350, 5000000, 25000000],
                [0.04, 0.045, 0.0525, 0.0625, 0.0685, 0.0965, 0.103, 0.109],
                [
                    686,
                    976.25,
                    1202,
                    9020.525,
                    19123.65,
                    144625.925,
                    419134.65,
                    2479134.65,
                ],
            ],
            ["North Carolina", [0], [0.0499], [0]],
            [
                "North Dakota",
                [67700, 163550, 249150, 445000],
                [0.011, 0.0204, 0.0227, 0.0264, 0.029],
                [744.7, 2700.04, 4643.16, 9813.6],
            ],
            [
                "Ohio",
                [25000, 44250, 88450, 110650],
                [0.02765, 0.03226, 0.03688, 0.0399],
                [691.25, 1312.255, 2942.351, 3828.131],
            ],
            [
                "Oklahoma",
                [2000, 5000, 7500, 9800, 12200],
                [0.0025, 0.0075, 0.0175, 0.0275, 0.0375, 0.0475],
                [5, 27.5, 71.25, 134.5, 224.5],
            ],
            [
                "Oregon",
                [7300, 18400, 250000],
                [0.0475, 0.0675, 0.0875, 0.099],
                [346.75, 1096, 21361],
            ],
            ["Pennsylvania", [0], [0.0377], [0]],
            [
                "Rhode Island",
                [68200, 155050],
                [0.0375, 0.0475, 0.0599],
                [2557.5, 6682.875],
            ],
            [
                "South Carolina",
                [3200, 6410, 9620, 12820, 16040],
                [0, 0.03, 0.04, 0.05, 0.06, 0.07],
                [0, 96.3, 224.7, 384.7, 577.9],
            ],
            ["South Dakota", [0], [0], [0]],
            ["Tennessee", [0], [0], [0]],
            ["Texas", [0], [0], [0]],
            ["Utah", [0], [0.0495], [0]],
            [
                "Vermont",
                [68400, 165350, 251950],
                [0.035, 0.06, 0.076, 0.0875],
                [2394, 8211, 14792.6],
            ],
            [
                "Virginia",
                [3000, 5000, 17000],
                [0.02, 0.03, 0.05, 0.0575],
                [60, 120, 720],
            ],
            ["Washington", [0], [0], [0]],
            [
                "West Virginia",
                [10000, 25000, 40000, 60000],
                [0.03, 0.04, 0.045, 0.06, 0.065],
                [300, 900, 1575, 2775],
            ],
            [
                "Wisconsin",
                [17010, 34030, 374600],
                [0.0354, 0.0465, 0.053, 0.0765],
                [602.154, 1393.584, 19443.794],
            ],
            ["Wyoming", [0], [0], [0]],
        ]
        self.totalTax = self.getRate()
        self.takeHome = self.income - self.totalTax

    def getRate(self):
        if not self.state in self.states:
            if self.state == "Federal":
                taxState = self.federal[0]
                brackets = self.federal[0][1]
                rates = self.federal[0][2]
                baseTax = self.federal[0][3]
            else:
                return "Invalid State"
        else:
            taxState = self.states.index(self.state)
            brackets = self.taxRates[taxState][1]
            rates = self.taxRates[taxState][2]
            baseTax = self.taxRates[taxState][3]

        i = bisect(brackets, self.income)
        if not i:
            return 0
        rate = rates[i - 1]
        bracket = brackets[i - 1]
        incomeInBracket = self.income - bracket
        taxInBracket = incomeInBracket * rate
        totalTax = baseTax[i - 1] + taxInBracket
        return totalTax

    def printRate(self):
        print("Tax Amount: ${:,.2f}".format(self.getRate()))
        print("Take-Home Pay: ${:,.2f}".format(self.income - self.getRate()))
