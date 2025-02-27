import data
import build_data
import unittest
import hw3
from data import CountyDemographics

# These two values are defined to support testing below. The
# data within these structures should not be modified. Doing
# so will affect later tests.
#
# The data is defined here for visibility purposes in the context
# of this course.
full_data = build_data.get_data()

reduced_data = [
    data.CountyDemographics(
        {'Percent 65 and Older': 13.8,
         'Percent Under 18 Years': 25.2,
         'Percent Under 5 Years': 6.0},
        'Autauga County',
        {"Bachelor's Degree or Higher": 20.9,
         'High School or Higher': 85.6},
        {'American Indian and Alaska Native Alone': 0.5,
         'Asian Alone': 1.1,
         'Black Alone': 18.7,
         'Hispanic or Latino': 2.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 1.8,
         'White Alone': 77.9,
         'White Alone, not Hispanic or Latino': 75.6},
        {'Per Capita Income': 24571,
         'Persons Below Poverty Level': 12.1,
         'Median Household Income': 53682},
        {'2010 Population': 54571,
         '2014 Population': 55395,
         'Population Percent Change': 1.5,
         'Population per Square Mile': 91.8},
        'AL'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.0},
        'Crawford County',
        {"Bachelor's Degree or Higher": 14.3,
         'High School or Higher': 82.2},
        {'American Indian and Alaska Native Alone': 2.5,
         'Asian Alone': 1.6,
         'Black Alone': 1.6,
         'Hispanic or Latino': 6.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 2.8,
         'White Alone': 91.5,
         'White Alone, not Hispanic or Latino': 85.6},
        {'Per Capita Income': 19477,
         'Persons Below Poverty Level': 20.2,
         'Median Household Income': 39479},
        {'2010 Population': 61948,
         '2014 Population': 61697,
         'Population Percent Change': -0.4,
         'Population per Square Mile': 104.4},
        'AR'),
    data.CountyDemographics(
        {'Percent 65 and Older': 17.5,
         'Percent Under 18 Years': 18.1,
         'Percent Under 5 Years': 4.8},
        'San Luis Obispo County',
        {"Bachelor's Degree or Higher": 31.5,
         'High School or Higher': 89.6},
        {'American Indian and Alaska Native Alone': 1.4,
         'Asian Alone': 3.8,
         'Black Alone': 2.2,
         'Hispanic or Latino': 22.0,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 3.4,
         'White Alone': 89.0,
         'White Alone, not Hispanic or Latino': 69.5},
        {'Per Capita Income': 29954,
         'Persons Below Poverty Level': 14.3,
         'Median Household Income': 58697},
        {'2010 Population': 269637,
         '2014 Population': 279083,
         'Population Percent Change': 3.5,
         'Population per Square Mile': 81.7},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 11.5,
         'Percent Under 18 Years': 21.7,
         'Percent Under 5 Years': 5.8},
        'Yolo County',
        {"Bachelor's Degree or Higher": 37.9,
         'High School or Higher': 84.3},
        {'American Indian and Alaska Native Alone': 1.8,
         'Asian Alone': 13.8,
         'Black Alone': 3.0,
         'Hispanic or Latino': 31.5,
         'Native Hawaiian and Other Pacific Islander Alone': 0.6,
         'Two or More Races': 5.0,
         'White Alone': 75.9,
         'White Alone, not Hispanic or Latino': 48.3},
        {'Per Capita Income': 27730,
         'Persons Below Poverty Level': 19.1,
         'Median Household Income': 55918},
        {'2010 Population': 200849,
         '2014 Population': 207590,
         'Population Percent Change': 3.4,
         'Population per Square Mile': 197.9},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 19.6,
         'Percent Under 18 Years': 25.6,
         'Percent Under 5 Years': 4.9},
        'Butte County',
        {"Bachelor's Degree or Higher": 17.9,
         'High School or Higher': 89.2},
        {'American Indian and Alaska Native Alone': 1.0,
         'Asian Alone': 0.3,
         'Black Alone': 0.2,
         'Hispanic or Latino': 5.8,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 2.3,
         'White Alone': 96.1,
         'White Alone, not Hispanic or Latino': 90.6},
        {'Per Capita Income': 20995,
         'Persons Below Poverty Level': 15.7,
         'Median Household Income': 41131},
        {'2010 Population': 2891,
         '2014 Population': 2622,
         'Population Percent Change': -9.4,
         'Population per Square Mile': 1.3},
        'ID'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.9},
        'Pettis County',
        {"Bachelor's Degree or Higher": 15.2,
         'High School or Higher': 81.8},
        {'American Indian and Alaska Native Alone': 0.7,
         'Asian Alone': 0.7,
         'Black Alone': 3.4,
         'Hispanic or Latino': 8.3,
         'Native Hawaiian and Other Pacific Islander Alone': 0.3,
         'Two or More Races': 1.9,
         'White Alone': 92.9,
         'White Alone, not Hispanic or Latino': 85.5},
        {'Per Capita Income': 19709,
         'Persons Below Poverty Level': 18.4,
         'Median Household Income': 38580},
        {'2010 Population': 42201,
         '2014 Population': 42225,
         'Population Percent Change': 0.1,
         'Population per Square Mile': 61.9},
        'MO'),
    data.CountyDemographics(
        {'Percent 65 and Older': 18.1,
         'Percent Under 18 Years': 21.6,
         'Percent Under 5 Years': 6.5},
        'Weston County',
        {"Bachelor's Degree or Higher": 17.2,
         'High School or Higher': 90.2},
        {'American Indian and Alaska Native Alone': 1.7,
         'Asian Alone': 0.4,
         'Black Alone': 0.7,
         'Hispanic or Latino': 4.2,
         'Native Hawaiian and Other Pacific Islander Alone': 0.0,
         'Two or More Races': 2.2,
         'White Alone': 95.0,
         'White Alone, not Hispanic or Latino': 91.5},
        {'Per Capita Income': 28764,
         'Persons Below Poverty Level': 11.2,
         'Median Household Income': 55461},
        {'2010 Population': 7208,
         '2014 Population': 7201,
         'Population Percent Change': -0.1,
         'Population per Square Mile': 3.0},
        'WY')
    ]

