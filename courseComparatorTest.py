import unittest
from penn.registrar import Registrar

class TestCourseComparator(unittest.TestCase):

	r = Registrar("UPENN_OD_emFc_1001364", "6kl4eonkquheuti65e32qick6l")

	cis262 = r.section('cis', '262', '001')
	cis320 = r.section('cis', '320', '001')
	cis380 = r.section('cis', '380', '001')

	def test_single_course_no_conflict(self):

	def test_single_course_conflict(self):

	def test_multiple_courses_some_conflicts(self):

