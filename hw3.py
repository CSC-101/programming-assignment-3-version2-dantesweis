from build_data import get_data
import data

# Part 1
def population_total(counties: list[data.CountyDemographics]) -> float: # Calculates the total population across all given counties based on the 2014 population data.
    # Parameters: counties (List[data.CountyDemographics]): A list of CountyDemographics objects containing population data.
    # Returns: float: the total population across all countries
    total_population = 0
    for county in counties:
        total_population += county.population.get('2014 Population',0)
    return total_population

# Part 2
def filter_by_state(counties: list[data.CountyDemographics], abbrev: str) -> list[data.CountyDemographics]: # Filters the list of counties to include only those from the specified state.
    # Parameters: counties (List[data.CountyDemographics]): A list of CountyDemographics objects containing population data. abbrev (str): The state abbreviation to filter by.
    # Returns: list[data.CountyDemographics]: A list of counties belonging to the specified state.
    return [county for county in counties if county.state == abbrev]

# Part 3
def population_by_education(counties: list[data.CountyDemographics], education_key: str) -> float: # Calculates the total population by the education percentage for a given education key across counties.
    # Parameters: counties (List[data.CountyDemographics]): A list of CountyDemographics objects containing population data. education_key (str): the key for the education level in the education data.
    # Returns: float: The sum of the population adjusted by the specified education percentage.
    total_population = 0
    for county in counties:
        pop = county.population.get('2014 Population',0)
        education_percentage = county.education.get(education_key, 0) / 100
        total_population += pop * education_percentage

    return total_population

def population_by_ethnicity(counties: list[data.CountyDemographics], ethnicity_key: str) -> float: # Calculates the total population by the ethnicity percentage for a given ethnicity key across counties.
    # Parameters: counties (List[data.CountyDemographics]): A list of CountyDemographics objects containing population data. ethnicity_key (str): the key for the ethnicity in the ethnicity data
    # Returns: float: The sum of the population adjusted by the specified ethnicity percentage.
    total_population = 0
    for county in counties:
        pop = county.population.get('2014 Population', 0)
        ethnicity_percentage = county.ethnicities.get(ethnicity_key, 0) / 100
        total_population += pop * ethnicity_percentage

    return total_population

def population_below_poverty_level(counties: list[data.CountyDemographics]) -> float: # Calculates the total population living below the poverty level across counties.
    # Parameters: counties (List[data.CountyDemographics]): A list of CountyDemographics objects containing population data.
    # Returns: float: The estimated population below the poverty level.
    total_population = 0.0
    for county in counties:
        population_2014 = county.population.get("2014 Population", 0)
        poverty_percentage = county.income.get("Persons Below Poverty Level", 0) / 100
        total_population += population_2014 * poverty_percentage

    return total_population

def percent_by_education(counties: list[data.CountyDemographics], education_key: str) -> float: # Calculates the percentage of the total population that falls under a specific education category.
    # Parameters: counties (List[data.CountyDemographics]): A list of CountyDemographics objects containing population data. education_key (str): the key for the education level in the education data.
    # Returns: float: The percentage of the population with the specified education level.
    total_edu_population = population_by_education(counties, education_key)
    total_pop = population_total(counties)
    if total_pop == 0 or total_edu_population == 0:
        return 0.0
    return total_edu_population / total_pop * 100

def percent_by_ethnicity(counties: list[data.CountyDemographics], ethnicity_key: str) -> float: # Calculates the percentage of the total population that belongs to a specific ethnicity.
    # Parameters: counties (List[data.CountyDemographics]): A list of CountyDemographics objects containing population data. ethnicity_key (str): the key for the ethnicity in the ethnicity data
    # Return: float: The percentage of the population that belongs to the specified ethnicity.
    total_ethnicity_population = population_by_ethnicity(counties, ethnicity_key)
    total_pop = population_total(counties)
    if total_pop == 0 or total_ethnicity_population == 0:
        return 0.0
    return (total_ethnicity_population / total_pop) * 100

