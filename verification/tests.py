"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""

LETTERS_1 = [
    list('ABCD'),
    list('EFGH'),
    list('IJKL')
]

LETTERS_2 = [
    list('GFEE'),
    list('LABA'),
    list('FDRW')
]


TESTS = {
    "Basics": [
        {
            "input": [LETTERS_1, 'BAEF'],
            "answer": True
        },
        {
            "input": [LETTERS_1, 'ABCDE'],
            "answer": False
        },
        {
            "input": [LETTERS_1, 'A'],
            "answer": True
        },
        {
            "input": [LETTERS_2, 'BEE'],
            "answer": True
        },
        {
            "input": [LETTERS_2, 'ABBA'],
            "answer": False
        }
    ],
    "Extra": [
        {
            "input": [LETTERS_1, 'W'],
            "answer": False
        },
        {
            "input": [LETTERS_2, 'GLF'],
            "answer": True
        },
    ]
}
