def calculate_fine(book_title, days_overdue, daily_rate=5.0, max_fine=150.0):
    fine = days_overdue * daily_rate
    if fine > max_fine:
        return max_fine, True
    return fine, False

book_title = input()
days_overdue = int(input())

fine, max_reached = calculate_fine(book_title, days_overdue)

print(f"Book: {book_title}")
print(f"Days overdue: {days_overdue}")
print(f"Fine: Rs. {fine}")

if max_reached:
    print("You have accumulated the maximum fine of INR: 150.0")