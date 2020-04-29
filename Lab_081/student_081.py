from collections import namedtuple

Module = namedtuple('Module', 'code title ects')

CA1_MODULES = {'CA103': Module('CA103', 'Computer Systems', 5),
               'CA106': Module('CA106', 'Web Design', 5),
               'CA115': Module('CA115', 'Digital Innovation', 5),
               'CA116': Module('CA116', 'Computer Programming I', 10),
               'CA117': Module('CA117', 'Computer Programming II', 10),
               'CA169': Module('CA169', 'Networks and Internet', 5),
               'CA170': Module('CA170', 'Operating Systems', 5),
               'CA172': Module('CA172', 'Problem Solving', 5),
               'MS121': Module('MS121', 'IT Mathematics', 10)}

class Student(object):

    def __init__(self, idnum, surname, firstname):
        self.idnum = idnum
        self.surname = surname
        self.firstname = firstname
        self.mods = CA1_MODULES
        self.marks = {code: 0 for code in self.mods.keys()}

    def __str__(self):
        name = '{} : {} {}'.format(self.idnum,
                                   self.firstname,
                                   self.surname)
        uline = '-' * len(name)
        results = '\n'.join([code + ' : ' + self.mods[code].title + ' : ' + str(self.marks[code]) for code in sorted(self.mods.keys())])

        pm = 'Precision mark: {:.2f}'.format(self.precision_mark())
        if self.passed():
            outcome = 'Pass'
        elif self.passed_by_compensation():
            outcome = 'Pass by compensation'
        else:
            outcome = 'Fail'
        return '\n'.join([name, uline, results, pm, outcome])

    def add_mark(self, module, mark):
        self.marks[module] = mark

    def precision_mark(self):
        total = 0
        total1 = 0
        for mark in self.marks:
            if mark == "CA116" or mark == "CA117" or mark == "MS121":
                total += self.marks[mark] * 2
                total1 += 1
            else:
                total += self.marks[mark]
        self.precisionmark = total / (len(self.marks) + total1)
        return self.precisionmark

    def passed(self):
        for mark in self.marks:
            if self.marks[mark] < 40:
                return False
        return True

    def passed_by_compensation(self):
        for grade in self.marks:
            if self.marks[grade] < 35:
                return False
            else:
                total = 0
                for mark in self.marks:
                    if self.marks[mark] < 40:
                        if mark == "CA116" or mark == "CA117" or mark == "MS121":
                            total += 10
                        else:
                            total += 5
                    if 10 < total:
                        return False
        return True
