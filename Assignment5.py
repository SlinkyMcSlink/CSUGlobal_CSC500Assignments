# Critical Thinking Assignment 5

# Part 1 - Rain Averages

years = int(input('Number of years to track rainfall: \n'))
total_rainfall = 0
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September' , 'October', 'November', 'December']

for year in range(0, years):
    for month in months:
        monthly_rainfall = int(input('How much rain fell (in inches) in {} of year {}?\n'.format(month, year + 1)))
        total_rainfall += monthly_rainfall

total_months = years * 12
if total_rainfall > 0:
    average_rainfall = total_rainfall / total_months
else:
    average_rainfall = 0

print()
print('RESULTS')
print('***************************************************')
print('Collected Data for {} year(s) - {} months total.'.format(years, total_months))
print('Total Overall rainfall: {} inches.'.format(total_rainfall))
print('Average monthly rainfall: {:.2f} inches.'.format(average_rainfall))
print('***************************************************')
print()
print()


# Part 2 - Bookstore Points

books_purchased = int(input('Hello Valued Customer! How many books have you purchased at CSU Global Bookstore this month?\n'))

points = 0
if books_purchased >= 8:
    points = 60
elif books_purchased >= 6:
    points = 30
elif books_purchased >= 4:
    points = 15
elif books_purchased >= 2:
    points = 5
else:
    points = 0

if points > 0:
    print('{} books?? That is great! You earned {} points this month!'.format(books_purchased, points))
else:
    print('Sorry, you have not purchased enough books to gain any points. You earned 0 points this month.')
    print('You need to purchase {} more book(s) to earn points this month.'.format(2 - books_purchased))



