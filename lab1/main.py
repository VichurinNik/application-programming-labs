import argparse
import datetime
import re


def parsing() -> str:
   """
   Parse command line arguments and returns the file name
   :return: file name
   """
   parser = argparse.ArgumentParser()
   parser.add_argument('file', type=str, help='The name of the file to analyze')
   args = parser.parse_args()
   return args.file


def open_file(filename: str) -> str :
    """
    Reading the contents of a file
    :param namefile: The file name
    :return: A string containing data from a file
    """
    with open(filename, 'r', encoding='utf=8') as file:
       text = file.read()
       return text


def separation_text(text: str) -> list[str]:
   """
    Searches for parser values in the text
    :param text: A line with the words
    :return: A row with birth dates
    """
   pattern = r'\d{2}.\d{2}.\d{4}'
   date = re.findall(pattern, text)
   return date


def counting_birth(separation: list[str]) -> list[str]:
   """
   It is passed along the line with birthdays and will check whether it fits the criteria
   """
   b = 0
   for birthday in separation:
    date_d = datetime.datetime.strptime(birthday, '%d.%m.%Y').date()
    year = date_d.year
    day = date_d.day
    mo = date_d.month
    if 30 < counting_years(day,mo,year) < 40:
        b += 1
   return b


def counting_years(da: int, mo:int, yea:int) -> int:
    """
    Calculates how old a person is
    """
    current_day = datetime.datetime.now().date()
    day = current_day.day-da
    month = current_day.month
    year=current_day.year
    birthday=year-yea
    if (mo > month) or ((mo == month) and da > day):
        birthday -= 1
    return birthday


def main():
   filename = parsing()
   try:
    text = open_file(filename)
    separation = separation_text(text)
    result = counting_birth(separation)
    print('The number of people aged 30 to 40 years:', result)
   except Exception as ex:
       print(ex)


if __name__ == "__main__":
    main()