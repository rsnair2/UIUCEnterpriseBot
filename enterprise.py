__author__ = 'rsnair2'

import requests
from HTMLParser import HTMLParser


class UIUCEnterpriseWebBot:

    session = None
    term = None

    def __init__(self):
        pass

    def set_term(self, term):
        self.term = term

    def login(self, username, password):
        """
        uiuc login - initializes a session object that is logged into the UIUC
        self service website for the specified user. note: there is no error
        checking so if the username/password is invalid or if the website has
        changed, the system will still return an session object, but one that
        won't work correctly.

        :param username: username to login as
        :param password: password for user
        """
        s = requests.Session()
        s.headers = dict()
        s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:22.0) Gecko/20100101 Firefox/22.0'
        s.headers['Accept-Language'] = 'en-US,en;q=0.5'
        s.headers['Accept-Encoding'] = 'gzip, deflate'
        s.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        s.headers['Connection'] = 'keep-alive'

        url = """https://eas.admin.uillinois.edu/eas/servlet/EasLogin?redirect=https://webprod.admin.uillinois.edu/ssa/servlet/SelfServiceLogin?appName=edu.uillinois.aits.SelfServiceLogin&dad=BANPROD1"""
        payload = {}

        r = s.get(url=url, data=payload)

        url = """https://eas.admin.uillinois.edu/eas/servlet/login.do"""
        payload = {u'password': password, u'inputEnterpriseId': username, u'queryString': u'', u'BTN_LOGIN': u'Login'}

        r = s.post(url=url, data=payload)

        url = """https://ui2web1.apps.uillinois.edu/BANPROD1/twbkwbis.P_GenMenu?name=bmenu.P_StuMainMnu"""
        payload = {}

        r = s.get(url=url, data=payload)

        self.session = s

    def get_classes(self, major, course):
        """
        UIUC get classes - gets a list of all classes (identified by CRN -
        course registration number) for the specified major and course.

        :param s: a session object that is logged into the uiuc self-service
        website
        :param major: the abbreviated major/department name for the class
        (ex. ECE)
        :param course: the course name and number (ex. ECE 391)
        :param term_in: the semester in 1yearX, where X = 1 for spring, 8 for
        fall

        :return: a dictionary where key is the CRN of every class found and
        value is a bool indicating whether or not the class is available
        """
        if not self.session:
            return None

        t = self._get_classes_page(major, course, self.term)
        r = t['r']
        p = self._UiucClassesParser()
        p.feed(r.content)
        d = {}

        if len(p.list_avail) != len(p.list_crn):
            return None

        for i in range(0, len(p.list_avail)):
            d[p.list_crn[i]] = p.list_avail[i]

        return d

    def get_majors(self):
        d = self._get_majors_page(term_in=self.term)
        r = d['r']
        p = self._UiucMajorsParser()
        p.feed(r.content)
        return { 's' : p.majors_short, 'l' : p.majors }

    def get_courses(self, major):
        t = self._get_courses_page(major, self.term)
        r = t['r']
        p = self._UiucCoursesParser()
        p.feed(r.content)
        return { 'd': p.descriptions, 'n': p.courses }

    def _get_classes_page(self, major, course, term_in):
        s = self.session

        if not s:
            return None

        url = """https://ui2web1.apps.uillinois.edu/BANPROD1/twbkwbis.P_GenMenu?name=bmenu.P_RegMnu"""
        payload = {}

        r = s.get(url=url, data=payload)

        url = """https://ui2web1.apps.uillinois.edu/BANPROD1/twbkwbis.P_GenMenu?name=bmenu.P_RegAgreementLook"""
        payload = {}

        r = s.get(url=url, data=payload)

        url = """https://ui2web1.apps.uillinois.edu/BANPROD1/bwskfcls.p_sel_crse_search"""
        payload = {}

        r = s.get(url=url, data=payload)

        url = """https://ui2web1.apps.uillinois.edu/BANPROD1/bwckgens.p_proc_term_date"""
        payload = {u'p_term': term_in,
                   u'p_calling_proc': u'P_CrseSearch'}

        r = s.post(url=url, data=payload)

        url = """https://ui2web1.apps.uillinois.edu/BANPROD1/bwskfcls.P_GetCrse"""
        payload = {u'sel_instr': [u'dummy'],
                   u'sel_camp': [u'dummy', u'dummy'],
                   u'begin_ap': [u'x'],
                   u'sel_from_cred': [u''],
                   u'sel_sess': [u'dummy'],
                   u'sel_title': [u''],
                   u'sel_insm': [u'dummy'],
                   u'sel_attr': [u'dummy'],
                   u'sel_subj': [u'dummy', major],
                   u'term_in': [term_in],
                   u'sel_to_cred': [u''],
                   u'rsts': [u'dummy'],
                   u'end_ap': [u'y'],
                   u'sel_schd': [u'dummy'],
                   u'sel_crse': [u''],
                   u'begin_mi': [u'0'],
                   u'begin_hh': [u'0'],
                   u'SUB_BTN': [u'Course Search '],
                   u'end_mi': [u'0'], u'path': [u'1'],
                   u'sel_levl': [u'dummy'],
                   u'crn': [u'dummy'],
                   u'end_hh': [u'0'],
                   u'sel_day': [u'dummy'],
                   u'sel_ptrm': [u'dummy', u'%']}

        r = s.post(url=url, data=payload)

        url = """https://ui2web1.apps.uillinois.edu/BANPROD1/bwskfcls.P_GetCrse"""
        payload = {u'SEL_LEVL': [u'dummy', u'%'],
                   u'SEL_TITLE': [u''],
                   u'END_HH': [u'0'],
                   u'sel_subj': [u'dummy', major],
                   u'BEGIN_HH': [u'0'],
                   u'term_in': [term_in],
                   u'SEL_CAMP': [u'dummy'],
                   u'rsts': [u'dummy'],
                   u'END_MI': [u'0'],
                   u'SEL_DAY': [u'dummy'],
                   u'SEL_INSTR': [u'dummy', u'%'],
                   u'END_AP': [u'a'],
                   u'SEL_SCHD': [u'dummy'],
                   u'SUB_BTN': [u'View Sections'],
                   u'SEL_CRSE': [course],
                   u'BEGIN_MI': [u'0'],
                   u'path': [u'1'],
                   u'SEL_PTRM': [u'dummy'],
                   u'SEL_INSM': [u'dummy'],
                   u'BEGIN_AP': [u'a'],
                   u'call_value_in': [u''],
                   u'sel_dunt_unit': [u''],
                   u'SEL_SESS': [u'dummy'],
                   u'SEL_ATTR': [u'dummy', u'%'],
                   u'sel_dunt_code': [u''],
                   u'crn': [u'dummy']}

        r = s.post(url=url, data=payload)

        return {'s': s, 'r': r}

    class _UiucClassesParser(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)
            self.found_table = False
            self.found_td = False
            self.found_tr = False
            self.found_a = False

            self.list_crn = []
            self.list_avail = []

        def handle_starttag(self, tag, attr):
            if tag == 'table':
                for a in attr:
                    if a[0] == 'class' and a[1] == 'datadisplaytable':
                        self.found_table = True

            if self.found_table and tag == 'tr':
                self.found_tr = True

            if self.found_table and tag == 'td':
                for a in attr:
                    if a[0] == 'class' and a[1] == 'dddefault':
                        self.found_td = True

            if self.found_table and self.found_tr and self.found_td:
                if tag == 'abbr':
                    self.list_avail.append(False)
                    self.found_tr = False
                elif tag == 'input':
                    self.list_avail.append(True)
                    self.found_tr = False

            if self.found_table and self.found_td and tag == 'a':
                self.found_a = True

        def handle_data(self, data):
            if self.found_a:
                self.list_crn.append(data.strip('\n'))
                self.found_a = False

        def handle_endtag(self, tag):
            if tag == 'table':
                self.found_table = False
            if self.found_table and tag == 'td':
                self.found_td = False

    def _get_majors_page(self, term_in):
        s = self.session

        url = """https://ui2web1.apps.uillinois.edu/BANPROD1/twbkwbis.P_GenMenu?name=bmenu.P_RegMnu"""
        payload = {}

        r = s.get(url=url, data=payload)

        url = """https://ui2web1.apps.uillinois.edu/BANPROD1/twbkwbis.P_GenMenu?name=bmenu.P_RegAgreementLook"""
        payload = {}

        r = s.get(url=url, data=payload)

        url = """https://ui2web1.apps.uillinois.edu/BANPROD1/bwskfcls.p_sel_crse_search"""
        payload = {}

        r = s.get(url=url, data=payload)

        url = """https://ui2web1.apps.uillinois.edu/BANPROD1/bwckgens.p_proc_term_date"""
        payload = {u'p_term': term_in, u'p_calling_proc': u'P_CrseSearch'}

        r = s.post(url=url, data=payload)

        return {'s': s, 'r': r}

    class _UiucMajorsParser(HTMLParser):
        print_data = False
        lock_data = False
        majors = []
        majors_short = []

        def handle_starttag(self, tag, attr):
                if tag == 'option':
                        self.print_data = True;
                        if not self.lock_data:
                                self.majors_short.append(attr[0][1])

        def handle_data(self, data):
            if self.print_data and not self.lock_data:
                    self.majors.append(data.rstrip('\n'))
                    self.print_data = False

                    if data.find('Zulu') != -1:
                            self.lock_data = True

    def _get_courses_page(self, major, term_in):
        s = self.session

        url = """https://ui2web1.apps.uillinois.edu/BANPROD1/twbkwbis.P_GenMenu?name=bmenu.P_RegMnu"""
        payload = {}

        r = s.get(url=url, data=payload)

        url = """https://ui2web1.apps.uillinois.edu/BANPROD1/twbkwbis.P_GenMenu?name=bmenu.P_RegAgreementLook"""
        payload = {}

        r = s.get(url=url, data=payload)

        url = """https://ui2web1.apps.uillinois.edu/BANPROD1/bwskfcls.p_sel_crse_search"""
        payload = {}

        r = s.get(url=url, data=payload)

        url = """https://ui2web1.apps.uillinois.edu/BANPROD1/bwckgens.p_proc_term_date"""
        payload = {u'p_term': term_in, u'p_calling_proc': u'P_CrseSearch'}

        r = s.post(url=url, data=payload)

        url = """https://ui2web1.apps.uillinois.edu/BANPROD1/bwskfcls.P_GetCrse"""
        payload = {u'sel_instr': [u'dummy'], u'sel_camp': [u'dummy', u'dummy'], u'begin_ap': [u'x'], u'sel_from_cred': [u''], u'sel_sess': [u'dummy'], u'sel_title': [u''], u'sel_insm': [u'dummy'], u'sel_attr': [u'dummy'], u'sel_subj': [u'dummy', major], u'term_in': [term_in], u'sel_to_cred': [u''], u'rsts': [u'dummy'], u'end_ap': [u'y'], u'sel_schd': [u'dummy'], u'sel_crse': [u''], u'SUB_BTN': [u'Course Search '], u'begin_hh': [u'0'], u'begin_mi': [u'0'], u'end_mi': [u'0'], u'path': [u'1'], u'sel_levl': [u'dummy'], u'sel_ptrm': [u'dummy', u'%'], u'end_hh': [u'0'], u'sel_day': [u'dummy'], u'crn': [u'dummy']}

        r = s.post(url=url, data=payload)

        return { 's': s, 'r': r }

    class _UiucCoursesParser(HTMLParser):

        def __init__(self):
                HTMLParser.__init__(self)
                self.print_data = False
                self.courses = []
                self.descriptions = []
                self.internal_string = ""

        def handle_starttag(self, tag, attr):
                if tag == 'td':
                        for a in attr:
                                if a[0] == 'class' and a[1] == 'dddefault':
                                        self.print_data = True

                                        if self.internal_string:
                                                self.descriptions.append(self.internal_string)
                                                self.internal_string = ""

        def handle_data(self, data):
                if self.print_data and data.isdigit():
                        self.courses.append(data)
                        self.print_data = False
                elif self.print_data:
                        self.internal_string = self.internal_string + data.strip('\n')