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


def open_file(filename) -> str :
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


def counting_birth(separation: str) -> list[str]:
   b = 0
   for birthday in separation:
    date_d = datetime.datetime.strptime(birthday, '%d.%m.%Y').date()
    year = date_d.year
    day =date_d.day
    mo = date_d.month
    if 30<counting_years(day,mo,year)<40:
        b+=1
   return b


def counting_years(da: int,mo:int,yea:int)->int:
    """
    Сделал if как вы и сказали, отступы проверил все стоит как у вас.
    """
    current_day = datetime.datetime.now().date()
    day = current_day.day
    month = current_day.month
    year=current_day.year
    Birthday=year-yea
    if( (mo>month) or ((mo==month) and da>day)):
        Birthday-=1
    return Birthday


def main():
   filename = parsing()
   text =  open_file(filename)
   separation = separation_text(text)
   result = counting_birth(separation)
   print('Количество людей возрастом от 30 до 40 лет:', result)

if __name__ == "__main__":
   main()