def percent_below_poverty_level(counties: list[data.CountyDemographics]) -> float: # Calculates the percentage of the total population that is living below the poverty level.
    # Parameters: counties (List[data.CountyDemographics]): A list of CountyDemographics objects containing population data.
    # Return: float: The percentage of the population living below the poverty level.
    total_poverty_population = population_below_poverty_level(counties)
    total_pop = population_total(counties)

    if total_pop == 0 or total_poverty_population == 0:
        return 0.0
    return (total_poverty_population / total_pop) * 100


def education_greater_than(counties: list[data.CountyDemographics], education_key: str, threshold: float) -> list[data.CountyDemographics]: # Filters the list of counties to include only those where the percentage of people with a specified education level exceeds a given threshold.
    # Parameters: counties (List[data.CountyDemographics]): A list of CountyDemographics objects containing population data. education_key (str): The key representing the education level in the education data. threshold (float): The minimum percentage threshold to filter counties.
    # Returns: List[data.CountyDemographics]: A list of counties where the specified education percentage is greater than the threshold.
    return [county for county in counties if county.education.get(education_key, 0) > threshold]

def education_less_than(counties: list[data.CountyDemographics], education_key: str, threshold: float) -> list[data.CountyDemographics]: # Filters the list of counties to include only those where the percentage of people with a specified education level is below a given threshold.
    # Parameters: counties (List[data.CountyDemographics]): A list of CountyDemographics objects containing population data. education_key (str): The key representing the education level in the education data. threshold (float): The maximum percentage threshold to filter counties.
    # Returns: List[data.CountyDemographics]: A list of counties where the specified education percentage is less than the threshold.
    return [county for county in counties if county.education.get(education_key, 0) < threshold]


def ethnicity_greater_than(counties: list[data.CountyDemographics], ethnicity_key: str, threshold: float) -> list[data.CountyDemographics]: # Filters the list of counties to include only those where the percentage of a specified ethnicity exceeds a given threshold.
    # Parameters: counties (List[data.CountyDemographics]): A list of CountyDemographics objects containing population data. ethnicity_key (str): The key representing the ethnicity in the ethnicity data. threshold (float): The minimum percentage threshold to filter counties.
    # Returns: List[data.CountyDemographics]: A list of counties where the specified ethnicity percentage is greater than the threshold.
    return [county for county in counties if county.ethnicities.get(ethnicity_key, 0) > threshold]


def ethnicity_less_than(counties: list[data.CountyDemographics], ethnicity_key: str, threshold: float) -> list[data.CountyDemographics]:
    # Parameters: counties (List[data.CountyDemographics]): A list of CountyDemographics objects containing population data. ethnicity_key (str): The key representing the ethnicity in the ethnicity data. threshold (float): The minimum percentage threshold to filter counties.
    # Returns: List[data.CountyDemographics]: A list of counties where the specified ethnicity percentage is less than the threshold.
    return [county for county in counties if county.ethnicities.get(ethnicity_key, 0) < threshold]


def below_poverty_level_greater_than(counties: list[data.CountyDemographics], threshold: float) -> list[data.CountyDemographics]: # Filters the list of counties to include only those where the percentage of people below the poverty level exceeds a given threshold.
    # Parameters: counties (List[data.CountyDemographics]): A list of CountyDemographics objects containing population data. threshold (float): The minimum percentage threshold to filter counties.
    # Returns: List[data.CountyDemographics]: A list of counties where the percentage of people below the poverty level is greater than the threshold.
    return [county for county in counties if county.income.get("Persons Below Poverty Level", 0) > threshold]


def below_poverty_level_less_than(counties: list[data.CountyDemographics], threshold: float) -> list[data.CountyDemographics]:
    # Parameters: counties (List[data.CountyDemographics]): A list of CountyDemographics objects containing population data. threshold (float): The minimum percentage threshold to filter counties.
    # Returns: List[data.CountyDemographics]: A list of counties where the percentage of people below the poverty level is less than the threshold.
    return [county for county in counties if county.income.get("Persons Below Poverty Level", 0) < threshold]
