# Task - 1
PERFECT_SQUARES = [-4, -16, 0, 1, 4, 5, 9, 121, 16, 25, 36, 49, 64, 81, 100]

def find_perfect_squares(lst):
   """
   Bu funksiya verilmiş siyahıdan müsbət tam kvadrat ədədləri tapır və onları artan sıra ilə qaytarır.
   """
   result = [num for num in lst if num > 0 and (num ** 0.5).is_integer()]
   result.sort()
   return result


# Task - 2
MIXED_LIST = [-1, 1, 2, 2, 6, 7, 7, 'say']

def find_unique_elements(lst):
   """
   Bu funksiya verilmiş siyahıdan tək elementləri tapır və onları qaytarır.
   """
   return [elem for elem in lst if lst.count(elem) == 1]


# Task - 3
NUMBER_LIST = [2, 4, 6, 10]

def calculate_product(lst):
   """
   Bu funksiya verilmiş siyahıdakı ədədlərin hasilini hesablayır.
   """
   result = 1
   for num in lst:
       result *= num
   return result


# Task - 4
def find_divisors():
   """
   Bu funksiya istifadəçidən bir ədəd alır və həmin ədədin bölənlərini tapır.
   """
   number = int(input("Ədəd daxil edin: "))
   return [divisor for divisor in range(1, number + 1) if number % divisor == 0]


# Task - 5
MONTH_NAMES = ["yanvar", "fevral", "mart", "aprel", "may", "iyun", "iyul", "avqust", "sentyabr", "oktyabr"]

def get_month_lengths(lst):
   """
   Bu funksiya verilmiş ayların adlarının uzunluğunu qaytarır.
   """
   return {month: len(month) for month in lst}


# Task - 6
CHARACTER_NAMES = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

def get_first_names(lst):
   """
   Bu funksiya verilmiş ad-soyadlardan sadəcə adları kiçik hərflərlə qaytarır.
   """
   return [name.split()[0].lower() for name in lst]


# Task - 7
NUMBERS_1 = [1, 2, 4, 8, 6]
NUMBERS_2 = [4, 5, 6, 1, 2]

def calculate_averages(lst1, lst2):
   """
   Bu funksiya iki siyahının uyğun elementlərinin ortalamasını hesablayır.
   """
   return [(num1 + num2) / 2 for num1, num2 in zip(lst1, lst2)]


def main():
   task_number = int(input("Hansı taskı işə salmaq istəyirsiniz? (1-7 arası rəqəm daxil edin): "))

   if task_number == 1:
       print("Task 1:", find_perfect_squares(PERFECT_SQUARES))
   elif task_number == 2:
       print("Task 2:", find_unique_elements(MIXED_LIST))
   elif task_number == 3:
       print("Task 3:", calculate_product(NUMBER_LIST))
   elif task_number == 4:
       print("Task 4:", find_divisors())
   elif task_number == 5:
       print("Task 5:", get_month_lengths(MONTH_NAMES))
   elif task_number == 6:
       print("Task 6:", get_first_names(CHARACTER_NAMES))
   elif task_number == 7:
       print("Task 7:", calculate_averages(NUMBERS_1, NUMBERS_2))
   else:
       print("Yanlış task nömrəsi daxil edildi.")


if __name__ == "__main__":
   main()