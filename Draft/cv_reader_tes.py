from pandas import date_range
from pyresparser import ResumeParser
data = ResumeParser('resume_test.pdf').get_extracted_data()

print(data)
