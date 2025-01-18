def filter_square_odd_even(start, end):

    if start > end:
        print("Invalid range: start should be less than or equal to end.")
        return

    odd_squares = []
    even_squares = []

    for number in range(start, end + 1):
        square = number ** 2
        if square % 2 == 0:
            even_squares.append(square)
        else:
            odd_squares.append(square)

    print("Odd Squares:", odd_squares)
    print("Even Squares:", even_squares)


start_range = int(input("Enter the starting range: "))
end_range = int(input("Enter the ending range: "))
filter_square_odd_even(start_range, end_range)
