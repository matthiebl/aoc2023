answers = {
    2024: {
        1:  {"p1": 3246517, "p2": 29379307},
        2:  {"p1": 383, "p2": 436},
        3:  {"p1": 166905464, "p2": 72948684},
        4:  {"p1": 2530, "p2": 1921},
        5:  {"p1": 5732, "p2": 4716},
        6:  {"p1": 5318, "p2": 1831},
        7:  {"p1": 66343330034722, "p2": 637696070419031},
        8:  {"p1": 426, "p2": 1359},
        9:  {"p1": 6288707484810, "p2": 6311837662089},
        10: {"p1": 552, "p2": 1225},
        11: {"p1": 229043, "p2": 272673043446478},
        12: {"p1": 1421958, "p2": 885394},
        13: {"p1": 25751, "p2": 108528956728655},
        14: {"p1": 222208000, "p2": 7623},
        15: {"p1": 1527563, "p2": 1521635},
        16: {"p1": 66404, "p2": 433},
        17: {"p1": "3,7,1,7,2,1,0,6,3", "p2": 37221334433268},
        18: {"p1": 314, "p2": "15,20"},
        19: {"p1": 283, "p2": 615388132411142},
        20: {"p1": 1448, "p2": 1017615},
        21: {"p1": 211930, "p2": 263492840501566},
        22: {"p1": 12664695565, "p2": 1444},
        23: {"p1": 1253, "p2": "ag,bt,cq,da,hp,hs,mi,pa,qd,qe,qi,ri,uq"},
        24: {"p1": 50411513338638, "p2": "gfv,hcm,kfs,tqm,vwr,z06,z11,z16"},
        25: {"p1": 3077, "p2": None},
    },
    2023: {
        1:  {"p1": 54940, "p2": 54208},
        2:  {"p1": 2101, "p2": 58269},
        3:  {"p1": 535078, "p2": 75312571},
        4:  {"p1": 15205, "p2": 6189740},
        5:  {"p1": 31599214, "p2": 20358599},
        6:  {"p1": 1195150, "p2": 42550411},
        7:  {"p1": 253313241, "p2": 253362743},
        8:  {"p1": 22199, "p2": 13334102464297},
        9:  {"p1": 1868368343, "p2": 1022},
    }
}


def get_answers(year: str, day: str):
    return answers.get(int(year), {}).get(int(day), None)


def answer_tester(year: str, day: str):
    """Gets the answers from the answers"""
    answers = get_answers(year, day)

    def inner(p1, p2):
        if answers is None:
            print(f"No stored answers for {year} day {day}")
            return False
        assert p1 == answers["p1"], f"Part 1: {p1} is not expected {answers["p1"]}"
        assert p2 == answers["p2"], f"Part 2: {p2} is not expected {answers["p2"]}"
        return True
    return inner