class TestCases(unittest.TestCase):
    pass

    # Part 1
    # test population_total
    def test_population_total(self):
        pop = build_data.get_data()
        self.assertEqual(hw3.population_total(pop), 318857056)

    # Part 2
    # test filter_by_state
    def test_filter_by_state1(self):
        data1 = build_data.get_data()
        CA = hw3.filter_by_state(data1, 'CA')
        self.assertEqual(len(CA), 58)

    def test_filter_by_state2(self):
        data1 = build_data.get_data()
        unknown = hw3.filter_by_state(data1, 'UK')
        self.assertEqual(len(unknown), 0)
    # Part 3
    # test population_by_education
    def test_population_by_education(self):
        data1 = reduced_data
        slo_county = [county for county in data1 if county.county == "San Luis Obispo County"]
        result = hw3.population_by_education(slo_county, "Bachelor's Degree or Higher")
        self.assertEqual(result, 87911.145)

    def test_population_by_education2(self):
        data1 = reduced_data
        result = hw3.population_by_education(data1, "Nonexistent Degree")
        self.assertEqual(result, 0)

    # test population_by_ethnicity
    def test_population_by_ethnicity(self):
        data1 = reduced_data
        CA = [county for county in data1 if county.state == "CA"]
        result = hw3.population_by_ethnicity(CA, "Two or More Races")
        expected_result = ((279083 * 0.034) + (207590 * 0.050))
        self.assertEqual(result, expected_result)

    def test_population_by_ethnicity2(self):
        data1 = reduced_data
        result = hw3.population_by_ethnicity(data1, "Nonexistent Ethnicity")
        self.assertEqual(result, 0)

    # test population_below_poverty_level
    def test_population_below_poverty_level1(self):
        data1 = reduced_data
        CA: list[CountyDemographics] = [county for county in data1 if county.state == "CA"]
        result = hw3.population_below_poverty_level(CA)
        expected_result = (279083 * 0.143) + (207590 * 0.191)
        self.assertAlmostEqual(result, expected_result)

    def test_population_below_poverty_level2(self):
        result = hw3.population_below_poverty_level([])
        self.assertEqual(result, 0)

    # Part 4
    # test percent_by_education
    def test_percent_by_education(self):
        data1 = reduced_data
        CA = [county for county in data1 if county.state == "CA"]
        result = hw3.percent_by_education(CA, "Bachelor's Degree or Higher")
        total_edu_population = (279083 * 0.315) + (207590 * 0.379)
        total_pop = sum(county.population.get("2014 Population", 0) for county in CA)
        expected_result = (total_edu_population / total_pop) * 100
        self.assertAlmostEqual(result, expected_result)

    def test_percent_by_education2(self):
        data1 = reduced_data
        CA = [county for county in data1 if county.state == "CA"]
        result = hw3.percent_by_education(CA, "Invalid Key")
        self.assertEqual(result, 0)
    # test percent_by_ethnicity
    def test_percent_by_ethnicity(self):
        data1 = reduced_data
        CA = [county for county in data1 if county.state == "CA"]
        result = hw3.percent_by_ethnicity(CA, "Two or More Races")
        total_ethnicity_population = (279083 * 0.034) + (207590 * 0.050)
        total_pop = sum(county.population.get("2014 Population", 0) for county in CA)
        expected_result = (total_ethnicity_population / total_pop) * 100
        self.assertAlmostEqual(result, expected_result)

    def test_percent_by_ethnicity2(self):
        data1 = reduced_data
        ca_counties = [county for county in data1 if county.state == "CA"]
        result = hw3.percent_by_ethnicity(ca_counties, "Invalid Key")
        self.assertEqual(result, 0)

    # test percent_below_poverty_level
    def test_percent_below_poverty_level(self):
        data1 = reduced_data
        ca_counties = [county for county in data1 if county.state == "CA"]
        result = hw3.percent_below_poverty_level(ca_counties)
        total_poverty_population = (279083 * 0.143) + (207590 * 0.191)  # Only CA counties
        total_pop = sum(county.population.get("2014 Population", 0) for county in ca_counties)
        expected_result = (total_poverty_population / total_pop) * 100
        self.assertAlmostEqual(result, expected_result)

    def test_percent_below_poverty_level2(self):
        result = hw3.percent_below_poverty_level([])
        self.assertEqual(result, 0)

    # Part 5
    # test education_greater_than
    def test_education_greater_than(self):
        data1 = reduced_data
        result = hw3.education_greater_than(data1, "Bachelor's Degree or Higher", 30.0)
        expected_counties = [county for county in data1 if county.education.get("Bachelor's Degree or Higher", 0) > 30.0]
        self.assertEqual(result, expected_counties)

    def test_education_greater_than2(self):
        data1 = reduced_data
        result = hw3.education_greater_than(data1, "Bachelor's Degree or Higher", 100.0)
        self.assertEqual(result, [])
    # test education_less_than
    def test_education_less_than1(self):
        data1 = reduced_data
        result = hw3.education_less_than(data1, "Bachelor's Degree or Higher", 20.0)
        expected_counties = [county for county in data1 if county.education.get("Bachelor's Degree or Higher", 0) < 20.0]
        self.assertEqual(result, expected_counties)

    def test_education_less_than2(self):
        data1 = reduced_data
        result = hw3.education_less_than(data1, "Bachelor's Degree or Higher", 0.0)
        self.assertEqual(result, [])

    # test ethnicity_greater_than
    def test_ethnicity_greater_than(self):
        data1 = reduced_data
        result = hw3.ethnicity_greater_than(data1, "Hispanic or Latino", 30.0)
        expected_counties = [county for county in data1 if county.ethnicities.get("Hispanic or Latino", 0) > 30.0]
        self.assertEqual(result, expected_counties)

    def test_ethnicity_greater_than2(self):
        data1 = reduced_data
        result = hw3.ethnicity_greater_than(data1, "Hispanic or Latino", 100.0)
        self.assertEqual(result, [])
    # test ethnicity_less_than
    def test_ethnicity_less_than1(self):
        data1 = reduced_data
        result = hw3.ethnicity_less_than(data1, "Hispanic or Latino", 20.0)
        expected_counties = [county for county in data1 if county.ethnicities.get("Hispanic or Latino", 0) < 20.0]
        self.assertEqual(result, expected_counties)

    def test_ethnicity_less_than2(self):
        data1 = reduced_data
        result = hw3.ethnicity_less_than(data1, "Hispanic or Latino", 0.0)
        self.assertEqual(result, [])
    # test below_poverty_level_greater_than
    def test_below_poverty_level_greater_than1(self):
        data1 = reduced_data
        result = hw3.below_poverty_level_greater_than(data1, 20.0)
        expected_counties = [county for county in data1 if county.income.get("Persons Below Poverty Level", 0) > 20.0]
        self.assertEqual(result, expected_counties)

    def test_below_poverty_level_greater_than2(self):
        data1 = reduced_data
        result = hw3.below_poverty_level_greater_than(reduced_data, 100.0)
        self.assertEqual(result, [])


    # test below_poverty_level_less_than
    def test_below_poverty_level_less_than1(self):
        data1 = reduced_data
        result = hw3.below_poverty_level_less_than(data1, 15.0)
        expected_counties = [county for county in data1 if county.income.get("Persons Below Poverty Level", 0) < 15.0]
        self.assertEqual(result, expected_counties)

    def test_below_poverty_level_less_than2(self):
        data1 = reduced_data
        result = hw3.below_poverty_level_less_than(data1, 0.0)
        self.assertEqual(result, [])



if __name__ == '__main__':
    unittest.main()
